import datetime

def calculateLivedfor():
    try:
        year = int(input("Print Your Born Year: "))
        month = int(input("Print Your Born Month (1-12): "))
        day = int(input("Print Your Born Day: "))
        MyBirthDay = datetime.datetime(year, month, day)
    except ValueError:
        print("Please enter valid integer values for year, month, and day.")
        return
    
    datenow = datetime.datetime.now()
    delta = datenow - MyBirthDay

    unit = input("Please Choose Time Unit: Year, Month, Week, Day, Hour, Seconds: ").strip().lower()

    if unit in ["year", "y"]:
        print(f"You have lived for {delta.days // 365} years.")
    elif unit in ["month", "m"]:
        print(f"You have lived for {delta.days // 30} months.")
    elif unit in ["week", "w"]:
        print(f"You have lived for {delta.days // 7} weeks.")
    elif unit in ["day", "d"]:
        print(f"You have lived for {delta.days} days.")
    elif unit in ["hour", "h"]:
        print(f"You have lived for {int(delta.total_seconds() // 3600)} hours.")
    elif unit in ["second", "s"]:
        print(f"You have lived for {int(delta.total_seconds())} seconds.")
    else:
        print("Invalid time unit. Please try again.")

calculateLivedfor()