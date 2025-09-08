tasks = []

while True:
    print("\n1. View tasks\n2. Add task\n3. Done\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        num = int(input("Enter task number done: "))
        if 0 < num <= len(tasks):
            print(f"Done ✅ {tasks.pop(num-1)}")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")
