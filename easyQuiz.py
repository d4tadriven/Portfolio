
questions = [
    {
        "prompt": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "prompt": "What color do you get when you mix blue and yellow?",
        "options": ["A. Green", "B. Purple", "C. Orange", "D. Brown"],
        "answer": "A"
    },
    {
        "prompt": "Which animal is known as the King of the Jungle?",
        "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Leopard"],
        "answer": "C"
    },
    {
        "prompt": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "prompt": "What gas do humans breathe in to survive?",
        "options": ["A. Carbon Dioxide", "B. Nitrogen", "C. Oxygen", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "prompt": "Which shape has three sides?",
        "options": ["A. Square", "B. Circle", "C. Triangle", "D. Rectangle"],
        "answer": "C"
    },
    {
        "prompt": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "prompt": "What is the capital of Italy?",
        "options": ["A. Rome", "B. Paris", "C. Madrid", "D. Berlin"],
        "answer": "A"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            score += 1
            if score != 1:
                print("You're right! "+question["answer"]+" was indeed the right answer!\nYou now have "+str(score)+" points!\n")
            else:
                print("You're right! "+question["answer"]+" was indeed the right answer!\nYou now have "+str(score)+" point!\n")
        else:
            print("WRONG! You idiot. The right answer is "+question["answer"]+"\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)