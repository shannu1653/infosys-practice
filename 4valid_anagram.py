#Valid anagram 242

#1.method brute force count gives O(n2)
s = "anagram"
t = "nagaram"
for i in s:
    if s.count(i)!= t.count(i):
        print('False')
        break
else:
    print("True")

#2.HashMap
s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print("False")
else:
    new_dict={}
    for i in s:
        new_dict[i] = new_dict.get(i, 0) + 1
    for i in t:
        if i not in new_dict:
            print("False")
            break
        new_dict[i]-=1
    else:
        for value in new_dict.values():
            if value !=0:
                print("False")
        else:
            print("True")

name='anagram'
freq={}
for ch in name:
    freq[ch]=freq.get(ch,0)+1
print(freq)
for i in name:
    print(name.count(i))