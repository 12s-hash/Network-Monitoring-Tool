import psutil

print("=" * 50)
print("       SYSTEM MONITOR")
print("=" * 50)

# CPU Usage
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage       : {cpu}%")

# RAM Usage
memory = psutil.virtual_memory()
print(f"RAM Usage       : {memory.percent}%")

# Disk Usage
disk = psutil.disk_usage('/')
print(f"Disk Usage      : {disk.percent}%")

# Battery Information
battery = psutil.sensors_battery()

if battery:
    print(f"Battery         : {battery.percent}%")
    if battery.power_plugged:
        print("Charging        : Yes")
    else:
        print("Charging        : No")
else:
    print("Battery         : Not Available")

# Network Statistics
network = psutil.net_io_counters()

print(f"Bytes Sent      : {network.bytes_sent}")
print(f"Bytes Received  : {network.bytes_recv}")

print("=" * 50)