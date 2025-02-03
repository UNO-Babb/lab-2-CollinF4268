#Magic8Ball.py
#Name: Collin Frederick
#Date: 2/02/2025
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
]

  #Answer question randomly with one of the options from your earlier list.
def magic_8_ball():
    input("Ask the Magic 8 Ball a question: ")  # User asks a question
    response = random.choice(answers)  # Randomly select a response
    print("\nMagic 8 Ball says:", response)  # Display the response

while True:
    magic_8_ball()  # Call the Magic 8 Ball function
    play_again = input("\nDo you want to ask another question? (yes/no): ").strip().lower()
    if play_again != "yes":  # Exit if the user doesn't want to continue
        print("Thanks for playing! Goodbye!")
        break

if __name__ == '__main__':
  main()
