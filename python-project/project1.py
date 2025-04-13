def quiz():
    print("welcome to the quiz game")

    questions = [
        {
            "question": "Which city is the capital of Georgia?",
            "options": {
                "A": "Rustavi",
                "B": "Tbilisi",
                "C": "Qutaisi",
                "D": "Telavi"
            },
            "correct": "B"
        },
        {
            "question": "Which year did Georgia declare independence?",
            "options": {
                "A": "1991",
                "B": "1992",
                "C": "2001",
                "D": "2012"
            },
            "correct": "A"
        },
        {
            "question": "What's the official motto of Georgia?",
            "options": {
                "A": "Strength is in unity",
                "B": "Freedom",
                "C": "For Georgia",
                "D": "Georgia Forever"
            },
            "correct": "A"
        },
        {
            "question": "What is the Georgian currency called?",
            "options": {
                "A": "Euro",
                "B": "Dime",
                "C": "Lari",
                "D": "Leri"
            },
            "correct": "C"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for key, value in q["options"].items():
            print(f"{key}: {value}")

        answer = input("Your answer (A/B/C/D): ")

        if answer == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['correct']}")

    print(f"You scored {score} out of {len(questions)}")
    if score == len(questions):
        print("Amazing, all correct!")
    elif score >= len(questions) / 2:
        print("Good work!")
    else:
        print("You failed, try again!")


quiz()