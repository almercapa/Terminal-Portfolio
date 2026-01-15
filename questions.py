import os
import random
from colorist import Color

question_bank = [
    {
        "question": "What is my favorite Pokemon?",
        "choices": ["Chandelure", "Annihilape", "Breloom", "Mienshao"],
        "correctIndex": 2,
        "difficulty": "Medium",
        "explanation": "Also happens to be Luigi Mangione's favorite"
    },

    {
        "question": "What is my favorite snack?",
        "choices": ["Ritz", "Biscoff", "Oreo", "Cheez-Its"],
        "correctIndex": 1,
        "difficulty": "Hard",
        "explanation": "Tastes like Scooby Snacks"
    },

    {
        "question": "What is my favorite artist?",
        "choices": ["Bruno Mars", "Carti", "Tyler the Creator", "Don Toliver"],
        "correctIndex": 0,
        "difficulty": "Easy",
        "explanation": "That's What I Like"
    },

    {
        "question": "What is my favorite show?",
        "choices": ["Mob Psycho", "Bleach", "Gurren Lagann", "Jojo's"],
        "correctIndex": 0,
        "difficulty": "Medium",
        "explanation": "Sometimes it's okay to run away"
    },

    {
        "question": "What is my current split?",
        "choices": ["Bro Split", "Arnold Split", "PPL", "Upper Lower/PPL"],
        "correctIndex": 3,
        "difficulty": "Insane",
        "explanation": "I love doing legs and abs on the same day"
    }
]

def printHealthBar(name, hp):
    filled_segments = hp // 5
    empty_segments = 20 - filled_segments
    bar = "█" * filled_segments
    empty = "." * empty_segments
    print(f"\n{name}: [{Color.GREEN}{bar}{Color.OFF}{Color.RED}{empty}{Color.OFF}] {hp}/100")

play_hp = 100
maho_hp = 100
index = 0

while (maho_hp > 0 and play_hp > 0):
    os.system('cls' if os.name == 'nt' else 'clear')
    q = question_bank[index]
    print("\n" + q["question"])
    for i, choice in enumerate(q["choices"]):
        print(f"{i + 1}: {choice}")
    
    user_input = input("Enter choice index: ")

    try:
        user_input = int(user_input)
    except ValueError:
        print("Not a valid option. Please try again.\n")
        input("Press enter to start again: ")
        continue

    if (user_input - 1) == q["correctIndex"]:
        print("\nCorrect!")
        print(q["explanation"])
        damage_map = {"Easy": 5, "Medium": 10, "Hard": 15, "Insane": 25}
        flash = random.randint(1,10)
        if (flash == 10):
            print("BLACK FLASH")
            maho_hp -= (damage_map.get(q["difficulty"], 10)) * 2
        else:
            maho_hp -= damage_map.get(q["difficulty"], 10)
    else:
        print("\nIncorrect!")
        print(q["explanation"])
        play_hp -= 25
    
    if (maho_hp > 0 and play_hp > 0):
        printHealthBar("MAHORAGA", maho_hp)
        printHealthBar("PLAYER", play_hp)
    
    if (maho_hp <= 0 or play_hp <= 0):
        break

    if (index < len(question_bank) - 1):
        index += 1
    else:
        index = 0
    
    cont = input("\nType anything for the next question: ")

if (maho_hp <= 0):
    print("\nPlayer wins!")
else:
    print("\nMahoraga wins!")