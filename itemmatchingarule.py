items = [
    ["phone","blue","pixel"],
    ["computer","silver","lenovo"],
    ["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
rks=["type","color","name"]
for i in range(len(rks)):
    if rks[i] == ruleKey:
        print(i)
        break
count=0
for t in items:
    # print(t[i])
    if t[i] == ruleValue:
        print(t[i])
        count+=1
