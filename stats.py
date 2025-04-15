def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    for char in text.lower():  # Convert to lowercase
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(dict):
    return dict["num"]

def sorted_count(count):
    ret = []
    for key in count.keys():
        ret.append({"char":key, "num":count[key]})
    ret.sort(reverse=True, key=sort_on)
    return ret