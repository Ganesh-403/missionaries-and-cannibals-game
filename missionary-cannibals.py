class MissionariesCannibalsGame:
    def __init__(self, total_missionaries=3, total_cannibals=3):
        self.total_missionaries = total_missionaries
        self.total_cannibals = total_cannibals
        self.left_missionaries = total_missionaries
        self.left_cannibals = total_cannibals
        self.right_missionaries = 0
        self.right_cannibals = 0
        self.boat = "left"

    def is_valid_state(self, missionaries, cannibals):
        """Check if missionaries are safe from being eaten."""
        return missionaries == 0 or missionaries >= cannibals

    def move(self, missionaries, cannibals):
        """Process a move if valid; otherwise, prompt user again."""
        if 1 <= missionaries + cannibals <= 2:
            if self.boat == "left":
                if missionaries <= self.left_missionaries and cannibals <= self.left_cannibals:
                    self.left_missionaries -= missionaries
                    self.left_cannibals -= cannibals
                    self.right_missionaries += missionaries
                    self.right_cannibals += cannibals
                    self.boat = "right"
                else:
                    print("🚨 Invalid move! Not enough people on the left side.")
                    return False
            else:
                if missionaries <= self.right_missionaries and cannibals <= self.right_cannibals:
                    self.right_missionaries -= missionaries
                    self.right_cannibals -= cannibals
                    self.left_missionaries += missionaries
                    self.left_cannibals += cannibals
                    self.boat = "left"
                else:
                    print("🚨 Invalid move! Not enough people on the right side.")
                    return False

            # Check if any side has unsafe conditions
            if (self.left_missionaries > 0 and self.left_missionaries < self.left_cannibals) or \
               (self.right_missionaries > 0 and self.right_missionaries < self.right_cannibals):
                print("\n💀 Oh no! The cannibals ate the missionaries. GAME OVER! 💀\n")
                return "lost"

            return True
        print("🚨 Invalid move! You can only move 1 or 2 people at a time.")
        return False

    def has_won(self):
        """Check if the game is won."""
        return self.right_missionaries == self.total_missionaries and self.right_cannibals == self.total_cannibals

    def play(self):
        """Main game loop."""
        print("\n🎮 Welcome to the Missionaries and Cannibals Game!")
        print("Move all missionaries and cannibals to the right side without getting them eaten.")
        print("💡 Type 'q' at any time to quit.\n")

        while not self.has_won():
            print(f"\n🌍 Left side -> Missionaries: {self.left_missionaries}, Cannibals: {self.left_cannibals}")
            print(f"🏝️ Right side -> Missionaries: {self.right_missionaries}, Cannibals: {self.right_cannibals}")
            print(f"🚤 Boat is on the {'LEFT' if self.boat == 'left' else 'RIGHT'} side.")

            try:
                missionaries_input = input("👤 Enter number of missionaries to move (or 'q' to quit): ").strip()
                if missionaries_input.lower() == 'q':
                    print("\n🚪 You quit the game. See you next time! 👋")
                    return
                
                cannibals_input = input("🦴 Enter number of cannibals to move (or 'q' to quit): ").strip()
                if cannibals_input.lower() == 'q':
                    print("\n🚪 You quit the game. See you next time! 👋")
                    return

                missionaries = int(missionaries_input)
                cannibals = int(cannibals_input)

                result = self.move(missionaries, cannibals)
                if result == "lost":
                    print("\n🔄 Restart the game to try again!")
                    return
            except ValueError:
                print("🚨 Invalid input! Please enter numbers only.")

        print("\n🎉 Congratulations! You successfully moved everyone across safely. 🎉")

if __name__ == "__main__":
    game = MissionariesCannibalsGame()
    game.play()
