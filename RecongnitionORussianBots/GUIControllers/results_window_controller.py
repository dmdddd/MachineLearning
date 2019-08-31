from GUI.results_window import Ui_ResultsWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os, csv, json, webbrowser
import tempfile


class ResultsWindow(QtWidgets.QMainWindow, Ui_ResultsWindow):
    tweets = []
    sil_val = 0
    clustering = []
    mapped_tweets = []
    group_one = []
    group_two = []
    loaded_results = False
    loaded_path = None

    # def __init__(self, parent=None):
    #     super(ResultsWindow, self).__init__(parent)
    #     self.setupUi(self)
    #
    #     self.saveResultsButton.clicked.connect(self.save_results)
    #     self.loadResultsButton.clicked.connect(self.load_results)
    #     self.backButton.clicked.connect(self.closeAndReturn)

    def __init__(self, clustering, tweets, sil_score, mapped_tweets, parent=None):
        super(ResultsWindow, self).__init__(parent)
        self.setupUi(self)

        self.saveResultsButton.clicked.connect(self.save_results)
        self.loadResultsButton.clicked.connect(self.load_results)
        self.backButton.clicked.connect(self.closeAndReturn)

        self.sil_val = sil_score
        self.clustering = clustering
        self.tweets = tweets
        self.mapped_tweets = mapped_tweets

        if len(self.group_two) == 0:
            self.showGroupTwoSal.setEnabled(False)
            if len(self.group_one) == 0:
                self.showGroupOneSal.setEnabled(False)
        if len(self.tweets) == 0:
            self.saveResultsButton.setEnabled(False)

        if self.tweets is not []:
            self.update_display()

        self.showGroupOneSal.clicked.connect(self.show_saliency_group_one)
        self.showGroupTwoSal.clicked.connect(self.show_saliency_group_two)

    @QtCore.pyqtSlot()
    def load_results(self):
        self.groupOneBox.setText("")
        self.groupTwoBox.setText("")
        results_dir_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Result Directory', os.getenv('HOME'))
        if results_dir_path != "":  # Otherwise the program crashes if Cancel is clicked
            first_csv = os.path.join(results_dir_path, "group1.csv")
            if os.path.isfile(first_csv):
                with open(first_csv, encoding='utf16') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=",")
                    for row in csv_reader:
                        for tweet in row:
                            if tweet != "":
                                self.groupOneBox.append(tweet + "\n")
                self.showGroupOneSal.setEnabled(True)

            second_csv = os.path.join(results_dir_path, "group2.csv")
            if os.path.isfile(second_csv):
                with open(os.path.join(results_dir_path, "group2.csv"), encoding='utf16') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=",")
                    for row in csv_reader:
                        for tweet in row:
                            if tweet != "":
                                self.groupTwoBox.append(tweet + "\n")
                self.showGroupTwoSal.setEnabled(True)

            self.loaded_results = True
            self.loaded_path = results_dir_path

            # self.humanTextEdit.setHtml(open(results_file_path).read())
            # self.humanTextEdit.page().mainFrame().evaluateJavaScript(str(open("/script.js").read()))

    @QtCore.pyqtSlot()
    def save_results(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(None, 'Dialog Title', os.getenv('HOME'))[0]
        if file_name != "":  # Otherwise the program crashes if Cancel is clicked
            os.mkdir(file_name)
            with open(os.path.join(file_name, 'group1.csv'), 'w', newline='', encoding='utf16') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='|')
                if self.sil_val > 0.5:
                    index = -1
                    for tweet in self.tweets:
                        index += 1
                        if self.clustering[index] == 0:
                            filewriter.writerow([tweet])
                else:
                    for tweet in self.tweets:
                        filewriter.writerow([tweet])
            # Creating a second file only if there were two groups
            if self.sil_val > 0.5:
                with open(os.path.join(file_name, 'group2.csv'), 'w', newline='', encoding='utf16') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar='|')
                    index = -1
                    for tweet in self.tweets:
                        index += 1
                        if self.clustering[index] == 1:
                            filewriter.writerow([tweet])

        create_sal_wiz_file(self.group_one, os.path.join(file_name, 'group1.html'))
        print(len(self.group_two))
        if len(self.group_two) > 0:
            create_sal_wiz_file(self.group_two, os.path.join(file_name, 'group2.html'))

    def closeAndReturn(self):
        self.close()
        self.parent().show()

    def update_display(self):
        self.groupOneBox.setText("")
        self.groupTwoBox.setText("")
        if self.sil_val > 0.5:
            self.messageLabel.setText("Given data has been split into two groups")
            index = -1
            for tweet in self.tweets:
                index += 1
                if self.clustering[index] == 0:
                    self.groupOneBox.append(tweet + "\n")
                    self.group_one.append(self.mapped_tweets[index])
                else:
                    self.groupTwoBox.append(tweet + "\n")
                    self.group_two.append(self.mapped_tweets[index])

        else:
            self.messageLabel.setText("Given data was too syntactically similar to split into two groups")
            for tweet in self.tweets:
                self.groupOneBox.append(tweet + "\n")

            self.group_one = self.mapped_tweets

        if len(self.group_one) > 0:
            self.showGroupOneSal.setEnabled(True)
        if len(self.group_two) > 0:
            self.showGroupTwoSal.setEnabled(True)

    def show_saliency_group_one(self):
        if self.load_results and self.loaded_path is not None:
            first_html = os.path.join(self.loaded_path, "group1.html")
            if os.path.isfile(first_html):
                url = "file://" + first_html
                webbrowser.open(url, new=2)
        else:
            file = create_sal_wiz_file(self.group_one)

            url = "file://" + file.name
            webbrowser.open(url, new=2)

    def show_saliency_group_two(self):
        if self.load_results and self.loaded_path is not None:
            first_html = os.path.join(self.loaded_path, "group2.html")
            if os.path.isfile(first_html):
                url = "file://" + first_html
                webbrowser.open(url, new=2)

        else:
            file = create_sal_wiz_file(self.group_two)

            url = "file://" + file.name
            webbrowser.open(url, new=2)


def create_sal_wiz_file(mapped_data_, path=None):
    tmp_json_file = tempfile.NamedTemporaryFile("w", delete=False, suffix='.json')

    with open(tmp_json_file.name, 'w') as fd:
        fd.write(json.dumps(mapped_data_))
    tmp_json_file.close()

    with open(tmp_json_file.name, "r") as fp:
        data = json.load(fp)

    beginning_html_str = '''
        <!DOCTYPE html>
        <html>
            <head>
                    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
            </head>
        <body>
        '''

    vars_html_str = '''</body>
        <script>
        '''
    functions_html_str = ""
    end_html_str = '''</script>
        </html>'''
    index = 0
    for tweet in data:
        index += 1
        beginning_html_str += '''
        <div id="text_''' + str(index) + '''">text goes here</div>'''

        vars_html_str += "var words_" + str(index) + " = "
        vars_html_str += json.dumps(tweet)
        vars_html_str += ''';
        '''

        functions_html_str += '''
        $("#text_''' + str(index) + '''").html($.map(words_''' + str(index) + ''', function(w) {
        var z = document.createElement("span");
        // we have to normalize to: 1(black) to 100(white)
        z.style.backgroundColor = 'hsl(360,100%,' + w.sal + '%)';
        z.textContent = w.word + " ";
        return z;
        }))
        '''

    full_html_str = beginning_html_str + vars_html_str + functions_html_str + end_html_str

    # Working on a temp file
    if path is None:
        Html_file = tempfile.NamedTemporaryFile("w", delete=False, suffix='.html')
        Html_file.write(full_html_str)
        Html_file.close()

    else:
        Html_file = open(path, "w")
        Html_file.write(full_html_str)
        Html_file.close()

    return Html_file
