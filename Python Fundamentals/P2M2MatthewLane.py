#P2M2MatthewLane
zoo = ["Gorilla", "Lion", "Tiger", "Elephant"]
 
def list_o_matic(animal):
    if animal == "":
        animal = zoo.pop()
        print(animal + " has been popped from the list")
    elif animal in zoo:
        zoo.remove(animal)
        print("One instance of " + animal + " removed from list")
    else:
        zoo.append(animal)
        print("One instance of " + animal + " appended from list")
 
while True:
    if zoo == "":
        break
    else:
        animal_name = input("enter the name of a zoo animal or \"q\" to quit: ")
        if animal_name.lower().startswith("q"):
            break
        else:
            list_o_matic(animal_name)
            print(zoo)
 
print("Farewell!")    