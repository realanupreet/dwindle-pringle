# sentences = [
#     "alice and bob love leetcode", 
#     "i think so too", 
#     "this is great thanks very much"
#     ]

sentences = ["please wait", "continue to fight", "continue to win"]

maxwords=0
for sentence in sentences:
    workcount=0
    wordcount = len(sentence.split(' '))
    if wordcount>maxwords:
        maxwords = wordcount
print(maxwords)