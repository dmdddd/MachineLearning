# Stemming and processing the text
# Input: text
# Output: a list of tagged words
#   * returning only the words we've found tags to
def tag_mystem(stemModel, mapping, text='Текст нужно передать функции в виде строки!'):
    processed = stemModel.analyze(text)
    tagged = []
    mapping_dictionary = {}
    for w in processed:
        try:
            lemma = w["analysis"][0]["lex"].lower().strip()
            pos = w["analysis"][0]["gr"].split(',')[0]
            pos = pos.split('=')[0].strip()
            if pos in mapping:
                tagged_word = lemma + '_' + mapping[pos]
                tagged.append(tagged_word)  # здесь мы конвертируем тэги
                mapping_dictionary[tagged_word] = w['text']
            else:
                tagged_word = lemma + '_X'
                tagged.append(tagged_word)  # на случай, если попадется тэг, которого нет в маппинге
                mapping_dictionary[tagged_word] = w['text']

        except KeyError:
            continue  # я здесь пропускаю знаки препинания, но вы можете поступить по-другому
        except IndexError:
            continue
    return tagged, mapping_dictionary
