a= "Gubba  Kalyani"
print(a)
print(len(a))                             #length of string
print(a[0])                               #first character of a string
print(a[-1])                              #last character of a string
print(a[:5])                              #first 5 characters
print(a.upper())                          #uppercase convertion
print(a.lower())                          #lowercase covertion
print(a.replace("Kalyani","Laxmi"))       #replace a word
print(a.strip())                          #remove whitespaces  
print(a[::-1])                            #reverse a string 

print(a.count("a"))                       #count "a"
print(a.split())                          #split

fn="Kalyani"
ln="Gubba"
fullname= fn + " " + ln
print(fullname)

a= "I am learning Python"                   #word is present or not
if "Python" in a:
    print("Python is present")
else:
    print("python is not present") 

words = ["Python", "is", "easy"]             #join list of words
sentence= " ".join(words)
print(sentence)  

text = "Python is easy to learn"             #count the no.of words
words= text.split()
print(len(words)) 

print(text.startswith("Hello"))              #startswith()
print(text.endswith("learn"))                #endswith()

a = "Python"
print(text.find("t"))                        #find position of a character 

text="madam"                                 #palindrome
reverse= text[::-1]
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

txt= "education"                              #count vowels
count=0
for char in txt:
    if char in "aeiou":
        count+=1
print("Vowels:", count)

txt1= "Python"                                 #count vowels and consonants
vowels=0
consonants=0
for char in txt1:
    if char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
print("vowels:", vowels)
print("consonants:", consonants) 

txt2="hello"                                 #count frequency of each char
for char in txt2:
    print(char, "=", txt2.count(char))

text1= "programming"                         #remove duplicates
result= ""
for char in text1:
    if char not in result:
        result += char
print(result) 

text2= "Python is very powerfull"            #largest word
words=text2.split()
largest= ""
for word in words:
    if len(word) > len(largest):
        largest = word
print("Largest word:", largest)
