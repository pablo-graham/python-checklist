checklist = []

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist.pop(index)
    checklist.insert(index, item)

def destroy(index):
    checklist.pop(index)

def iterateThroughList():
    for i in range(len(checklist)):
        print(checklist[i])
    # this is another way to do it, it actually checks every element
    # for el in checklist:
    #     items.append (element)

def completed(index):
    unchecked = checklist[index]
    checklist[index] = "check " + unchecked
    return checklist[index]

def userInput(prompt):
    entry = input(prompt)
    return entry

def userChoice():
    editing = True
    while editing:
        choice = userInput("which function would you like to use? C = create, R = read, U = update, D = destroy, A to view all items, S to select an item w a check or Q to quit")
        if choice == "C":
            item = userInput("type the color and the item")
            create(item)
            continue
        elif choice == "R":
            index = userInput("which item do you want to read?")
            read(int(index))
            continue
        elif choice == "U":
            newItem = userInput("what item would you like to update")
            newIndex = userInput("where would you like tp update the item to")

            update(int(newIndex), newItem)
            continue
        elif choice == "D":
            itemToDestroy = userInput("which item number would you like to destroy")
            destroy(int(itemToDestroy))
            continue
        elif choice == "A":
            iterateThroughList()
            continue
        elif choice == "S":
            indexToItem = userInput("At what index is the item you want to check")
            completed(int(indexToItem))
            continue
        else:
            end = userInput("do you wish to stop the program? enter Y for yes or N for no")
            if end == "Y":
                print(checklist)
                editing = False
            else:
                continue

userChoice()

def test():
    create("purple sox")
    create("red cloak")
    iterateThroughList()
    

    update(0, "purple socks")
    destroy(1)

    
    iterateThroughList()
    print(completed(0))
    print(userInput("input str: "))
    userChoice()

test()
