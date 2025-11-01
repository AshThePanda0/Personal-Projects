print("This application is for turning military time to standard time or vise versa")
answer = str.upper(input("Are you starting in Military time of Standard time? Please write either MT or ST"))
while answer != "MT" or answer != "ST":
    print("This is not a valid imput")
    answer = str.upper(input("Are you starting in Military time of Standard time? Please write either MT or ST"))

def milirary_standard ():
    military_time = [int(input("What hour? ")), int(input("What minute? ")), int(input("What second? "))]
    while military_time[0] > 24:
        print("Invalid hours")
        military_time[0] = int(input("What hour? "))

    while military_time[1] >= 60:
        print("Invalid minutes")
        military_time[1] = int(input("What minute? "))

    while military_time[2] >= 60:
        print("Invalid seconds")
        military_time[2] = int(input("What second? "))

    if military_time[0] > 12:
        regular_hour = military_time[0] - 12
    elif military_time[0] <= 12:
        regular_hour = military_time[0]

def display_military(military_time):
    print(f"You're military time is:\n{military_time[0]:02d}:{military_time[1]:02d}:{military_time[2]:02d}")
    if military_time[0] == 0:
        print("The standard time hour is 12 o'clock AM")
        regular_hour = 12
    print(f"In standard time, the time is:\n{regular_hour:02d}:{military_time[1]:02d}:{military_time[2]:02d}")

def standard_military ():
    am_pm = str.upper(input("Is the time in AM or PM"))
    standatd_time = [int(input("What hour? ")), int(input("What minute? ")), int(input("What second? "))]


def display_standard(standard_time, am_pm):
    print(f"You're standard time is:\n{standard_time:02d}{am_pm}")