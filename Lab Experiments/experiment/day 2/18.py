
# Name and Date of Birth Database

# Store names and DOBs in a dictionary
database = {
    "Arun": "2002-01-15",
    "Bala": "2003-06-20",
    "Chitra": "2004-09-10",
    "Devi": "2002-12-25",
    "Kumar": "2003-03-08"
}

# Display all records
print("Name and DOB Database")
print("---------------------")

for name, dob in database.items():
    print("Name:", name, "| DOB:", dob)

# Search for a person's DOB
search_name = input("\nEnter a name to search: ")

if search_name in database:
    print("Name:", search_name)
    print("Date of Birth:", database[search_name])
else:
    print("Name not found in database.")
