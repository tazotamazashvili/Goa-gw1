import random
import pyfiglet
from colorama import Fore, Style, init



init(autoreset=True)

def print_welcome_message():
    
    
    ascii_banner = pyfiglet.figlet_format("Welcome to the Quiz Game!")
    
    print(Fore.MAGENTA + ascii_banner)
    

print_welcome_message()

    
    
    
    


def quiz():
    
    print(Fore.GREEN + Style.BRIGHT + "lets get started! the quiz has 4 questions. good luck!")
    print(Fore.YELLOW + "-"*40)


    questions = [
        {"q": "which city is the capital of Georgia?", "opts": {"A": "Rustavi", "B": "Tbilisi", "C": "Qutaisi", "D": "Telavi"}, "ans": "B"},
        {"q": "which year did Georgia declare independence?", "opts": {"A": "1991", "B": "1992", "C": "2001", "D": "2012"}, "ans": "A"},
        {"q": "whats the official motto of Georgia?", "opts": {"A": "Strength is in unity", "B": "Freedom", "C": "For Georgia", "D": "Georgia Forever"}, "ans": "A"},
        {"q": "whats the Georgian currency called?", "opts": {"A": "Euro", "B": "Dime", "C": "Lari", "D": "Leri"}, "ans": "C"}
    ]
    

    random.shuffle(questions)

    score = 0


    for q in questions:
        print(Fore.CYAN + "\n" + q["q"])
        print(Fore.YELLOW + "-" * len(q["q"]) + "\n")
        for key, val in q["opts"].items():
            print(f"{Fore.MAGENTA}{key}: {val}")
            
        
        answer = input(Fore.YELLOW + "ur answer (A/B/C/D): ").strip().upper()
        
        

        if answer == q["ans"]:
            print(Fore.GREEN + "correct!" + Style.BRIGHT)
            score += 1
        else:
            print(Fore.RED + f"wrong. correct answer is {q['ans']}." + Style.NORMAL)
            
            
            
            
            

    print(Fore.YELLOW + "-"*40)
    print(f"\n{Fore.CYAN}you scored {score}/{len(questions)}.")
    
    

    if score == len(questions):
        print(Fore.GREEN + "u got all the questions right great job! :)")
    elif score >= len(questions) / 2:
        print(Fore.GREEN + "u did a pretty good job!")
    else:
        print(Fore.RED + "u failed.")

    print(Fore.YELLOW + "-"*40)
    
    
    

quiz()