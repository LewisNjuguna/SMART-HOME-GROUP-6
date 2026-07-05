import random
import time


def smart_lighting():
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
