# ====================== NUmber Guessing Game ======================
import random

print("""
      =======================================================================
                    🎉 Welcome to the Number Guessing Game! 🎉
      =======================================================================
    """)

print(""" 🔰 Rules: 
      1. You have to guess a number between 1 and 100. 
      2. You have 10 attempts to guess the correct number. 
      3. After each guess, you will receive feedback whether your guess is too low, too high, or correct. 
      4. If you guess the correct number within 10 attempts, you win! Otherwise, you lose.
""")

secrete_number = random.randint(1, 100)
attempts = 10

while True:
    try:
        guess = int(input("\n🤷 Guess the number (between 1 and 100): "))
        attempts -= 1
        
        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
            continue
        
        if guess < secrete_number:
            print("📉 Too low! Try again.")
        elif guess > secrete_number:
            print("📈 Too high! Try again.")
        else:            
            print(f"\n✅ Congratulations! You've guessed the correct number {secrete_number} in {10 - attempts} attempts!")
            break
        
        if attempts == 0:
            print(f"\n❌ Game Over! You've used all your attempts. The correct number was {secrete_number}.")
            break
        
    except ValueError:
        print("\n🚨 You Enter a Invalid Input.")
    
    