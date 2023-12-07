import random
def play_game():
	n= int(input("Enter how many rounda you want to play:"))
	user_score = 0
	computer_score = 0
	for i in range(n):
		user_choice = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
		while user_choice not in ['r','p','s']:
			user_choice = input("Invalid choice. Please enter 'r' for rock, 'p' for paper, 's' for scissors\n")
		computer_choice = random.choice(['r', 'p', 's'])
		if user_choice == computer_choice:
			print("It's a tie!")
		elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
			print("You win!")
			user_score += 1
		else:
			print("You lose!")
			computer_score += 1
	print(f"Your score: {user_score}  Computer score: {computer_score}\n")
	if user_score > computer_score:
		print("You win the game!")
	elif user_score == computer_score:
		print("It's a tie!")
	else:
		print("You lose the game!")
	print("Game over!")


play_game()
