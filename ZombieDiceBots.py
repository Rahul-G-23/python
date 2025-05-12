
import random

class ZombieDiceBot:

    def __init__(self, name):
        self.name = name

    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        raise NotImplementedError("Subclasses must implement the should_roll method.")

    def __str__(self):
        return self.name

class BasicBot(ZombieDiceBot):
    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        return brain_count < 1

class RiskyBot(ZombieDiceBot):
    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        return shotguns_count < 3

class CautiousBot(ZombieDiceBot):
    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        return brain_count < 2

class RandomBot(ZombieDiceBot):
    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        return random.choice([True, False])

class BrainGreedyBot(ZombieDiceBot):
    def should_roll(self, brain_count, shotguns_count, turn_rolls_history):
        return shotguns_count < 3

def roll_dice():
    dice_colors = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3
    rolled_dice = random.sample(dice_colors, 3)
    results = []
    for color in rolled_dice:
        if color == 'green':
            outcomes = ['brain'] * 3 + ['shotgun'] * 1 + ['runner'] * 2
        elif color == 'yellow':
            outcomes = ['brain'] * 2 + ['shotgun'] * 2 + ['runner'] * 2
        else:  # red
            outcomes = ['brain'] * 1 + ['shotgun'] * 3 + ['runner'] * 2
        results.append(random.choice(outcomes))
    return tuple(results)

def play_turn(bot):
    print(f"\n--- {bot.name}'s turn ---")
    brains_this_turn = 0
    shotguns_this_turn = 0
    turn_rolls_history = []

    while shotguns_this_turn < 3 and bot.should_roll(brains_this_turn, shotguns_this_turn, turn_rolls_history):
        input(f"{bot.name} decides to roll. Press Enter to roll...")
        roll_result = roll_dice()
        turn_rolls_history.append(roll_result)
        print(f"{bot.name} rolled: {', '.join(roll_result)}")

        for result in roll_result:
            if result == 'brain':
                brains_this_turn += 1
            elif result == 'shotgun':
                shotguns_this_turn += 1

        print(f"Brains this turn: {brains_this_turn}")
        print(f"Shotguns this turn: {shotguns_this_turn}")

        if shotguns_this_turn >= 3:
            print(f"{bot.name} got zombied out!")
            return 0  

    print(f"{bot.name} decided to stop. Total brains this turn: {brains_this_turn}")
    return brains_this_turn

def run_game(bots, num_turns=5):
    scores = {bot.name: 0 for bot in bots}

    for turn in range(1, num_turns + 1):
        for bot in bots:
            brains_earned = play_turn(bot)
            scores[bot.name] += brains_earned
            print(f"{bot.name}'s total score: {scores[bot.name]}")
        print(f"\n--- End of Turn {turn} ---")
        print("Current Scores:")
        for name, score in scores.items():
            print(f"{name}: {score}")
        break

    print("\n--- Game Over ---")
    print("Final Scores:")
    for name, score in scores.items():
        print(f"{name}: {score}")

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    bot1 = BasicBot("Basic Bot")
    bot2 = RiskyBot("Risky Bot")
    players = [bot1, bot2]
    run_game(players, num_turns=3)
