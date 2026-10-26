
# Facts
birds = ["parrot", "pigeon", "sparrow", "ostrich"]

# Rule
def can_fly(bird):
    if bird in birds and bird != "ostrich":
        return True
    else:
        return False

# Input
bird = input("Enter a bird name: ").lower()

# Output
if can_fly(bird):
    print(bird, "can fly.")
elif bird in birds:
    print(bird, "cannot fly.")
else:
    print(bird, "is not in the bird database.")
