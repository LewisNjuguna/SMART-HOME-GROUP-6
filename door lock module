import time

CORRECT_PIN = "1234"


def smart_door_lock():
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
