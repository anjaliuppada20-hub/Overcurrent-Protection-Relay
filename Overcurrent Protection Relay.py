# Overcurrent Protection Relay
# Simple Python Simulation

# Safe current limit
limit = 10.0  # Amps

# Get measured current
current = float(input("Enter measured current (A): "))

# Check current
if current > limit:
    print("OVER CURRENT DETECTED!")
    print("Relay TRIPPED")
    print("Load DISCONNECTED")
else:
    print("Current is NORMAL")
    print("Relay ON")
    print("Load CONNECTED")
