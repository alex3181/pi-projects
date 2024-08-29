import datetime


def run():
    # Get the current time and day
    current_time = datetime.datetime.now().time()
    current_day = datetime.datetime.today()

    # Define the time range
    start_time = datetime.time(9, 30)  # 0930 Start of market
    end_time = datetime.time(16, 1)  # 1600 End of market

    print("Start time", start_time)
    print("Now time", current_time)
    print("End time", end_time)

    # Check if current time is between 9:30 AM and 16:01 PM
    if (start_time <= current_time <= end_time) and (current_day.weekday() < 5):
        print("Now time", current_time)


if __name__ == "__main__":
    run()
