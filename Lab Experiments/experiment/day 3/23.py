
# Facts
parents = {
    "john": ["mary", "david"],
    "mary": ["alice", "bob"],
    "david": ["charlie"]
}

# Rule: Find children of a person
def children(person):
    return parents.get(person, [])

# Rule: Find the parent of a person
def find_parent(child):
    for parent, kids in parents.items():
        if child in kids:
            return parent
    return None

# Main program
name = input("Enter a person's name: ").lower()

parent = find_parent(name)

if parent:
    print(name, "is the child of", parent)
else:
    print("Parent not found for", name)

kids = children(name)

if kids:
    print(name, "is the parent of:", ", ".join(kids))
else:
    print(name, "has no children in the family tree.")
