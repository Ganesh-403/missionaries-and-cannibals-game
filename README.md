# Missionaries and Cannibals Game  

Move all missionaries and cannibals across the river without getting them eaten.  

# How to Play  
- Your goal is to move all missionaries and cannibals from the left side to the right side using a boat.  
- Rules:  
  - The boat can only carry 1 or 2 people at a time.  
  - At no point should cannibals outnumber missionaries on either side, or they will eat them.  
  - You can quit anytime by entering `"q"` instead of a number.  

# Game Controls  
1. Enter the number of missionaries you want to move.  
2. Enter the number of cannibals you want to move.  
3. The boat will move automatically if the move is valid.  
4. If an invalid move is made, the game will warn you and let you try again.  

# Win & Lose Conditions  
- **Win:** Move all missionaries and cannibals safely across the river.  
- **Lose:** If cannibals outnumber missionaries on either side, you lose.  

# Example Gameplay  

```
Welcome to the Missionaries and Cannibals Game!  
Move all missionaries and cannibals to the right side without getting them eaten.  
Type 'q' at any time to quit.  

Left side -> Missionaries: 3, Cannibals: 3  
Right side -> Missionaries: 0, Cannibals: 0  
Boat is on the LEFT side.  

Enter number of missionaries to move (or 'q' to quit): 1  
Enter number of cannibals to move (or 'q' to quit): 1  

The boat moves to the right side...  

Left side -> Missionaries: 2, Cannibals: 2  
Right side -> Missionaries: 1, Cannibals: 1  
Boat is on the RIGHT side.  

Enter number of missionaries to move (or 'q' to quit): 0  
Enter number of cannibals to move (or 'q' to quit): 2  

Oh no! The cannibals ate the missionaries. GAME OVER!  
Restart the game to try again.  
```

# How to Run  
1. Install **Python 3** if you haven’t already.  
2. Save the script as `game.py`.  
3. Open a terminal and run:  
   ```
   python game.py
   ```  

# Features  
- Interactive gameplay – You decide every move.  
- Smart input handling – No crashes from bad inputs.  
- Lose condition detection – Cannibals eating missionaries ends the game.  
- Quit anytime – Just type `"q"` to exit.  
- Clear messages – You always know what's happening.  

Can you solve the puzzle and get everyone across safely?  

