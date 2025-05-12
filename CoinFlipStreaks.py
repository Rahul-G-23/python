import random

def coin_flip_streaks(num_flips):
    flips = []
    for _ in range(num_flips):
        if random.randint(0, 1) == 0:
            flips.append('T')
        else:  
            flips.append('H')

    print("List of flips:", ' '.join(flips))

    streak_count = 0
    for i in range(len(flips) - 5):  
        if (flips[i] == flips[i+1] == flips[i+2] == flips[i+3] == flips[i+4] == flips[i+5]):
            streak_count += 1

    return streak_count

if __name__ == "__main__":
    number_of_flips = 6
    streaks = coin_flip_streaks(number_of_flips)
    print(f"\nNumber of flips: {number_of_flips}")
    print(f"Number of streaks of 6 consecutive heads or tails: {streaks}")
    num_simulations = 10
    total_streaks = 0
    for i in range(num_simulations):
        streaks = coin_flip_streaks(number_of_flips)
        total_streaks += streaks
        print(f"Simulation {i+1}: Streaks found = {streaks}")

    average_streaks = total_streaks / num_simulations
    print(f"\nAverage number of streaks over {num_simulations} simulations: {average_streaks:.2f}")
