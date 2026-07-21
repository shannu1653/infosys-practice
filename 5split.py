#split converts or sperates string to  list
name="Python is easy and Python is powerful"
print(name.split())
name="Python,is,easy,and,Python,is,powerful"
print(name.split(","))
name="Python is easy and Python is powerful"
print(name.split(" ",2))
text = "Python  is  easy"
print(text.split(" "))
print(len(text.split(" ")))
print(text.split())
print(len(text.split()))


#print each word
text = "Python is powerful"
for i in text:
    print(i)
for word in text.split():
    print(word)