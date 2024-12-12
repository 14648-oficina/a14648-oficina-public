import random
global result
i = 1
b = 1
c = 1
wins = 0
tryagain = "Y"
print(f"{'--------GUESS THE NUMBER--------': ^75}")
print("Do You Know How to Play?")
tutorial1 = input("Y/N: ")
tutorial2 = tutorial1.upper()

if tutorial2 != "N":
  pass
else:
  print("""Welcome to the Tutorial!
  You have 6 tries to guess a random number between 0-20.
  If you guess correctly, you win!""")
Name = input("\nType Out Your Name: ")
def RandomChoice(i,wins):
  global tryagain
  global tryagain1
  global answer
  global victorysuffix
  global wins2
  answer = 0
  while i <= 6:
    answer = int(input("Type Out Your Guess: "))
    if answer == NumberGuess:
      print("\nYou Won!")
      wins = wins + 1
      if wins == 1:
          victorysuffix = ""
      else:
          victorysuffix = "s"
      print(f"You have {wins} wins{victorysuffix}")
      print("Do You Want to Play Again")
      tryagain1 = str(input("Y/N: "))
      tryagain = tryagain1.upper()
      return wins
    else:
      i += 1
    return answer
def Guess(b):
  global tryagain
  global tryagain1
  global trynum
  trynum = 0
  while b <= 6:
    trynum2 = b
    trynum1 = 6 - trynum2
    if answer > NumberGuess:
      print(f"\nYour Answer is Higher!, you have {trynum1} tries")
      print("\n Try Again!")
      b += 1
      RandomChoice(i,wins)
    elif answer < NumberGuess:
      print(f"\nYour Answer is Lower!, you have {trynum1} tries")
      print("Try Again!")
      b += 1
      RandomChoice(i,wins)
    elif answer == NumberGuess:
      pass
      break
    if (b > 6) and answer != NumberGuess:
      print("You Lost!")
      if wins == 1:
        victorysuffix = ""
      else:
        victorysuffix = "s"
      print(f"You have {wins} win{victorysuffix}")
      print("Do you Want to Try Again")
      tryagain1 = str(input("Y/N: "))
      tryagain = tryagain1.upper()
      break

def main():
    global NumberGuess
    while True:
      if c <= 1 and tryagain == "Y":
       NumberGuess = random.randint(0,20)
       RandomChoice(i,wins)
       Guess(b)
       print(wins)
        
      elif c <= 1 and tryagain != "Y":
        asksave1 = input("Do you want to save your Score: ")
        asksave2 = asksave1.upper()
        if asksave2 == "Y":
          Saving = open("Scoreboard.txt","a")
          Saving.write(f"Name - Wins :{wins}")

if __name__ == "__main__":
    main()
    

    
