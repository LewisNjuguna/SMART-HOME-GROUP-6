import random
import time


CORRECT_PIN = "1234"

print("\n" + "*" * 45)
print("*   SMART HOME SYSTEM - Nairobi Apartments   *")
print("*" * 45)

while True:
    print("\n  Select a feature:")
    print("  1. Smart Door Lock")
    print("  2. Smart Lighting")
    print("  3. Smart Dishwasher")
    print("  4. Temperature Control")
    print("  5. Exit")

    main_choice = input("\n  Enter your choice (1-5): ").strip()

    # FEATURE 1: SMART DOOR LOCK
    if main_choice == "1":
        print("\n" + "=" * 45)
        print("  SMART DOOR LOCK")
        print("=" * 45)
        print("  Secure PIN-protected entry system")

        max_attempts = 3
        attempts = 0
        locked_out = False

        while attempts < max_attempts:
            remaining = max_attempts - attempts
            print(f"\n  Attempts remaining: {remaining}")
            pin = input("  Enter PIN: ")

            if pin == CORRECT_PIN:
                print("\n  Correct PIN!")
                time.sleep(1.0)
                print("  Door UNLOCKED")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("  Incorrect PIN. Please try again.")
                else:
                    locked_out = True

        if locked_out:
            print("\n  Too many failed attempts!")
            time.sleep(1.0)
            print("  Door LOCKED")
            print("  Notification: Unauthorized access attempt detected.")

    # FEATURE 2: SMART LIGHTING
    elif main_choice == "2":
        print("\n" + "=" * 45)
        print("  SMART LIGHTING SYSTEM")
        print("=" * 45)
        print("  Auto-controls lights based on time and motion")

        print("\n  How would you like to set the time?")
        print("  1. Use a random time")
        print("  2. Enter the hour manually")

        light_choice = input("\n  Choose (1 or 2): ")

        valid_input = True
        hour = 0

        if light_choice == "1":
            hour = random.randint(0, 23)
            print(f"\n  Random time: {hour:02d}:00")
        elif light_choice == "2":
            hour_text = input("\n  Enter current hour (0 - 23): ")
            if hour_text.isdigit() and 0 <= int(hour_text) <= 23:
                hour = int(hour_text)
            else:
                print("  Invalid input. Please enter a number between 0 and 23.")
                valid_input = False
        else:
            print("  Invalid choice.")
            valid_input = False

        if valid_input:
            motion = input("  Is motion detected in the room? (yes/no): ").strip().lower()

            print()
            time.sleep(1.0)

            is_daytime = 6 <= hour <= 18

            if is_daytime:
                print("  Daytime detected.")
                print("  Lights are OFF - natural light is sufficient.")
                if motion == "yes":
                    print("  Motion noted. Lights will activate if it gets dark.")
            else:
                if motion == "yes":
                    print("  Night-time detected + motion sensed.")
                    if hour >= 22 or hour < 5:
                        print("  Lights ON at 30% brightness - night mode.")
                        print("  Dim setting to avoid disturbing sleep.")
                    else:
                        print("  Lights ON at full brightness.")
                else:
                    print("  Night-time detected - no motion in room.")
                    print("  Lights remain OFF to save energy.")
                    print("  Motion sensor is active and watching.")

    # FEATURE 3: SMART DISHWASHER
    elif main_choice == "3":
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

    # FEATURE 4: TEMPERATURE CONTROL
    elif main_choice == "4":
        print("\n" + "=" * 45)
        print("  TEMPERATURE CONTROL SYSTEM")
        print("=" * 45)
        print("  Keeps room temperature close to your target")

        print("\n  How would you like to set the current temperature?")
        print("  1. Use a random temperature")
        print("  2. Enter the temperature manually")

        temp_choice = input("\n  Choose (1 or 2): ")

        valid_input = True
        current_temp = 0

        if temp_choice == "1":
            current_temp = random.randint(10, 35)
            print(f"\n  Random current temperature: {current_temp} C")
        elif temp_choice == "2":
            temp_text = input("\n  Enter current temperature in C: ")
            if temp_text.lstrip("-").isdigit():
                current_temp = int(temp_text)
            else:
                print("  Invalid input. Please enter a whole number.")
                valid_input = False
        else:
            print("  Invalid choice.")
            valid_input = False

        if valid_input:
            target_text = input("  Enter target temperature in C: ")
            if target_text.lstrip("-").isdigit():
                target_temp = int(target_text)

                print()
                time.sleep(1.0)

                print(f"  Current temperature: {current_temp} C")
                print(f"  Target temperature: {target_temp} C")

                difference = current_temp - target_temp

                if difference > 5:
                    print("  Room is much too warm.")
                    print("  Cooling system ON - high speed.")
                elif difference > 0:
                    print("  Room is slightly too warm.")
                    print("  Cooling system ON - low speed.")
                elif difference < -5:
                    print("  Room is much too cold.")
                    print("  Heating system ON - high speed.")
                elif difference < 0:
                    print("  Room is slightly too cold.")
                    print("  Heating system ON - low speed.")
                else:
                    print("  Room is already at the target temperature.")
                    print("  Heating and cooling systems OFF.")
            else:
                print("  Invalid input. Please enter a whole number.")

    # EXIT
    elif main_choice == "5":
        print("\n  Smart Home System shutting down.")
        print("*" * 45 + "\n")
        break

    else:
        print("\n  Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        continue

    input("\n  Press Enter to return to the main menu...")
