def freq_words(text):
    text = str(text).lower()
    word_list = text.split(' ')
    out = {}
    for word in word_list:
        if word not in out:
            out[word] = 1
        else:
            tmp = int(out[word])
            out[word] = tmp + 1
    return sort(out)


