# Python-Project
Hangman Game.
# Overview -
The code is written in python language for a classic game known as Hangman Game. A word is randomly selected from a given list of words, and the player has six lives to guess the word. The code allows user to enter one letter as a guess at a time. The code shows the number of games played and the user's win score at the end of the game. After every game, user has two option to play futher or quit the game.

# Features -
1. Words gets selected randomly from a list of words.
2. Hangman gets representated for each incorrect guess.
3. Win and loss tracking with appropriate code.
4. Scoreboard detecting number of games played and wins and losses.
5. Play-again option for continuous gameplay by writing yes or no.

# Requirement -

1.Python 3.x

2. Module random

# Steps to install and run your Hangman project :
1. Install Software : Visual Studio Code, GitHub Desktop, Python 3.x Git.
2. Clone repository with gitHub desktop.
3. Open gitHub desktop and oform your gitHub account.
4. Clone your project repository to a local folder.
5. Open project in vs code.
6. In gitHub desktop, select your repository and click "Open in Visual Studio Code".
7. VS Code will load your project files.
8. In vs code, select python interpreter .
9. Install required Python module (random) using the terminal: pip install random.
10. Run the project and interact with the program.
11. Commit and push from GitHub Desktop.

# Gameplay Instructions -
1. On the initial stage, the game displays the length of the randomly chosen word and the hangman graphic.
2. Enter a letter on each turn.
3. If the letter is correct, the positions of the entered letter are revealed.
4. If the guess is wrong, the total life decreases by 1 and the hangman starts loosing its body parts.
5. The game ends when all letters are guessed or the total life becomes 0.
6. After the game, the user can choose whether to play again or quit the game.

# Examnple Screenshots -
1. Starting of the game - 
<img width="1197" height="381" alt="image" src="https://github.com/user-attachments/assets/edeea6ef-45df-4ca6-91f6-89e1a70b0ef8" />
2. In between game -
<img width="1193" height="828" alt="image" src="https://github.com/user-attachments/assets/d6e2ad8b-0172-42db-9b4c-2d8ae3042713" />
3. Ending of the game -
 <img width="1190" height="820" alt="image" src="https://github.com/user-attachments/assets/cf0bb623-6108-42bc-b9e0-0c0bdf09678b" />
 
# Scoreboard -

The scoreboard displays the number of games played and win count at the end of the gameplay.

# Design Decisions Rationale -
1. Lists for game state: Chosen for easy character replacement and state tracking.

Stages as multi-line strings: Offers simple visual feedback within text-only environments.

Modularity: Breaking the logic into clear functional blocks (input handling, state update, and rendering) simplifies maintenance.


