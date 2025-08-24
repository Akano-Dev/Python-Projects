def unit_converter():
    print("\n=== Unit Converter ===")
    print("1. Temperature (C ↔ F)")
    print("2. Distance (km ↔ miles)")
    print("3. Weight (kg ↔ pounds)")
    choice = input("Choose an option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")

    elif choice == "2":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")

    elif choice == "3":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} lbs")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    unit_converter()
