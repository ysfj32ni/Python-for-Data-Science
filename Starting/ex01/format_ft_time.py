import time
from datetime import datetime

seconds = time.time()

print("Seconds since January 1, 1970:", seconds , "or ", f"{seconds:.2e}" , " in scientific notation")

date_only = datetime.now().strftime("%a %b %d %Y")

print(date_only)
