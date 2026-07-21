'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''


#Approach 1: Preprocessing + Two Pointers
'''Time Complexity: O(n)
Space Complexity: O(n) (extra list is used)'''

s="A man, a plan, a canal: Panama"
print(s)
rev=[]
for i in s.lower():
    if i.isalnum():
        rev.append(i)
print(rev)
left=0
right=len(rev)-1
while left<right:
    if rev[left] != rev[right]:
        print("NOt a Palindorme")
        break
    left+=1
    right-=1
else:
    print("Palindrome")

'''Approach 2: Two Pointers (Without Extra Space) ⭐ Best Approach
Concept: Two Pointers + Character Skipping'''

s="A man, a plan, a canal: Panama"
left=0
right=len(s)-1
while left<right:
    while left<right and not s[left].isalnum():
        left+=1
    while left<right and not s[right].isalnum():
        right-=1
    if s[left].lower() != s[right].lower():
        print('Not a Palindrome')
        break
    left+=1
    right-=1
else:
    print("Palindrome")

name=[0,0,1,1,1,2,2,3,3,4]
n=len(name)
left=0
right=n
while left<right:
    if name[0:right].count(name[left])>1:
        name.append(name[left])
        name.remove(name[left])
        left+=1
        right-=1
    left+=1
# print(name)


def removeDuplicates(nums):
        new_dict={}
        for i in nums:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        count=0
        print(new_dict)
        for i in new_dict:
            print(new_dict[i])
            if  new_dict[i]==1 or new_dict[i]<2:
                count+=1
        return count
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

def plusOne(digits):
    val=0
    for i in digits:
        val=val*10+i
    val+=1
    print(val)
    arr=list(map(int,str(val)))
    return arr
print(plusOne([1,2,3,4]))