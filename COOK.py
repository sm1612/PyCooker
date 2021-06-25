import random
def cooker():
    combination_list = ["Mix","Fry","Curry","Roast","Grilled","Baked","Boiled","steamed"]
    randomnumitem = random.randrange(0,len(items_list))
    randomnumcombi = random.randrange(0,len(combination_list))
    dish = items_list[randomnumitem]+ "  "+ combination_list[randomnumcombi]
    print("You can make this dish today. Enjoy Cooking", dish)
def about():
    print("THIS FUN LITTLE PROGRAM HELPS TO DECIDE WHAT MENU CAN BE SERVED ON YOUR DINNER TABLE. SIMPLY ENTER ALL THE FOOD ITEMS YOU ARE HAVING IN YOUR HOUSE, AND LET THIS PROGRAM DO THE REST OF THE WORK")

#MAIN
print("WELCOME TO THE VIRTUAL COOK. I AM YOUR HELPING HAND IN DECIDING WHAT MENU WILL BE PLACED ON YOUR DINNER TABLE.")
about()
items_list = []
n = int(input("Enter number of Food items you have in your house : "))
for i in range(0, n):
    ele = input()
    items_list.append(ele)  # adding the element
combination_list = ["Mix","Fry","Curry","Roast","Grilled","Baked","Boiled","steamed"]
cooker()
while True:
    cont=int(input("Do you Wish to Continue? Press 1 for Yes and 2 for No"))
    if cont == 1:
        cooker()
    else:
        break

