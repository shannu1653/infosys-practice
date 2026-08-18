sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
]

for sentence in sentences:
    print(len(sentence.split()))




sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
]
for s in sentences:
    count = 1
    for ch in s:
        print(ch,end="")
        if ch == " ":
            count += 1
    print(count)



def dict_merge(dict1,dict2):
    for i in dict2:
        if i in dict1:
            dict1[i]+=dict2[i]
        else:
            dict1[i]=dict2[i]
    return dict1

dict1={"a":1,"b":2,"c":3}
dict2={"a":3,"b":3,"d":5}
print(dict_merge(dict1,dict2))
