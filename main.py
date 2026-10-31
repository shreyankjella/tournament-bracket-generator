"""Run a small single-elimination tournament, including byes."""
import random

def first_round(names, seed=None):
    names = names[:]
    random.Random(seed).shuffle(names)
    size = 1
    while size < len(names):
        size *= 2
    # Pair each extra bye with a player, instead of pairing byes together.
    byes = size - len(names)
    matches = [(name, None) for name in names[:byes]]
    remaining = names[byes:]
    matches += [(remaining[i], remaining[i + 1]) for i in range(0, len(remaining), 2)]
    return matches

def play_round(matches):
    advancing = []
    for number, (a, b) in enumerate(matches, 1):
        if b is None:
            print(f"Match {number}: {a} advances (bye)")
            advancing.append(a)
            continue
        while True:
            winner = input(f"Match {number}: {a} vs {b}. Winner: ").strip()
            if winner in (a, b):
                advancing.append(winner)
                break
            print("Type one of the two names exactly.")
    return advancing

def main():
    print("Tournament Bracket Generator")
    names = [n.strip() for n in input("Player names (comma-separated): ").split(",") if n.strip()]
    if len(names) < 2 or len(set(n.lower() for n in names)) != len(names):
        print("Enter at least two players with different names.")
        return
    matches = first_round(names)
    round_number = 1
    while True:
        print(f"\nRound {round_number}")
        advancing = play_round(matches)
        if len(advancing) == 1:
            print(f"\nChampion: {advancing[0]}!")
            break
        matches = [(advancing[i], advancing[i + 1]) for i in range(0, len(advancing), 2)]
        round_number += 1

if __name__ == "__main__":
    main()
