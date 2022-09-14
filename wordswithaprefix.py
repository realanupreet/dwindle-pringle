words = ["pay", "attention", "practice", "attend"]
pref = "at"
n = 0
for w in words:
    if w[:len(pref)] == pref:
        n += 1
