sentence = "leetcode"
hashmap={}
missed=[]
if len(sentence)>=26 :
    for ch in sentence.lower():
        hashmap[ch]=hashmap.get(ch,0)+1
    for i in range(ord('a'),ord("z")+1):
        if chr(i) in hashmap:
            hashmap[chr(i)]-=1
        else:
            missed.append(chr(i))
            hashmap[chr(i)]-=1
    for i in hashmap.values():
        if i<0:
            print("Not a Panagram")
            break
    else:
        print("Panagram")
else:
    print("Not a Panagram")
    for i in range(ord('a'),ord("z")+1):
        if chr(i) not in sentence:
            missed.append(chr(i))
print(missed)