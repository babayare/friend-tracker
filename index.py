# Function to add a new friend
def add_friend(friends_list):
    name = input("Enter friend's name: ")
    age = input("Enter friend's age: ")
    email = input("Enter friend's email: ")
    friends_list.append({"Name": name, "Age": age, "Email": email})
    print("Friend added successfully!")

# Function to display all friends
def display_friends(friends_list):
    if not friends_list:
        print("You have no friends in your list.")
    else:
        print("Your Friends:")
        for idx, friend in enumerate(friends_list, start=1):
            print(f"{idx}. Name: {friend['Name']}, Age: {friend['Age']}, Email: {friend['Email']}")

# Function to search for a friend by name
def search_friend(friends_list):
    name = input("Enter friend's name to search: ")
    found = False
    for friend in friends_list:
        if friend['Name'].lower() == name.lower():
            print("Friend found:")
            print(f"Name: {friend['Name']}, Age: {friend['Age']}, Email: {friend['Email']}")
            found = True
            break
    if not found:
        print("Friend not found.")

# Main function
def main():
    friends = []
    while True:
        print("\n1. Add a friend")
        print("2. Display all friends")
        print("3. Search for a friend")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_friend(friends)
        elif choice == '2':
            display_friends(friends)
        elif choice == '3':
            search_friend(friends)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
