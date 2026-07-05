import random
import time


def temperature_control():
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
