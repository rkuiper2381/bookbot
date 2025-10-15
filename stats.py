def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    chars = {}

    for c in text:
        if c in chars.keys():
            chars[c] = chars[c] + 1
        else:
            chars[c] = 1

    return chars

def chars_sorted(text):
    chars = count_chars(text)
    sorted = []

    for i in chars:
        sorted.append({ "char":i, "num":chars[i] })

    sorted.sort(reverse=True, key=sort_on)

    return sorted

def sort_on(dictionary):
    return dictionary["num"]
