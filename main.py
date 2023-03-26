import time
import psutil

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = cpu_usage / 100.0
    cpu_bar = '🔋' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = '🔋' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\nCPU Usage: |{cpu_bar}| |{cpu_usage:.2f}%", end = " ")
    print(f"\nMEM Usage: |{mem_bar}| {mem_usage:.2f}%", end = "\n")


while True: 
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 50)
    time.sleep(1.0)