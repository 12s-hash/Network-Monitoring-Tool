import tkinter as tk
import socket
import platform
import requests
import psutil
from ping_test import check_ping
import datetime


# -------------------------
# Refresh Function
# -------------------------

def refresh():
    

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    try:
        public_ip = requests.get(
            "https://api.ipify.org",
            timeout=5
        ).text
    except:
        public_ip = "No Internet"

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    battery = psutil.sensors_battery()

    if battery:
        battery_percent = str(battery.percent) + "%"
    else:
        battery_percent = "Not Available"

    network = psutil.net_io_counters()

    os_name = platform.system() + " " + platform.release()
    processor = platform.machine()
    total_ram = round(psutil.virtual_memory().total / (1024**3), 2)
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
       requests.get("https://www.google.com", timeout=2)
       internet = "Online"
    except:
       internet = "Offline"

    hostname_label.config(text=hostname)
    localip_label.config(text=local_ip)
    publicip_label.config(text=public_ip)
    cpu_label.config(text=str(cpu) + "%")
    ram_label.config(text=str(ram) + "%")
    disk_label.config(text=str(disk) + "%")
    battery_label.config(text=battery_percent)
    sent_label.config(text=str(network.bytes_sent))
    received_label.config(text=str(network.bytes_recv))

    os_label.config(text=os_name)
    processor_label.config(text=processor)
    totalram_label.config(text=f"{total_ram} GB")
    datetime_label.config(text=current_time)
    internet_label.config(text=internet)

    if internet == "Online":
       internet_label.config(fg="green")
    else:
       internet_label.config(fg="red")

    if cpu > 80:
      cpu_label.config(text=str(cpu) + "%", fg="red")
    else:
      cpu_label.config(text=str(cpu) + "%", fg="green")

    if ram > 80:
       ram_label.config(text=str(ram) + "%", fg="red")
    else:
      ram_label.config(text=str(ram) + "%", fg="green")

    root.after(1000, refresh)
    
# -------------------------
# Ping Function
# -------------------------

def ping_website():
    #print("Ping button clicked")

    host = website_entry.get().strip()

    if host == "":
        ping_result.config(text="Please enter a website", fg="red")
        return

    result = check_ping(host)
    #print(result)

    if isinstance(result, float):
        ping_result.config(
            text=f"✅ Reachable ({result} ms)",
            fg="green"
        )
    else:
        ping_result.config(
            text=f"❌ {result}",
            fg="red"
        )
# -------------------------
# GUI
# -------------------------

root = tk.Tk()

root.title("Network Monitoring Tool")
root.geometry("800x600")
root.configure(bg="#F4F6F8")

title = tk.Label(
    root,
    text="NETWORK MONITORING TOOL",
    font=("Arial",18,"bold"),
    bg="#1565C0",
    fg="white",
    pady=10
)

title.pack(fill="x")

frame = tk.Frame(root,bg="#F4F6F8")
frame.pack(pady=20)

# Labels

labels = [
    "💻 Host Name",
    "🌐 Local IP",
    "🌍 Public IP",
    "🖥 CPU Usage",
    "💾 RAM Usage",
    "📀 Disk Usage",
    "🔋 Battery",
    "📤 Bytes Sent",
    "📥 Bytes Received",
    "💻 Operating System",
    "⚙ Processor",
    "🧠 Total RAM",
    "📅 Date & Time",
    "🌐 Internet Status"
]

value_labels=[]

for i,text in enumerate(labels):

    tk.Label(
        frame,
        text=text,
        font=("Arial",12,"bold"),
        bg="#F4F6F8"
    ).grid(row=i,column=0,sticky="w",padx=10,pady=5)

    value=tk.Label(
        frame,
        text="------",
        font=("Arial",12),
        bg="#F4F6F8"
    )

    value.grid(row=i,column=1,padx=20)

    value_labels.append(value)

hostname_label=value_labels[0]
localip_label=value_labels[1]
publicip_label=value_labels[2]
cpu_label=value_labels[3]
ram_label=value_labels[4]
disk_label=value_labels[5]
battery_label=value_labels[6]
sent_label=value_labels[7]
received_label=value_labels[8]
os_label = value_labels[9]
processor_label = value_labels[10]
totalram_label = value_labels[11]
datetime_label = value_labels[12]
internet_label = value_labels[13]


# -------------------------
# Ping Section
# -------------------------

ping_frame = tk.Frame(root, bg="#F4F6F8")
ping_frame.pack(pady=20)

tk.Label(
    ping_frame,
    text="🌐 Website",
    font=("Arial",12,"bold"),
    bg="#F4F6F8"
).grid(row=0,column=0,padx=10)

website_entry = tk.Entry(
    ping_frame,
    width=25,
    font=("Arial",12)
)

website_entry.grid(row=0,column=1,padx=10)

website_entry.insert(0,"google.com")

tk.Button(
    ping_frame,
    text="Ping",
    font=("Arial",11,"bold"),
    bg="#1565C0",
    fg="white",
    command=ping_website
).grid(row=0,column=2,padx=10)

ping_result = tk.Label(
    ping_frame,
    text="",
    font=("Arial",12,"bold"),
    bg="#F4F6F8"
)

ping_result.grid(row=1,column=0,columnspan=3,pady=10)
tk.Button(
    root,
    text="❌ Exit",
    font=("Arial",12,"bold"),
    bg="red",
    fg="white",
    command=root.destroy
).pack()

refresh()

root.mainloop()