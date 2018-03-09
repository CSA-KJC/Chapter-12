#Katie Chiu
#Computer Programming 12th
#March 5, 2018

word=input("Which word would you like to use: ") #asks user for input

def count(word):
    num={}
    for y in word: #runs through each letter
        letter=word.count(y) #counts the number of specific letters
        num.update({y:letter}) #adds it to dictionary
    print(num)

count(word)
