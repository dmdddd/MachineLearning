from TextProcessing.mystem_preprocessor import *
import numpy as np
import re, os
from pymystem3 import Mystem
from gensim.models import KeyedVectors
from PyQt5.QtWidgets import QMessageBox

######################################
# A function that processes books
# Input: a book, model for text embedding
# Output: array of vectors
######################################
def process_books(GUI, embedding_model_path, dir_path):
    from gensim.models import KeyedVectors
    model = KeyedVectors.load_word2vec_format(embedding_model_path, binary=True)
    words_in_model = model.wv
    stemModel = Mystem()
    mapping = np.load("TextProcessing/tags.npy", allow_pickle=True).item()

    dataset_path = dir_path
    labels = ["1", "2"]

    no_data = False
    for label in labels:
        file_index = 1
        dir_path = os.path.join(dataset_path, label)
        # Get a list of books
        books = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if
                 (os.path.isfile(os.path.join(dir_path, f)) and f.endswith(".txt"))]
        if len(books) == 0:
            no_data = True

    if no_data is False:
        for author in labels:
            file_index = 1
            dir_path = os.path.join(dataset_path, author)
            # Get a list of books
            books = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if (os.path.isfile(os.path.join(dir_path, f)) and f.endswith(".txt"))]

            for book in books:
                print('[' + author + '] Processing book number ' + str(file_index))
                GUI.trainingSummaryTextEdit.append('[' + author + '] Processing book number ' + str(file_index))
                GUI.trainingSummaryTextEdit.repaint()
                with open(book, 'r', encoding='utf8') as file:
                    data = file.read().replace('\n', '')

                processed_words, word_to_tag_mapping_dictionary = tag_mystem(stemModel, mapping, text=data)

                tags = ['ADJ', 'ADV', 'DET', 'SCONJ', 'INTJ', 'NUM', 'PART', 'ADP', 'NOUN', 'PRON', 'VERB']
                words_vectors = []

                for pr_word in processed_words:
                    # for pr_word in processed_words:
                    # If word is not in vocabulary tries other tags
                    if pr_word not in words_in_model:
                        for tag in tags:
                            pr_word = pr_word.split('_')[0]
                            pr_word = pr_word + '_' + tag
                            if pr_word in words_in_model:
                                break

                    # Checks whether the word after tagging is in vocabulary
                    if pr_word in words_in_model:
                        words_vectors.append(words_in_model[pr_word])

                words_vectors = np.array(words_vectors)

                np.save(os.path.join(dir_path, str(file_index)) + '.npy', words_vectors)

                file_index += 1
                file.close()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("One or more of data set sub directories for training is empty!")
        msg.setWindowTitle("Error")
        msg.exec_()
        return 0

    return 1


######################################
# A function that processes tweets
# Input: a list of tweets, model for text embedding
# Output: array of vectors
######################################
def process_tweets(GUI, tweets, tags_mapping, word_embedding_model_path="TextProcessing/model.bin"):
    model = KeyedVectors.load_word2vec_format(word_embedding_model_path, binary=True)
    vector_mapping_dictionaries = []
    embedded_tweets = []
    tweets_to_remove = []  # I there is a tweet with no valid words, remove it
    # Pre loading tools
    stemModel = Mystem()
    mapping = np.load(tags_mapping, allow_pickle=True).item()
    word_vectors = model.wv
    index = 0
    for tweet in tweets:
        index += 1
        embedded_tweet = []
        word_to_vector_mapping_dictionary = {}
        # remove URLs
        tweet = re.sub(r"http\S+", "", tweet)

        print("Tweet " + str(index) + "/" + str(len(tweets)) + ": " + tweet)
        GUI.classificationSummaryTextEdit.append("Tweet " + str(index) + "/" + str(len(tweets)) + ": " + str(tweet))
        GUI.classificationSummaryTextEdit.repaint()

        processed_words, word_to_tag_mapping_dictionary = tag_mystem(stemModel, mapping, text=tweet)
        tags = ['ADJ', 'ADV', 'DET', 'SCONJ', 'INTJ', 'NUM', 'PART', 'ADP', 'NOUN', 'PRON', 'VERB']
        for word in processed_words:
            pr_word = word
            # for pr_word in processed_words:
            # If word is not in vocabulary tries other tags
            if pr_word not in word_vectors:
                for tag in tags:
                    pr_word = pr_word.split('_')[0]
                    pr_word = pr_word + '_' + tag
                    if pr_word in word_vectors:
                        break
            # Checks whether the word after tagging is in vocabulary
            if pr_word in word_vectors:
                tweet_vec = word_vectors[pr_word]
                embedded_tweet.append(tweet_vec)
                word_to_vector_mapping_dictionary[word_to_tag_mapping_dictionary[word]] = tweet_vec

        # # pads the tweets for prediction
        # padded_embedded_tweet = np.zeros((50, 300))
        # embedded_tweet = np.asarray(embedded_tweet)
        # padded_embedded_tweet[:embedded_tweet.shape[0], :embedded_tweet.shape[1]] = embedded_tweet
        # embedded_tweets.append(padded_embedded_tweet)
        if embedded_tweet != [] and len(embedded_tweet) <= 50:
            embedded_tweets.append(np.asarray(embedded_tweet))
            vector_mapping_dictionaries.append(word_to_vector_mapping_dictionary)
        else:
            tweets_to_remove.append(index - 1)

    return vector_mapping_dictionaries, embedded_tweets, tweets_to_remove
# words_vectors = []
# tweet_in_words = tweet.split(" ")
# for word in tweet_in_words:
#     processed_words = tag_mystem(text=word)
#     tags = ['ADJ', 'ADV', 'DET', 'SCONJ', 'INTJ', 'NUM', 'PART', 'ADP', 'NOUN', 'PRON', 'VERB']
#     for pr_word in processed_words:
#         # for pr_word in processed_words:
#         # If word is not in vocabulary tries other tags
#         if pr_word not in model.wv:
#             for tag in tags:
#                 pr_word = pr_word.split('_')[0]
#                 pr_word = pr_word + '_' + tag
#                 if pr_word in model.wv:
#                     break
#         # Checks whether the word after tagging is in vocabulary
#         if pr_word in model.wv:
#             item = [word, model.wv[pr_word]]
#             words_vectors.append(item)
#         else:
#             item = [word, None]
#             words_vectors.append(item)
# embedded_tweets.append(words_vectors)

    return embedded_tweets