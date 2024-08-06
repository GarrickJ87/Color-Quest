import random

class ColorQuestAI:
    def __init__(self):
        self.score = 0
        self.colors = {
            "red": "the color of a ripe tomato or a stop sign",
            "green": "the color of fresh grass or a cucumber",
            "blue": "the color of a clear sky or the ocean",
            "yellow": "the color of a sunflower or a school bus",
            "purple": "the color of a violet or an eggplant",
            "orange": "the color of an orange fruit or a pumpkin",
        }
        self.items = [
            ("strawberry", "red"),
            ("grass", "green"),
            ("sky", "blue"),
            ("banana", "yellow"),
            ("grape", "purple"),
            ("pumpkin", "orange"),
        ]
        self.welcome_message()
    
    def welcome_message(self):
        print("Welcome to Color Quest!")
        print("Embark on a journey to discover and understand colors.")
        print("Are you ready to begin your adventure?\n")
        self.start_game()

    def start_game(self):
        while True:
            print("Choose an option:")
            print("1. Color Description Quiz")
            print("2. Color Association Challenge")
            print("3. Check Score")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                self.color_description_quiz()
            elif choice == "2":
                self.color_association_challenge()
            elif choice == "3":
                self.display_score()
            elif choice == "4":
                print("Thank you for playing Color Quest! See you next time!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.\n")

    def color_description_quiz(self):
        print("\nColor Description Quiz:")
        color = random.choice(list(self.colors.keys()))
        description = self.colors[color]
        print(f"Which color matches the description: {description}?")
        answer = input("Your answer: ").lower()
        
        if answer == color:
            print("Correct! You've earned a point.\n")
            self.score += 1
        else:
            print(f"Sorry, the correct answer is {color}.\n")

    def color_association_challenge(self):
        print("\nColor Association Challenge:")
        item, correct_color = random.choice(self.items)
        print(f"What color is typically associated with a {item}?")
        answer = input("Your answer: ").lower()

        if answer == correct_color:
            print("Correct! You've earned a point.\n")
            self.score += 1
        else:
            print(f"Sorry, the correct answer is {correct_color}.\n")

    def display_score(self):
        print(f"\nYour current score is: {self.score}\n")

if __name__ == "__main__":
    ColorQuestAI()
