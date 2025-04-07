import time

def liftoff():
    print("🚀 Question No 04 - Lift Off Countdown\n")

    try:
        speed = input("Choose countdown speed in seconds (default is 1): ")
        speed = float(speed) if speed else 1.0
        if speed < 0:
            print("⛔ Speed can't be negative. Using default speed.")
            speed = 1.0
    except ValueError:
        print("⚠️ Invalid input. Using default speed (1 second).")
        speed = 1.0

    print("\n🔥 Countdown initiated!\n")
    for i in range(10, -1, -1):  # countdown from 10 to 0
        print(f"{i}...")
        time.sleep(speed)

    print("\n🚀 LIFT OFF! 🚀")
    print("""
        |
       / \\
      / _ \\
     | (_) |
     |     |
     |  |  |
    /|__|__|\\
      /   \\
    """)
    
liftoff()
