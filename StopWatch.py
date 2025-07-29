import time

def stopwatch():
    start_time = None
    elapsed_time = 0
    running = False

    while True:
        print("\nStopwatch Menu:")
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            if not running:
                start_time = time.time()
                running = True
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")

        elif choice == '2':
            if running:
                elapsed_time += time.time() - start_time
                running = False
                print(f"Stopped at {format_time(elapsed_time)}.")
            else:
                print("Stopwatch is not running.")

        elif choice == '3':
            start_time = None
            elapsed_time = 0
            running = False
            print("Stopwatch reset.")

        elif choice == '4':
            if running:
                elapsed_time += time.time() - start_time
            print(f"Final time: {format_time(elapsed_time)}")
            print("Exiting stopwatch.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

def format_time(seconds):
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

stopwatch()
