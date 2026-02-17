print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

for i in range(len(temperatures)):
    if i == 0:
        max_temp = temperatures[i]
        min_temp = temperatures[i]
    else:
        if temperatures[i] > max_temp:
            max_temp = temperatures[i]
        if temperatures[i] < min_temp:
            min_temp = temperatures[i]

print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days_count = 0

for i in range(len(temperatures)):
    if temperatures[i] > 30:
        hot_days_count += 1

print(f"Hot Days (>30°C): {hot_days_count}")

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days_count = 0

for i in range(len(temperatures)):

   

    if temperatures[i] >= 40:
        print(f"Hot Days before alert: {hot_days_count}")
        print(f"Alert! Extreme temperature {temperatures[i]}°C detected on Day {i+1}")
        break;

    if temperatures[i] > 30:
        hot_days_count +=1