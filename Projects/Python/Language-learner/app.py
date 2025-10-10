
import random

words = [
    {"French": "le", "Dutch": "de / het", "English": "the", "Spanish": "el", "German": "der / die / das"},
    {"French": "la", "Dutch": "de", "English": "the", "Spanish": "la", "German": "die"},
    {"French": "un", "Dutch": "een", "English": "a / one", "Spanish": "un", "German": "ein"},
    {"French": "une", "Dutch": "een", "English": "a / one", "Spanish": "una", "German": "eine"},
    {"French": "et", "Dutch": "en", "English": "and", "Spanish": "y", "German": "und"},
    {"French": "ou", "Dutch": "of", "English": "or", "Spanish": "o", "German": "oder"},
    {"French": "bonjour", "Dutch": "hallo", "English": "hello", "Spanish": "hola", "German": "hallo"},
    {"French": "merci", "Dutch": "dank je", "English": "thank you", "Spanish": "gracias", "German": "danke"},
    {"French": "au revoir", "Dutch": "tot ziens", "English": "goodbye", "Spanish": "adiós", "German": "auf Wiedersehen"},
    {"French": "s'il vous plaît", "Dutch": "alstublieft", "English": "please", "Spanish": "por favor", "German": "bitte"},
    {"French": "pardon", "Dutch": "sorry", "English": "sorry / excuse me", "Spanish": "perdón", "German": "entschuldigung"},
    {"French": "oui", "Dutch": "ja", "English": "yes", "Spanish": "sí", "German": "ja"},
    {"French": "non", "Dutch": "nee", "English": "no", "Spanish": "no", "German": "nein"},
    {"French": "homme", "Dutch": "man", "English": "man", "Spanish": "hombre", "German": "Mann"},
    {"French": "femme", "Dutch": "vrouw", "English": "woman", "Spanish": "mujer", "German": "Frau"},
    {"French": "enfant", "Dutch": "kind", "English": "child", "Spanish": "niño / niña", "German": "Kind"},
    {"French": "maison", "Dutch": "huis", "English": "house", "Spanish": "casa", "German": "Haus"},
    {"French": "chien", "Dutch": "hond", "English": "dog", "Spanish": "perro", "German": "Hund"},
    {"French": "chat", "Dutch": "kat", "English": "cat", "Spanish": "gato", "German": "Katze"},
    {"French": "eau", "Dutch": "water", "English": "water", "Spanish": "agua", "German": "Wasser"}
]
supportedLanguages = [
    "Dutch",
    "French",
    "English",
    "Spanish",
    "German"
]
learningTypes = [
    {"number": 1,
    "name": "Test",
    "description": "Gives you the word in your own language and makes you translate it"
    },
    #{
    #"number": 2,
    #"name": "First Letter Hint",
    #"description": "Shows you the first letter of the translation to help you recall the full word"
    #}
]

def checkSupportedLanguages(chosenLanguage):
    for language in supportedLanguages:
        if chosenLanguage == language:
            return True
    return False

def checkLearningType(chosenType):
    for type in learningTypes:
        if chosenType == str(type["number"]):
            return True
    return False

def startQuiz(learningLanguage, mainLanguage, learningType):
    quizPoints = 0
    print(f"You just chose {learningLanguage} and your own language is {mainLanguage}!\nGood luck!")
    availableWords = [word for word in words if learningLanguage in word and mainLanguage in word]
    if learningType == 1:
        while True:
            chosenWord = random.choice(availableWords)
            learningLanguageWord = chosenWord[learningLanguage]
            print(f"\nWhat is the {learningLanguage} translation for '{chosenWord[mainLanguage]}'?")
            answer = input("Your answer: ").lower()
            if answer == "exit":
                return quizPoints
            elif answer == learningLanguageWord:
                print("Correct")
                quizPoints += 1
            else:
                print(f"Wrong! The right answer was '{learningLanguageWord}'")
    #elif learningType == 2:

def main():
    points = 0
    quizPlaying = False
    while quizPlaying == False:
        print(f"Welcome to Styn language learning app\nYou currently have {str(points)} points!")
        supported = False
        print("Choose one of the following languages you want to learn\n")
        for language in supportedLanguages:
            print(language)
        while supported == False:
            learningLanguage = input("\nYour answer: ")
            if checkSupportedLanguages(learningLanguage) == False:
                print("Please select a different language")
            else:
                supported = True
        supported = False
        print("Choose your own language\n")
        for language in supportedLanguages:
            print(language)
        while supported == False:
            mainLanguage = input("\nSelect your own language: ")
            if checkSupportedLanguages(mainLanguage) == False:
                print("Please select a different language")
            else:
                supported = True
        print("Select the way you want to learn.\n")
        for type in learningTypes:
            print(f"({type["number"]}) - {type["name"]} - {type["description"]}")
        supported = False
        while supported == False:
            chosenType = input("\nSelect your learning type (1/2/3): ")
            if checkLearningType(chosenType) == False:
                print("Please select a different type. Only type the number Eg. 2")
            else:
                supported = True
        points += startQuiz(learningLanguage, mainLanguage, int(chosenType))

if __name__ == "__main__":
    main()