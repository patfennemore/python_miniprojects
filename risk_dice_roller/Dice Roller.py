import random
attacker_user_input = int(input(f'How many troops are you attacking with?'))
defender_user_input = int(input(f'How many troops are you defending with?'))

attacker_roll_one = f"You rolled", random.randint(1, 6)
attacker_roll_two = f"You rolled", random.randint(1, 6)
attacker_roll_three = f"You rolled", random.randint(1, 6)

defender_roll_one = f"You rolled", random.randint(1, 6)
defender_roll_two = f"You rolled", random.randint(1, 6)

print(f'{attacker_roll_one}, {attacker_roll_two}, {attacker_roll_three}, {defender_roll_one}, {defender_roll_two}')


