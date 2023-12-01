with open('in.txt') as f:
    text = f.read()

total = 0
words = ['one','two','three','four','five','six','seven','eight','nine']
for line in text.split('\n'):
    first = 0
    for pos in range(len(line)):
        for i, word in enumerate(words):
            i += 1
            if line[pos:pos+len(word)] == word or line[pos] == str(i):
                if first == 0:
                    first = i
                last = i

    total += first * 10 + last

print(total)