import random

def gamble(stake, goal, N):
    wins = 0
    bets = 0
    for i in range(N):
        while stake>0 and stake<goal:
            if random.random() < 0.5:
                stake += 1
            else:
                stake -= 1
            bets += 1
        if stake >= goal:
            wins += 1
        stake = 100
    return wins, bets

def main():
    stake = int(input("Enter the initial stake: "))
    goal = int(input("Enter the goal: "))
    N = int(input("Enter the number of times to run the experiment: "))
    
    wins, bets = gamble(stake, goal, N)
    win_percentage = wins/N*100
    loss_percentage = 100 - win_percentage
    print(f"Number of wins: {wins}")
    print(f"Win percentage: {win_percentage}%")
    print(f"Loss percentage: {loss_percentage}%")
    
if __name__ == "__main__":
    main()
    