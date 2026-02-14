# homework6_<firstname_lastname>.py
# Python Week 6 Assignment: If and While

# -----------------------------
# Conditional Lists
# -----------------------------

# Existing website users
web_users = ["alice", "bob", "charlie", "diana", "edward"]

# New users attempting to register
new_users = ["frank", "diana", "george", "alice", "hannah"]

# Check availability
for user in new_users:
    if user.lower() in [w.lower() for w in web_users]:
        print(f"This user name '{user}' is already in use. Please choose a different user name.")
    else:
        print(f"This user name '{user}' is available.")

print("\n")  # Just for spacing between sections

# -----------------------------
# Nested Dictionaries
# -----------------------------

# Cities dictionary
cities = {
    "Paris": {
        "country": "France",
        "population": 2148000,
        "fact": "Known as the City of Light."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13929286,
        "fact": "Has the busiest metropolitan area in the world."
    },
    "New York": {
        "country": "USA",
        "population": 8419000,
        "fact": "Famous for Times Square and Central Park."
    }
}

# Print city information
for city_name, city_info in cities.items():
    print(f"City: {city_name}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}\n")
