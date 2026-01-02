def start():
    print("\n--- The Lost Realm of Eldoria ---")
    print("You stand at the edge of an ancient forest.")
    print("A crumbling sign reads: 'Only the brave may enter.'")
    print("\nWhat do you do?")
    print("1. Enter the forest")
    print("2. Turn back")

    choice = input("> ")

    if choice == "1":
        forest()
    elif choice == "2":
        print("\nYou turn back, forever wondering what might have been.")
        print("THE END.")
    else:
        print("Invalid choice.")
        start()


def forest():
    print("\nTall trees surround you. The forest is eerily quiet.")
    print("You come to a fork in the path.")
    print("1. Take the moss-covered path")
    print("2. Take the rocky trail")

    choice = input("> ")

    if choice == "1":
        ruins()
    elif choice == "2":
        wolf()
    else:
        print("Invalid choice.")
        forest()


def ruins():
    print("\nYou discover ancient stone ruins.")
    print("A glowing artifact rests on a pedestal.")
    print("1. Take the artifact")
    print("2. Leave it alone")

    choice = input("> ")

    if choice == "1":
        artifact()
    elif choice == "2":
        guardian()
    else:
        print("Invalid choice.")
        ruins()


def artifact():
    print("\nAs you take the artifact, the ground shakes!")
    print("A hidden passage opens beneath your feet.")
    print("1. Enter the passage")
    print("2. Try to escape")

    choice = input("> ")

    if choice == "1":
        underground()
    elif choice == "2":
        print("\nThe ruins collapse.")
        print("You are buried beneath the stones. Game Over.")
    else:
        print("Invalid choice.")
        artifact()


def underground():
    print("\nYou find an underground chamber filled with glowing runes.")
    print("A voice whispers: 'Choose wisely.'")
    print("1. Touch the runes")
    print("2. Follow the tunnel")

    choice = input("> ")

    if choice == "1":
        print("\nThe runes grant you ancient knowledge.")
        print("You emerge as a Sage of Eldoria.")
        print("YOU WIN!")
    elif choice == "2":
        dragon()
    else:
        print("Invalid choice.")
        underground()


def guardian():
    print("\nA stone guardian awakens!")
    print("1. Fight the guardian")
    print("2. Run away")

    choice = input("> ")

    if choice == "1":
        print("\nThe guardian is too strong.")
        print("You fall in battle. Game Over.")
    elif choice == "2":
        village()
    else:
        print("Invalid choice.")
        guardian()


def wolf():
    print("\nA giant wolf blocks your path, growling.")
    print("1. Stand your ground")
    print("2. Climb a tree")

    choice = input("> ")

    if choice == "1":
        print("\nThe wolf attacks.")
        print("You are defeated. Game Over.")
    elif choice == "2":
        village()
    else:
        print("Invalid choice.")
        wolf()


def village():
    print("\nYou reach a hidden village.")
    print("The villagers speak of a castle beyond the hills.")
    print("1. Visit the castle")
    print("2. Stay in the village")

    choice = input("> ")

    if choice == "1":
        castle()
    elif choice == "2":
        print("\nYou live peacefully among the villagers.")
        print("A quiet but happy ending.")
        print("THE END.")
    else:
        print("Invalid choice.")
        village()


def dragon():
    print("\nA massive dragon guards a golden gate.")
    print("1. Challenge the dragon")
    print("2. Sneak past")

    choice = input("> ")

    if choice == "1":
        print("\nThe dragon incinerates you.")
        print("Game Over.")
    elif choice == "2":
        print("\nYou enter Eldoria unseen.")
        print("You uncover its secrets and return a legend.")
        print("YOU WIN!")
    else:
        print("Invalid choice.")
        dragon()


def castle():
    print("\nThe castle gates open slowly.")
    print("A crowned figure awaits you.")
    print("1. Kneel")
    print("2. Draw your weapon")

    choice = input("> ")

    if choice == "1":
        print("\nThe ruler names you Champion of Eldoria.")
        print("YOU WIN!")
    elif choice == "2":
        print("\nGuards overwhelm you.")
        print("Game Over.")
    else:
        print("Invalid choice.")
        castle()


# Start game
start()
