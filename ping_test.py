import subprocess
import re

def check_ping(host):
    try:
        output = subprocess.check_output(
            ["ping", "-n", "1", host],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        #print("PING OUTPUT:")
        #print(output)

        match = re.search(r"time[=<]\s*(\d+)\s*ms", output, re.IGNORECASE)

        if match:
            return float(match.group(1))

        return "Host Unreachable"

    except Exception as e:
        #print("ERROR:", e)
        return "Host Unreachable"