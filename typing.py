# Author Tanner Mesaric
import random
import string

def get_scores():
    scores = []
    with open("Assignments/assignment21/scores.txt") as file:
        lines = file.readlines()
        for line in file:
            scores.append(line)
        return scores

def save_scores(score): 
    with open("Assignments/assignment21/scores.txt", "w") as file:
        file.write(f"{score}")


def display_scores(scores):
    for i in range(len(scores)):
        print(f"game {i+1}. {scores[i]}/10")


def play_round():
    questions = 0
    score = 0
    for i in range(10):
        randLetter = random.choice(string.ascii_letters)
        userAnswer = input(f"{randLetter}: ").strip()
        if userAnswer == randLetter:
                questions += 1
                score += 1
                if questions == 10:
                    print(f"You won this round!")
                    break
        else:
                print(f"you got {score} letters correct.")
                break
    return score


print("Let's learn to type!")
score = get_scores()
while True:
    game = input("(P)lay or (Q)uit: ").lower().strip()
    if game == "p":
        pRound = play_round()
        score.append(pRound)
        save_scores(score)
    elif game == "q":
        display_scores(score)
        print("Goodbye!")
        break
    else:
        print("Invalid Command")