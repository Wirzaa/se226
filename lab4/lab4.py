userAmount = int(input("Enter number of users: "))
Dict = {}
for i in range(userAmount):
    items = []
    uName = input("Enter username: ")
    print("How many items?")
    iAmount = int(input())
    for j in range(iAmount):
        print("item" , j+1, ":")
        temp = input()
        items.append(temp)

    Dict[uName] = items
    print("\n")
print("USER DATA: \n")

for user, item_list in Dict.items():
    print(user, "-->", item_list)

#Common items
itemCounts = {}

for user, item_list in Dict.items():

        for item in set(item_list):
             current_amount = itemCounts.get(item, 0)
             itemCounts.update({item: current_amount + 1})

print("COMMON ITEMS:")

for item, amount in itemCounts.items():
    if amount > 1:
        print(item)

print("UNIQUE ITEMS:")

for item, amount in itemCounts.items():
     if amount == 1:
        print(item)

print("MOST COMMON ITEM: ")
if itemCounts:
    mostCommonAmount = max(itemCounts.values())

    for item, amount in itemCounts.items():
        if amount == mostCommonAmount:
            print(item)
