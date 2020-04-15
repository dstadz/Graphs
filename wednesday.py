# My Team: Emoji react to this
def find_ladder(start, end, dictionary):
    q = []
    q.append((start, []))
    while len(q) > 0:
        node = q.pop(0)
        word = node[0]
        path = node[1].copy()
        path.append(word)
        for i in range(len(word)):
            letter = word[i]
            for char in range(ord("a"), ord("z")+1):
                char_actual = chr(char)
                word = word[:i] + char_actual + word[i+1:]
                if word in dictionary:
                    dictionary.remove(word)
                    q.append((word, path))
            word = word[:i] + letter + word[i+1:]
        if word == end:
            return path
    return None
dictionary = set()
with open("words.txt", "r") as f:
    for word in f.readlines():
        dictionary.add(word[:-1])
print(find_ladder("hit", "erghqreh", dictionary))