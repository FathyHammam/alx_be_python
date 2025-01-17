# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item to the shopping list
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Prompt for and remove an item from the shopping list
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"'{item}' has 
