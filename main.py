tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("New task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nTasks:")
        for t in tasks:
            print("-", t)

    elif choice == "3":
        break
