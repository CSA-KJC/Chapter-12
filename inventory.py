#Katie Chiu
#Computer Programming 12th
#February 28, 2018

inventory={"pears":36,"blueberries":19,"peaches":38,"oranges":83}
print(inventory)

def invent(inventory):
    amount=input("What item do you need to change: ") #Asks user for input
    remove=input("How many to remove: ")
    for x in inventory: #Runs through each value
        if x==amount: #Finds value
            inventory[amount]=inventory[amount]-int(remove) #Removes amount wanted
            print("You now have "+str(inventory[amount])+" "+str(amount)) #Prints new value
            
invent(inventory)
