def military_standard ():
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

    return military_time

def display_military(military_time):
    print(f"You're military time is:\n{military_time[0]:02d}:{military_time[1]:02d}:{military_time[2]:02d}")
    if military_time[0] == 0:
        print("The standard time hour is 12 o'clock AM")
        military_time[0] = 12
    if military_time[0] > 12:
        military_time[0] -= 12
    print(f"In standard time, the time is:\n{military_time[0]:02d}:{military_time[1]:02d}:{military_time[2]:02d}")

def standard_military (am_pm):
    standard_time = [int(input("What hour? ")), int(input("What minute? ")), int(input("What second? "))]
    return standard_time

def time():
    am_pm = str.upper(input("Is the time in AM or PM: "))

def st_hour(am_pm, standard_time):
    if am_pm == "PM":
        military_hour = standard_time[0] + 12
    return military_hour

    return am_pm

def display_standard(standard_time, am_pm, military_hour):
    print(f"You're standard time is:\n{standard_time[0]:02d}:{standard_time[1]:02d}:{standard_time[2]:02d} {am_pm}")
    print(f"You're military time is {military_hour:02d}:{standard_time[1]:02d}:{standard_time[2]:02d}")

def main():
    again = "Y"
    print("This application is for turning military time to standard time or vise versa")
    while again == "Y":
        answer = str.upper(input("Are you starting in Military time of Standard time? Please write either MT or ST: "))
        while answer != "MT" and answer != "ST":
            print("This is not a valid input")
            answer = str.upper(input("Are you starting in Military time of Standard time? Please write either MT or ST: "))
        if answer == "MT":
            m = military_standard()
            display_military(m)
        elif answer == "ST":
            t = time()
            s = standard_military(t)
            x = st_hour(t, s)
            display_standard(s, t, x)
        again = str.upper(input("Would you like to convert another time? (Y/N) "))
    print("Thank you for using Military Time Converter")

main()