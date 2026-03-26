HOT_DAY_THRESHOLD = 30
ALERT_THRESHOLD = 40


def find_temperature_bounds(temperatures):
    return max(temperatures), min(temperatures)


def count_hot_days(temperatures, threshold):
    return sum(1 for temp in temperatures if temp > threshold)


def run_alert_system(temperatures, hot_day_threshold, alert_threshold):
    hot_days_count = 0

    for day, temperature in enumerate(temperatures, start=1):
        if temperature >= alert_threshold:
            print(f"Hot Days before alert: {hot_days_count}")
            print(f"Alert! Extreme temperature {temperature}°C detected on Day {day}")
            return

        if temperature > hot_day_threshold:
            hot_days_count += 1


def main():
    temperatures = [28, 32, 35, 29, 31, 27, 30]

    print("===== Task 1: Find Maximum and Minimum =====")
    max_temp, min_temp = find_temperature_bounds(temperatures)
    print(f"Maximum Temperature: {max_temp}°C")
    print(f"Minimum Temperature: {min_temp}°C")

    print("\n===== Task 2: Count Hot Days =====")
    temperatures = [28, 32, 35, 29, 31, 27, 30]
    hot_days_count = count_hot_days(temperatures, HOT_DAY_THRESHOLD)
    print(f"Hot Days (>30°C): {hot_days_count}")

    print("\n===== Task 3: Alert System =====")
    temperatures = [28, 32, 35, 40, 31, 33, 30]
    run_alert_system(temperatures, HOT_DAY_THRESHOLD, ALERT_THRESHOLD)

if __name__ == "__main__":
    main()
