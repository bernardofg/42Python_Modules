import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind',
        'Hidden Path Finder'
    ]

    qnty: int = random.randint(3, 8)
    return set(random.sample(achievements, qnty))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()

    all_achievements = alice.union(bob).union(charlie).union(dylan)
    print(f"All distinct achievements: {all_achievements}")

    print()

    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"Common achievements: {common}")

    print()

    alice_unique = alice.difference(bob).difference(charlie).difference(dylan)
    bob_unique = bob.difference(alice).difference(charlie).difference(dylan)
    charli_unique = charlie.difference(bob).difference(alice).difference(dylan)
    dylan_unique = dylan.difference(bob).difference(charlie).difference(alice)

    print(f"Only Alice has: {alice_unique}")
    print(f"Only Bob has: {bob_unique}")
    print(f"Only Charlie has: {charli_unique}")
    print(f"Only Dylan has: {dylan_unique}")

    print()

    print(f"Alice is missing: {all_achievements - alice}")
    print(f"Bob is missing: {all_achievements - bob}")
    print(f"Charlie is missing: {all_achievements - charlie}")
    print(f"Dylan is missing: {all_achievements - dylan}")


if __name__ == "__main__":
    main()
