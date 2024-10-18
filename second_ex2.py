line = "which is better python 2 or python 3"
def word_frequency(line):
    out = line.split()
    word = []
    for i in out:
        print(i)
        word.append((i,out.count(i)))
    print(word)
#     for i in sorted(word):
#         print(f"{i}: {word[i]}")
line = "which is better python 2 or python 3"
word_frequency(line)