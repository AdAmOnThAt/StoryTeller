# Ask for the player's name
player_name = input("What's your name? ")

# Ask for another character's name
character_name = input("Enter another character's name: ")

# Ask for the name of the island
island_name = input("Enter the name of the island: ")

# Ask the player to choose an item
print("Choose your item:")
print("1. Sword and Shield")
print("2. Slingshot")
print("3. Cloak")

player_item = ""
companion_item = ""

while not player_item:
    choice = input("Enter the number of the item you choose: ")

    if choice == "1":
        player_item = "Sword and Shield"
    elif choice == "2":
        player_item = "Slingshot"
    elif choice == "3":
        player_item = "Cloak"
    else:
        print("Invalid choice. Please choose a valid item.")

# Companion cannot choose the same weapon as the player
if player_item == "Sword and Shield":
    companion_item_options = ["Slingshot", "Cloak"]
elif player_item == "Slingshot":
    companion_item_options = ["Sword and Shield", "Cloak"]
else:
    companion_item_options = ["Sword and Shield", "Slingshot"]

print(f"{character_name}, choose your item:")
print("1.", companion_item_options[0])
print("2.", companion_item_options[1])

while not companion_item:
    companion_choice = input("Enter the number of the item you choose: ")

    if companion_choice == "1":
        companion_item = companion_item_options[0]
    elif companion_choice == "2":
        companion_item = companion_item_options[1]
    else:
        print("Invalid choice. Please choose a valid item.")

# Greet the player, the other character, and mention the island with personalized messages
print(f"Welcome to {island_name}, {player_name} with a {player_item} and {character_name} with a {companion_item}! Get ready for an adventure where every code tells a story.")

if player_item == "Sword and Shield" and companion_item == "Slingshot":
    print("You and your companion arrive at the island on a boat and find two paths:")
    print("One path leads towards a deep forest...")
    print("The other path leads towards a river...")

    decision = input("Which path will you choose? (1 - Deep Forest, 2 - River): ")

    if decision == "1":
        print("You choose to enter the deep forest and are attacked by a giant spider!")
    elif decision == "2":
        print("You choose to enter the river and are attacked by a pack of wolves!")
    else:
        print("Invalid decision. Please choose a valid path (1 or 2).")

elif player_item == "Sword and Shield" and companion_item == "Cloak":
    print("You and your companion arrive at the island on a boat and find two paths:")
    print("One path leads towards a deep forest...")
    print("The other path leads towards a river...")

    decision = input("Which path will you choose? (1 - Deep Forest, 2 - River): ")

    if decision == "1":
        print("You choose to enter the deep forest and are attacked by a giant spider!")
    elif decision == "2":
        print("You choose to enter the river and are attacked by a pack of wolves!")
    else:
        print("Invalid decision. Please choose a valid path (1 or 2).")

elif player_item == "Slingshot" and companion_item == "Cloak":
    print("You and your companion arrive at the island on a boat and find two paths:")
    print("One path leads towards a deep forest...")
    print("The other path leads towards a river...")

    decision = input("Which path will you choose? (1 - Deep Forest, 2 - River): ")

    if decision == "1":
        print("You choose to enter the deep forest and are attacked by a giant spider!")
    elif decision == "2":
        print("You choose to enter the river and are attacked by a pack of wolves!")
    else:
        print("Invalid decision. Please choose a valid path (1 or 2).")

else:
    print("Invalid combination of items chosen.")

# Attack feature
player_hp = 100
companion_hp = 100
enemy_hp_river = 10
enemy_hp_forest = 15

sword_shield_damage = 25
cloak_damage = 5
slingshot_damage = 15
player_attacked_sword_shield = 5
player_attacked_slingshot = 15
player_attacked_cloak = 1

# Attack function to calculate damage taken
def attack(attacker, weapon, target):
    damage = 0

    if attacker == "player":
        if weapon == "Sword and Shield":
            damage = sword_shield_damage
        elif weapon == "Slingshot":
            damage = slingshot_damage
        elif weapon == "Cloak":
            damage = cloak_damage

        if weapon != "Sword and Shield":
            player_hp -= player_attacked_sword_shield

    if attacker == "companion":
        if weapon == "Sword and Shield":
            damage = sword_shield_damage
        elif weapon == "Slingshot":
            damage = slingshot_damage
        elif weapon == "Cloak":
            damage = cloak_damage

    target -= damage
    return target, damage

# Battle function to initiate a battle sequence
def battle(location, player_weapon, companion_weapon):
    global player_hp, companion_hp

    if location == "River":
        enemy_hp = enemy_hp_river
    elif location == "Deep Forest":
        enemy_hp = enemy_hp_forest

    print(f"A wild enemy appears in the {location}!")
    print(f"Player HP: {player_hp}")
    print(f"Companion HP: {companion_hp}")
    print(f"Enemy HP: {enemy_hp}")

    while enemy_hp > 0 and player_hp > 0 and companion_hp > 0:
        # Player's Turn
        player_decision = input("Player's Turn - Choose 'Attack' or 'Skip': ")

        if player_decision.lower() == "attack":
            enemy_hp, damage_player = attack("player", player_weapon, enemy_hp)
            print(f"Player attacks with {player_weapon} and causes {damage_player} damage to the enemy.")
        elif player_decision.lower() == "skip":
            player_hp -= 5
            print("Player decides to skip and loses 5 HP.")

        print(f"Player HP: {player_hp}")
        print(f"Enemy HP: {enemy_hp}")

        if enemy_hp <= 0:
            print("Enemy defeated!")
            break

        # Companion's Turn
        companion_decision = input("Companion's Turn - Choose 'Attack' or 'Skip': ")

        if companion_decision.lower() == "attack":
            enemy_hp, damage_companion = attack("companion", companion_weapon, enemy_hp)
            print(f"Companion attacks with {companion_weapon} and causes {damage_companion} damage to the enemy.")
        elif companion_decision.lower() == "skip":
            companion_hp -= 5
            print("Companion decides to skip and loses 5 HP.")

        print(f"Companion HP: {companion_hp}")
        print(f"Enemy HP: {enemy_hp}")

        if player_hp <= 0 or companion_hp <= 0:
            print("Player or Companion defeated! Game Over.")
            break

# Start level 2
print("Level 2: The Creepies")
if __name__ == "__main__":
    battle("Spooky graveyard", player_item, companion_item)
    print(f"Welcome to leve 2 of {island_name}, {player_name} with a {player_item} and {character_name} with a {companion_item}! Get ready for the second part of the adventure where every code tells a story.")

    if player_item == "Sword and Shield" and companion_item == "Slingshot":
      print("You and your companion arrive at the island on a boat and find two paths:")
      print("One path leads towards a spooky graveyard...")
      print("The other path leads towards a abandoned church...")

      decision = input("Which path will you choose? (1 - Spooky Graveyard, 2 - abamdoned church): ")

      if decision == "1":
          print("You choose to enter the spooky graveyard and are attacked by a crazy zombie!")
      elif decision == "2":
          print("You choose to enter the river and are attacked by a bunch of bad spirits!")
      else:
          print("Invalid decision. Please choose a valid path (1 or 2).")

    elif player_item == "Sword and Shield" and companion_item == "Cloak":
        print("You and your companion arrive at the island on a boat and find two paths:")
        print("One path leads towards a spooky graveyard...")
        print("The other path leads towards a abandoned church...")

        decision = input("Which path will you choose? (1 - Spooky Graveyard, 2 - abamdoned church): ")

        if decision == "1":
            print("You choose to enter the spooky graveyard and are attacked by a crazy zombie!")
        elif decision == "2":
            print("You choose to enter the river and are attacked by a bunch of bad spirits!")
        else:
            print("Invalid decision. Please choose a valid path (1 or 2).")

    elif player_item == "Slingshot" and companion_item == "Cloak":
      print("You and your companion arrive at the island on a boat and find two paths:")
    print("One path leads towards a spooky graveyard...")
    print("The other path leads towards a abandoned church...")

    decision = input("Which path will you choose? (1 - Spooky Graveyard, 2 - abamdoned church): ")

    if decision == "1":
        print("You choose to enter the spooky graveyard and are attacked by a crazy zombie!")
    elif decision == "2":
        print("You choose to enter the river and are attacked by a bunch of bad spirits!")

    else:
      print("Invalid combination of items chosen.")

  # Attack feature
    player_hp = 100
    companion_hp = 100
    enemy_hp_grave = 25
    enemy_hp_church = 75


    sword_shield_damage = 25
    cloak_damage = 5
    slingshot_damage = 15
    player_attacked_sword_shield = 15
    player_attacked_slingshot = 20
    player_attacked_cloak = 10

  # Attack function to calculate damage taken
    def attack(attacker, weapon, target):
      damage = 0

      if attacker == "player":
          if weapon == "Sword and Shield":
              damage = sword_shield_damage
          elif weapon == "Slingshot":
              damage = slingshot_damage
          elif weapon == "Cloak":
              damage = cloak_damage

          if weapon != "Sword and Shield":
              player_hp -= player_attacked_sword_shield

      if attacker == "companion":
          if weapon == "Sword and Shield":
              damage = sword_shield_damage
          elif weapon == "Slingshot":
              damage = slingshot_damage
          elif weapon == "Cloak":
              damage = cloak_damage

      target -= damage
      return target, damage

  # Battle function to initiate a battle sequence
    def battle(location, player_weapon, companion_weapon):
      global player_hp, companion_hp

      if location == "spooky graveyard":
          enemy_hp = enemy_hp_grave
      elif location == "abandoned church":
          enemy_hp = enemy_hp_church

      print(f"A wild enemy appears in the {location}!")
      print(f"Player HP: {player_hp}")
      print(f"Companion HP: {companion_hp}")
      print(f"Enemy HP: {enemy_hp}")

      while enemy_hp > 0 and player_hp > 0 and companion_hp > 0:
          # Player's Turn
          player_decision = input("Player's Turn - Choose 'Attack' or 'Skip': ")

          if player_decision.lower() == "attack":
              enemy_hp, damage_player = attack("player", player_weapon, enemy_hp)
              print(f"Player attacks with {player_weapon} and causes {damage_player} damage to the enemy.")
          elif player_decision.lower() == "skip":
              player_hp -= 5
              print("Player decides to skip and loses 5 HP.")

          print(f"Player HP: {player_hp}")
          print(f"Enemy HP: {enemy_hp}")

          if enemy_hp <= 0:
              print("Enemy defeated!")
              break

          # Companion's Turn
          companion_decision = input("Companion's Turn - Choose 'Attack' or 'Skip': ")

          if companion_decision.lower() == "attack":
              enemy_hp, damage_companion = attack("companion", companion_weapon, enemy_hp)
              print(f"Companion attacks with {companion_weapon} and causes {damage_companion} damage to the enemy.")
          elif companion_decision.lower() == "skip":
              companion_hp -= 5
              print("Companion decides to skip and loses 5 HP.")

          print(f"Companion HP: {companion_hp}")
          print(f"Enemy HP: {enemy_hp}")

          if player_hp <= 0 or companion_hp <= 0:
              print("Player or Companion defeated! Game Over.")
              break

  # Start the battle sequence when the script is executed directly
    if __name__ == "__main__":
      battle("Creepies", player_item, companion_item)