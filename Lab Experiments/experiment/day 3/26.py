
# Prolog: Fruits and Colours using Backtracking

# Knowledge Base (Facts)
fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grapes": "green",
    "mango": "yellow",
    "cherry": "red",
    "guava": "green"
}

# Backtracking function
def find_fruits(color, fruit_list):
    if not fruit_list:
        return

    fruit = fruit_list[0]

    if fruits[fruit] == color:
        print(fruit)

    # Backtracking: check the remaining fruits
    find_fruits(color, fruit_list[1:])


# Main program
print("FRUITS AND COLOURS USING BACKTRACKING")

color = input("Enter a colour (red/yellow/green/orange): ").lower()

print("Fruits with", color, "colour are:")

if color in fruits.values():
    find_fruits(color, list(fruits.keys()))
else:
    print("No fruits found for this colour.")
