import random
from datetime import datetime

# Function to display the game board
def display_board(human_pos, computer_pos):
    board = [" "] * 20
    board[6] = "O"
    board[13] = "O"
    
    if human_pos > 0:
        board[human_pos - 1] = "X"
    if computer_pos > 0:
        board[computer_pos - 1] = "X"
    
    print(" ".join([f"{i+1:2}" for i in range(20)]))
    print(" ".join(board))
    print("--------------------")

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to log game session
def log_session(session_data):
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
    filename = f"{timestamp}.txt"
    with open(filename, "w") as file:
        file.write("\n".join(session_data))
    print(f"Game session saved as {filename}")

# Main game function
def play_game():
    human_pos = 0
    computer_pos = 0
    session_data = []
    
    human_started = False
    computer_started = False
    total_human_moves = 0
    total_computer_moves = 0

    print("Starting 20x2 Dice Game!")
    
    while True:
        display_board(human_pos, computer_pos)

        # Human turn
        dice = roll_dice()
        session_data.append(f"Human rolled: {dice}")
        print(f"Human rolled: {dice}")
        
        if not human_started:
            if dice == 6:
                human_started = True
                print("Human started the game!")
            else:
                continue
        
        human_moves = dice // 2
        human_pos += human_moves
        total_human_moves += human_moves

        if human_pos == 7 or human_pos == 14:
            print("Human hit a black hole! Back to start.")
            session_data.append("Human hit a black hole! Back to start.")
            human_pos = 0
        elif human_pos >= 20:
            print("Human wins!")
            session_data.append("Human wins!")
            break

        # Computer turn
        dice = roll_dice()
        session_data.append(f"Computer rolled: {dice}")
        print(f"Computer rolled: {dice}")
        
        if not computer_started:
            if dice == 6:
                computer_started = True
                print("Computer started the game!")
            else:
                continue
        
        computer_moves = dice // 2
        computer_pos += computer_moves
        total_computer_moves += computer_moves

        if computer_pos == 7 or computer_pos == 14:
            print("Computer hit a black hole! Back to start.")
            session_data.append("Computer hit a black hole! Back to start.")
            computer_pos = 0
        elif computer_pos >= 20:
            print("Computer wins!")
            session_data.append("Computer wins!")
            break

    session_data.append(f"Total human moves: {total_human_moves}")
    session_data.append(f"Total computer moves: {total_computer_moves}")
    log_session(session_data)

if __name__ == "__main__":
    play_game()
