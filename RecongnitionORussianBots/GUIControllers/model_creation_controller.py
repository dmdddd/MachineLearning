from GUI.model_creation import Ui_NewModelConfiguration
from train_model import *


class NewModelConfiguration(QtWidgets.QMainWindow, Ui_NewModelConfiguration):

    trained_model = None
    textEditField = None
    is_training = None

    def __init__(self, parent=None):
        super(NewModelConfiguration, self).__init__(parent)
        self.setupUi(self)

        self.embeddingModelBrowseButton.clicked.connect(lambda state, args=["*.bin", "model"]:
                                                        self.load_file(args))
        self.dataSetDirectoryBrowseButton.clicked.connect(lambda state, args=["*", "data"]:
                                                          self.load_file(args))
        self.trainingValidationSlider.valueChanged.connect(self.slider_callback)
        self.trainModelButton.clicked.connect(self.pass_arguments_for_training)
        self.saveModelButton.clicked.connect(self.save_trained_model)
        self.modelConfigurationBackButton.clicked.connect(self.close_return)
        self.textEditField = self.trainingSummaryTextEdit
        self.additionalInfoButton.clicked.connect(self.show_additional_info)

        self.is_training = 0

    def load_file(self, args):
        extension = args[0]
        type_of_extension = args[1]

        if type_of_extension == "model":
            file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Model File', os.getenv('HOME'),
                                                              extension)[0]
            if file_path != "":
                self.embeddingModelLineEdit.setText(file_path)

        if type_of_extension == "data":
            file_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select File/Directory', os.getenv('HOME'),
                                                                   QtWidgets.QFileDialog.ShowDirsOnly |
                                                                   QtWidgets.QFileDialog.DontResolveSymlinks)
            if file_path != "":
                self.dataSetDirectoryLineEdit.setText(file_path)

    def pass_arguments_for_training(self):
        embedding_model_path = self.embeddingModelLineEdit.text()
        if embedding_model_path == "":
            self.display_error_message('Please, select embedding model for training!')
            return

        data_set_directory = self.dataSetDirectoryLineEdit.text()
        if data_set_directory == "":
            self.display_error_message('Please, select data set directory!')
            return

        vector_size = self.vectorSizeSpinBox.value()
        if vector_size <= 0:
            self.display_error_message('The vector size must be greater than zero!')
            return

        kernel_size = self.kernelSizeSpinBox.value()
        if kernel_size <= 0:
            self.display_error_message('The kernel size must be greater than zero!')
            return

        nb_filters = self.FiltersNumberSpinBox.value()
        dense_output = self.denseOutputSpinBox.value()
        pool_size = self.poolSizeSpinBox.value()
        epochs = self.epochsSpinBox.value()
        learning_rate = self.learningRateSpinBox.value()
        momentum = self.momentumSpinBox.value()
        decay = self.decaySpinBox.value()
        dropout = self.dropoutSpinBox.value()
        training_pecrentage = self.trainingValidationSlider.value()
        training_pecrentage = training_pecrentage / 100.0

        self.is_training = 1

        X, Y = prepare_input(self, embedding_model_path, data_set_directory, int(vector_size))
        if X is None or Y is None:
            self.is_training = 0
            self.trainingSummaryTextEdit.clear()
            self.trainingSummaryTextEdit.repaint()
            return

        self.trained_model = train_model(self, X, Y, int(vector_size), int(kernel_size),
                                         int(nb_filters), int(pool_size), int(dense_output), learning_rate,
                                         momentum, decay, int(epochs), dropout, training_pecrentage)

        self.display_information_message('The training has been finished!')
        self.is_training = 0

        if self.trained_model is not None:
            self.saveModelButton.setEnabled(True)

    def slider_callback(self):
        percentage = self.trainingValidationSlider.value()
        percentage_text = str(percentage) + "%"
        self.trainingPercentageLineEdit.setText(percentage_text)
        percentage = 100 - percentage
        percentage_text = str(percentage) + "%"
        self.validationPercentageLineEdit.setText(percentage_text)

    def save_trained_model(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Dialog Title', os.getenv('HOME'))[0]
        if file_path != "":  # Otherwise the program crashes if Cancel is clicked
        # file_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select File/Directory', os.getenv('HOME'),
        #                                                        QtWidgets.QFileDialog.ShowDirsOnly |
        #                                                        QtWidgets.QFileDialog.DontResolveSymlinks)
            self.trained_model.save(file_path)

            if os.path.isfile(file_path):
                self.display_information_message("Model has been saved")


    def close_return(self):
        self.close()
        self.parent().show()

    def closeEvent(self, event):
        if self.is_training == 1:
            reply = QMessageBox.question(QMessageBox(), 'Message', "Are you sure to quit?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def show_additional_info(self):
        self.display_information_message("1. Load embedding model file.\n\n2.Choose directory, in which must be two "
                                         "sub directories named \"1\" and \"2\", each includes text files "
                                         "for training.")

    def display_information_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Information")
        msg.exec_()

    def display_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
