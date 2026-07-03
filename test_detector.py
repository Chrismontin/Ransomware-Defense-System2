import time

from modules.detector import analyze_event

print("Testing ransomware detector...\n")

for i in range(12):

    detected, count = analyze_event()

    print(f"Event {i+1} -> Count: {count}")

    if detected:
        print("\n🚨 RANSOMWARE DETECTED 🚨")
        break

    time.sleep(0.3)