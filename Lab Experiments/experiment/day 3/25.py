
# Monkey and Banana Problem

monkey = "at_door"
box = "at_window"
banana = "hanging"
has_banana = False

print("Initial State:")
print("Monkey is at the door.")
print("Box is at the window.")
print("Banana is hanging from the ceiling.")

# Step 1: Monkey moves to the box
monkey = "at_window"
print("\nMonkey moves to the window.")

# Step 2: Monkey pushes the box under the banana
box = "under_banana"
monkey = "under_banana"
print("Monkey pushes the box under the banana.")

# Step 3: Monkey climbs onto the box
monkey = "on_box"
print("Monkey climbs onto the box.")

# Step 4: Monkey grabs the banana
if monkey == "on_box" and box == "under_banana":
    has_banana = True
    print("Monkey grabs the banana!")

# Final State
if has_banana:
    print("\nGoal Achieved: Monkey has the banana.")
else:
    print("\nGoal not achieved.")
