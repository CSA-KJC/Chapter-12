#Katie Chiu
#Computer Programming 12th
#March 6, 2018
num=0
word=""

def words(num,word):
    files=open("alice.txt","r") #opens file
    new=files.readlines()
    for y in new: #runs through the file
        z=y.split() #splits into word
        for x in z: #Runs through each word
            count=len(x) #Counts amount of letters
            if count>num: #updates original amount to new one if new word it is longer
                num=count
                word=x
    print(num)
    print(word)
                       
    files.close()

words(num,word)
