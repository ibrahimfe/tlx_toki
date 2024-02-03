import re

pattern = input().strip()
n = int(input())

matched_words = []
for _ in range(n):
    word = input().strip()
    if re.match(pattern.replace('*', '.*'), word):
        matched_words.append(word)

for word in matched_words:
    print(word)
