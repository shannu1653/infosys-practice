name="Python is easy and Python is powerful"
Vowels=0
Consonants=0
for i in name:
    if i.isalpha():
        if  i.lower()  in "aeiou":
            Vowels+=1
        else:
            Consonants+=1
freq={}
for word in name.split():
    freq[word]=freq.get(word,0)+1
print(f"Vowels = {Vowels}")
print(f"Consonants = {Consonants}")
print(f"Word Frequency : ")
for word,count in freq.items():
    print(f"{word} : {count}")
