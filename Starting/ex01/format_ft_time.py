import time
from datetime import datetime

try:
    seconds = time.time()
    print(f"Seconds since January 1, 1970:  {seconds} or {seconds:.2e}\
        in scientific notation")
    date_only = datetime.now().strftime("%b %d %Y")
    print(date_only)
except Exception as e:
    print("Error:", e)
