import json


def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)


def add_todo(todos):
    todo = input("Enter new todo: ")
    todos.append({"task": todo, "completed": False})
    save_todos(todos)
    print("Todo added successfully!")


def edit_todo(todos):
    show_todos(todos)
    index = int(input("Enter the index of the todo to edit: "))-1
    if index < 0 or index >= len(todos):
        print("Invalid index!")
        return
    todos[index]["task"] = input("Enter new task: ")
    save_todos(todos)
    print("Todo edited successfully!")


def complete_todo(todos):
    show_todos(todos)
    index = int(input("Enter the index of the todo to complete: "))-1
    if index < 0 or index >= len(todos):
        print("Invalid index!")
        return
    todos[index]["completed"] = True
    save_todos(todos)
    print("Todo completed!")


def delete_todo(todos):
    show_todos(todos)
    index = int(input("Enter the index of the todo to delete: "))-1
    if index < 0 or index >= len(todos):
        print("Invalid index!")
        return
    del todos[index]
    save_todos(todos)
    print("Todo deleted successfully!")


def show_todos(todos):
    if not todos:
        print("No todos found!")
        return
    for i, todo in enumerate(todos):
        status = "Completed" if todo["completed"] else "Pending"
        print(f"{i+1}. {todo['task']} ({status})")


def main():
    todos = load_todos()
    while True:
        print("\nChoose an option:")
        print("1. Add todo")
        print("2. Edit todo")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Show todos")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            edit_todo(todos)
        elif choice == '3':
            complete_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '5':
            show_todos(todos)
        elif choice == '6':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()