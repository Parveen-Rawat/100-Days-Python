# Rock paper scissors game
'''
import random

Rock = """         _______
               ---'   ____)
                    (_____)
                    (_____)
                     (____)
               ---.__(___)
"""
Paper = """       _______
              ---'   ____)____
                        ______)
                       _______)
                       _______)
                ---.__________)

"""
Scissors = """    _______
              ---'   ____)____
                        ______)
                    __________)
                   (____)
             ---.__(___)
"""

print("Welcome to the rock, paper , scissors game\n")

choice = int(input("What will you choose: \n type 0 for rock, 1 for paper and 2 for scissors\t"))

if choice == 0 or choice == 1 or choice == 2:
    if choice == 0:
        print(Rock)
        print("\nYou chose: Rock\n")
    elif choice == 1:
        print(Paper)
        print("\nYou chose: Paper\n")
    else:
        print(Scissors)
        print("\nYou chose : Scissors\n")
    
    
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        print(Rock)
        print("\nComputer chose : Rock\n")
    elif computer_choice == 1:
        print(Paper)
        print("\nComputer chose : Paper\n")
    else: 
        print(Scissors)
        print("\nComputer chose : Scissors\n")
        
    
    if choice == computer_choice:
        print("It's a draw")
    elif choice == 0 and computer_choice == 1 :
        print("You lost")
    elif choice == 0 and computer_choice == 2:
        print("You won")
    elif choice == 1 and computer_choice == 0:
        print("You won")
    elif choice == 1 and computer_choice == 2:
        print("You lost")
    elif choice == 2 and computer_choice == 0:
        print("You lost")
    elif choice == 2 and computer_choice == 1:
        print("You lost")
    else:
        print("Invalid format occur")
        
    '''
    
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the password generator\n")
number_of_letters = int(input("How many letters you want in your password\n"))
number_of_symbols = int(input("How many symbols you want in your password\n"))
number_of_numbers = int(input("How many numbers you want\n"))

password = ""
for char in range(0,number_of_letters):
    password += random.choice(letters)
    
for char in range(0,number_of_symbols):
    password += random.choice(symbols)
    
for char in range(0,number_of_numbers):
    password += random.choice(numbers)
    
print(password)


password2 = []

for char in range(0,number_of_letters):
    password2.append(random.choice(letters))
    
for char in range(0,number_of_numbers):
    password2.append(random.choice(numbers))
    
for char in range(0,number_of_symbols):
    password2.append(random.choice(symbols))

random.shuffle(password2)

print(f"Your generated passsword is : {''.join(password2)}\n")
