import random

import time
import sys

def spinning_ball(duration=2):
    # Overlapping frames simulating surface text shifts
    frames = [
        "  (  ●  )  ",
        "  ( ●   )  ",
        "  (●    )  ",
        "  (    ●)  ",
        "  (   ● )  ",
    ]
    
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        # Overwrite the same line with the next frame
        sys.stdout.write(f"\r {frames[i % len(frames)]} Welcome to the Number Guessing Game! {frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1

spinning_ball()


def typewriter(text, speed=0.06):
    """
    Prints text character by character with a realistic delay 
    and a blinking terminal cursor effect.
    """
    # Hide the system cursor to handle our custom cursor cleanly
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    
    try:
        for char in text:
            # Erase the previous cursor block, print character, and add trailing cursor block
            sys.stdout.write(f"\b \b{char}█")
            sys.stdout.flush()
            time.sleep(speed)
            
        # Keep the cursor blinking at the end of the text for a brief moment
        for _ in range(4):
            sys.stdout.write("\b \b")  # Erase cursor
            sys.stdout.flush()
            time.sleep(0.05)
            sys.stdout.write("█")      # Draw cursor
            sys.stdout.flush()
            time.sleep(0.1)
            
        # Final clean up: erase the cursor block and add a final newline
        sys.stdout.write("\b \b\n")
        
    finally:
        # Restore the original terminal cursor if interrupted
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# Run the animation
typewriter(""""\n\nI'm thinking of a number between 1 and 100.

Please select the difficulty level: """)





print("""
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")

machine_number=random.randint(1,100)
while True:
    try:
        level=int(input("\nEnter your choice: "))
        if level in [1,2,3]:
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number.")
def game():
    if level ==1:
        chances=10
        print(f"""\nGreat! You have selected the Easy difficulty level.\n You have {chances}chances to guess the correct number.
Let's start the game!""")

    if level ==2:
        chances=5
        print(f"""\nGreat! You have selected the Medium difficulty level.\nYou have {chances} chances to guess the correct number.
Let's start the game!""")

    if level ==3:
        chances=3
        print(f"""\nGreat! You have selected the Hard difficulty level.
        \nYou have {chances} chances to guess the correct number.
\nLet's start the game!""")
    status=None
    attempts=0
    for i in range(1,chances+1):
        attempts+=1
        while True:
            try:
                guess=int(input("\nEnter your choice: "))
                if 1<=guess<=100:
                    break
                else:
                    print("Guess only between 1 to 100.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 to 100.")
        
        if guess==machine_number :
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            status=True
            break
        elif guess<machine_number:
            print(f"Incorrect! The number is greater than {guess}.")
            
            status=False
        else:
            print(f"Incorrect! The number is less than {guess}.")
            status=False
    if status==False:
        print(f"\nGame Over! You Run out of chances and the correct number was {machine_number}.")
    
game()