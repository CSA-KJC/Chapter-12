#Katie Chiu
#Computer Programming 12th
#March 6, 2018
num=0
word=""

def words(num,word):
    files=open("alice.txt","r")
    new=files.readlines()
    for y in new:
        z=y.split()
        for x in z:
            count=len(x)
            if count>num:
                num=count
                word=x
    print(num)
    print(word)
                       
    files.close()

words(num,word)
