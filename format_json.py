import json

def read_json_file():
    with open("files\\newsafr.json", encoding="utf-8") as f:
        file_json = json.load(f)
    return file_json

def counting_simbols_in_words():
    words_list = str()
    for items in read_json_file()["rss"]["channel"]["items"]:
        words_list += items["description"]
    descriptions_list = words_list.split()
    long_words = []
    for word in descriptions_list:
        if len(word) > 6:
            long_words.append(word.lower())
    return long_words

def counting_words():
    words_value = {}
    for word in counting_simbols_in_words():
        if word in words_value:
            words_value[word] += 1
        else:
            words_value[word] = 1
    return words_value

def derivation_top_10_words():
    l = lambda counting_words: counting_words[1]
    sort_list = sorted(counting_words().items(), key=l, reverse=True)
    count = 1
    top_10_words = {}
    for word in sort_list:
        top_10_words[count] = word
        count += 1
        if count == 11:
            break
    print(top_10_words)

if __name__ == "__main__":
    derivation_top_10_words()