import random

def mad_libs_adventure():
    print("✨ Welcome to the Magical Adventure Mad Libs! ✨")
    print("Fill in the blanks to create your own fantasy story.\n")

    # Collect words from the user
    hero_name = input("Enter a hero's name: ")
    magical_creature = input("Enter a magical creature: ")
    place = input("Enter a mystical place: ")
    adjective1 = input("Enter an adjective: ")
    object1 = input("Enter a magical object: ")
    verb = input("Enter a verb ending in -ing: ")
    adjective2 = input("Enter another adjective: ")
    object2 = input("Enter another object: ")

    # Create the story using f-strings
    story = f"""
    In the land of {place}, there lived a brave soul named {hero_name}.
    One {adjective1} morning, {hero_name} stumbled upon a mysterious {object1} glowing beneath a tree.
    Suddenly, a {magical_creature} appeared, {verb} through the enchanted forest.

    The creature whispered, "Only the {adjective2} may wield the power of the {object2}."
    With courage in their heart, {hero_name} took a deep breath and stepped into the unknown...

    And thus began the legend of {hero_name}, the chosen one of {place}.
    """

    print("\nHere is your magical story:")
    print(story)

# Run the function
mad_libs_adventure()
