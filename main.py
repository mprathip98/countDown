import time

sec_time = int(input("How many second would you like to countdown?"))
for x in range(sec_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hour = int(x/3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print(time.clock())

print("TIMES UPPPPPP!")