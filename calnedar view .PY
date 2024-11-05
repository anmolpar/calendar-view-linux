import calendar

while True:
    try:
        # Ask the user if they want to view a month or a year
        choice = raw_input("Do you want to view a month or a year? (month/year): ").strip().lower()

        if choice == 'month':
            # Ask the user for the year and month
            year = int(raw_input("Enter year (e.g., 2023): "))
            month = int(raw_input("Enter month (1-12): "))

            # Validate the month
            if month < 1 or month > 12:
                print
                "Invalid month. Please enter a value between 1 and 12."
                continue

            # Display the calendar for the specified month and year
            print
            calendar.month(year, month)

        elif choice == 'year':
            # Ask the user for the year
            year = int(raw_input("Enter year (e.g., 2023): "))

            # Display the calendar for the entire year
            print
            calendar.calendar(year)

        else:
            print
            "Invalid choice. Please enter 'month' or 'year'."
            continue

    except ValueError:
        print
        "Invalid input. Please enter numeric values for year and month."

    # Ask if the user wants to view another month or year
    another = raw_input("Do you want to view another month or year? (yes/no): ").strip().lower()
    if another != 'yes':
        print
        "Goodbye!"
        break