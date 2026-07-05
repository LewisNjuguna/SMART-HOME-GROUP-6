import time


def smart_dishwasher():
    print("\n" + "=" * 45)
    print("  SMART DISHWASHER")
    print("=" * 45)
    print("  Automated wash cycle control")

    is_running = False
    is_door_locked = False
    wash_cycle = "Normal"
    time_remaining = 0

    while True:
        print("\n  1. Load Dishes")
        print("  2. Select Wash Cycle")
        print("  3. Start Dishwasher")
        print("  4. Check Status")
        print("  5. Return to Main Menu")

        dish_choice = input("\n  Enter your choice (1-5): ").strip()

        if dish_choice == "1":
            if is_running:
                print("\n  Cannot load dishes while dishwasher is running.")
            else:
                print("\n  Dishes loaded into the dishwasher.")

        elif dish_choice == "2":
            cycle = input("\n  Enter cycle (Quick/Normal/Heavy/Eco): ").strip().capitalize()
            if cycle in ["Quick", "Normal", "Heavy", "Eco"]:
                wash_cycle = cycle
                print(f"  Wash cycle set to {cycle}.")
            else:
                print("  Invalid cycle. Choose from: Quick, Normal, Heavy, Eco")

        elif dish_choice == "3":
            if is_running:
                print("\n  Dishwasher is already running.")
            else:
                is_door_locked = True
                is_running = True

                if wash_cycle == "Quick":
                    time_remaining = 30
                elif wash_cycle == "Normal":
                    time_remaining = 90
                elif wash_cycle == "Heavy":
                    time_remaining = 120
                else:
                    time_remaining = 150

                print(f"\n  Door locked. Starting {wash_cycle} cycle ({time_remaining} minutes).")
                time.sleep(1.0)

                while time_remaining > 0:
                    print(f"  Time remaining: {time_remaining} minutes")
                    time_remaining -= 30
                    time.sleep(1.0)

                is_running = False
                is_door_locked = False
                print("  Cycle complete. Door unlocked. Dishes are clean.")

        elif dish_choice == "4":
            if is_running:
                state = "Running"
            else:
                state = "Idle"

            if is_door_locked:
                lock_state = "Locked"
            else:
                lock_state = "Unlocked"

            print(f"\n  Status: {state}, Door: {lock_state}, Cycle: {wash_cycle}, "
                  f"Time remaining: {time_remaining} minutes")

        elif dish_choice == "5":
            print("\n  Returning to main menu.")
            break

        else:
            print("\n  Invalid choice. Please enter 1-5.")
