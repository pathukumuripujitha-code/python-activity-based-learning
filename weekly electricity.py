
# Weekly Electricity Consumption Matrix

appliances = ["Fan", "Light", "TV", "AC"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Electricity consumption in units (kWh)
readings = [
    [2, 2, 3, 2, 2, 3, 2],
    [1, 1, 1, 1, 1, 2, 1],
    [3, 2, 3, 3, 4, 3, 2],
    [8, 9, 10, 12, 11, 13, 9]
]

daily_limit = 15
appliance_limit = 60

print("Weekly Electricity Consumption Matrix")
print("Appliance", *days, "Total")

appliance_totals = []

for i in range(len(appliances)):
    total = sum(readings[i])
    appliance_totals.append(total)
    print(appliances[i], *readings[i], total)

daily_totals = []

for j in range(len(days)):
    total = 0
    for i in range(len(appliances)):
        total += readings[i][j]
    daily_totals.append(total)

print("\nDaily Consumption Totals:")
for j in range(len(days)):
    print(days[j], ":", daily_totals[j], "units")

print("\nAppliance-wise Totals:")
for i in range(len(appliances)):
    print(appliances[i], ":", appliance_totals[i], "units")

print("\nChecking Daily Limits:")
for j in range(len(days)):
    if daily_totals[j] > daily_limit:
        print(days[j], "exceeds the daily limit!")

print("\nChecking Appliance Limits:")
for i in range(len(appliances)):
    if appliance_totals[i] > appliance_limit:
        print(appliances[i], "exceeds the weekly limit!")

highest = appliance_totals.index(max(appliance_totals))
print("\nHighest Consumption Appliance:", appliances[highest])
print("Total Weekly Consumption:", sum(appliance_totals), "units")
