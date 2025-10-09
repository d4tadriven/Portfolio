import time

Dictionary = {
    "Hi": "Hello", 
    "Bye": "Goodbye"
}

def addWord(word, meaning):
    Dictionary[word] = meaning

def searchWord(word):
    return Dictionary.get(word, "Error code 001(Word doesn't exist). Try again later.")

def removeWord(word):
    if word in Dictionary:
        del Dictionary[word]
        return "Succesfully removed: "
    else:
        return "Word isn't in the dictionary"
    
def getType():
    while True:
        temp = input("What do you want to do? (Add, Search, Remove, Total) ")
        if temp in ["Add", "Search", "Remove", "Total"]:
            return temp
        print("Type isn't valid")

def getWord(type):
    temp = input(f"Which word do you want to {type}? ")
    return temp

def getMeaning():
    temp = input("What meaning do you want that word to give? ")
    return temp

    
while True:
    type = getType()

    if type == "Add":
        word = getWord(type)
        meaning = getMeaning()
        addWord(word, meaning)
    elif type == "Search":
        word = getWord(type)
        result = searchWord(word)
        print(f"Result: {result}")
        time.sleep(2)
    elif type == "Remove":
        word = getWord(type)
        meaning = searchWord(word)
        removeWord(word)
        print(f"Succesfully removed the word: {word} with the meaning: {meaning}")
    elif type == "Total":
        print(Dictionary)