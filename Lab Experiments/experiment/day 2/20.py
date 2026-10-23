
# Planets Database in Python

# Planet database: name, position, and type
planets = {
    "Mercury": {"position": 1, "type": "Terrestrial"},
    "Venus": {"position": 2, "type": "Terrestrial"},
    "Earth": {"position": 3, "type": "Terrestrial"},
    "Mars": {"position": 4, "type": "Terrestrial"},
    "Jupiter": {"position": 5, "type": "Gas Giant"},
    "Saturn": {"position": 6, "type": "Gas Giant"},
    "Uranus": {"position": 7, "type": "Ice Giant"},
    "Neptune": {"position": 8, "type": "Ice Giant"}
}

# Display all planets
def display_planets():
    print("\n--- Planets Database ---")
    for name, details in planets.items():
        print("Planet:", name,
              "| Position:", details["position"],
              "| Type:", details["type"])

# Search for a planet
def search_planet():
    name = input("Enter planet name: ").strip().title()

    if name in planets:
        print("\nPlanet:", name)
        print("Position from Sun:", planets[name]["position"])
        print("Type:", planets[name]["type"])
    else:
        print("Planet not found.")

# Display planets by type
def search_by_type():
    planet_type = input("Enter type (Terrestrial, Gas Giant, Ice Giant): ").strip().lower()

    found = False
    for name, details in planets.items():
        if details["type"].lower() == planet_type:
            print(name)
            found = True

    if not found:
        print("No planets found for this type.")

# Main menu
while True:
    print("\n===== PLANETS DATABASE =====")
    print("1. Display all planets")
    print("2. Search for a planet")
    print("3. Search planets by type")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_planets()
    elif choice == "2":
        search_planet()
    elif choice == "3":
        search_by_type()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
