import json

file_path = './userData.json'
with open(file_path, 'r') as file:
    data = json.load(file)
    
if "users" in data:
    users_data = data["users"]

    for user_id, user_info in users_data.items():
        print(f"User ID: {user_id}")
        print(f"Name: {user_info['name']}")
        print(f"Email: {user_info['email']}")
        print(f"Phone: {user_info['phone']}")

        address = user_info["address"]
        print("Address:")
        print(f"  Street: {address['street']}")
        print(f"  City: {address['city']}")
        print(f"  State: {address['state']}")
        print(f"  ZIP: {address['zip']}")

        is_active=user_info['is_active']
        print(f"Active Status: {'Active' if is_active else 'Inactive'}")
        print("-----------------------------")
else:
    print("No user data found in the JSON file.")

