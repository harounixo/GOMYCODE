import time

def countdown(t):
    while t >= 0:
        minutes, seconds = divmod(t, 60)
        timeformat = str(minutes) + ":" + str(seconds)
        print(timeformat, end = '\r' )
        t-=1
        time.sleep(1)
    print ("Fire in the hole")

countdown(int(input("enter the countdown lenght in seconds : ")))
