while True:
    print("To-Do List - ")
    print("1.Add Task")
    print("2.View Task")
    print("3.Mark as done")
    print("4.Exit")

    TC = input("Please choose an option : ")

    if TC == '1':
        task = input("Enter the task : ") 
        print("Task Added!")

    elif TC == '2':
        print("Viewing the Task. . .")

    elif TC == '3':
        print("Marking is done!")

    elif TC == "4":
        print("Exit")
        break

    else:
        print("Invalid Operation, Please try again")

    again = input("Do you want to do something else? (Yes/No): ")
    if again.lower() != "yes":
        print("Exiting To-Do List . . .")
        break