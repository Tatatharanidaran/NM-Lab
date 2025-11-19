todos = []

def add_todo(task):
    todos.append(task)
    print(f"Added: {task}")

def remove_todo(index):
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid index")

def list_todos():
    if not todos:
        print("No todos yet.")
    else:
        for i, task in enumerate(todos):
            print(f"{i}: {task}")

def main():
    while True:
        print("\n1. Add todo")
        print("2. Remove todo")
        print("3. List todos")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            add_todo(task)
        elif choice == '2':
            index = int(input("Enter index to remove: "))
            remove_todo(index)
        elif choice == '3':
            list_todos()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
