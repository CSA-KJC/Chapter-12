#Katie Chiu
#Computer Programming 12th
#March 5, 2018

word=input("Which word would you like to use: ")

def count(word):
    num={}
    for y in word:
        letter=word.count(y)
        num.update({y:letter})
    print(num)

count(word)
