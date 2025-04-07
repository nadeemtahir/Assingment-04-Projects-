import time
import sys

# Utility for colored text
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

# Loading animation
def loading_animation(seconds=3):
    print(color("⏳ Preparing countdown", "93"), end='')
    for _ in range(seconds):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print('\n')

# Countdown function
def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timeformat = color('{:02d}:{:02d}'.format(mins, secs), "96")
        print(f"⏰ Time Left: {timeformat}", end='\r')
        time.sleep(1)
        t -= 1
    print(color("⏰ Time's up! 00:00 🔔", "91"))

# Safe user input
def get_time_input():
    while True:
        try:
            seconds = int(input(color("⏱️ Enter the time in seconds: ", "94")))
            if seconds > 0:
                return seconds
            else:
                print(color("⚠️ Please enter a number greater than 0.", "93"))
        except ValueError:
            print(color("❌ Invalid input. Please enter a whole number.", "91"))

# Main execution
def start_timer():
    loading_animation()
    t = get_time_input()
    countdown(t)
    print(color("🎉 Countdown complete! Have a great day!", "92"))

if __name__ == '__main__':
    start_timer()
