
# Food Supply Chain Stock Reconciliation

locations = {
    "Location A": {
        "received": 500, "distributed": 300,
        "damaged": 20, "recorded_stock": 175
    },
    "Location B": {
        "received": 400, "distributed": 250,
        "damaged": 10, "recorded_stock": 140
    },
    "Location C": {
        "received": 600, "distributed": 350,
        "damaged": 25, "recorded_stock": 220
    }
}

minimum_stock = 150
total_received = 0
total_distributed = 0
total_damaged = 0
total_remaining = 0

print("FOOD SUPPLY CHAIN STOCK REPORT")
print("-" * 40)

for location, data in locations.items():
    received = data["received"]
    distributed = data["distributed"]
    damaged = data["damaged"]
    recorded = data["recorded_stock"]

    expected = received - distributed - damaged
    discrepancy = recorded - expected
    replenishment = max(0, minimum_stock - recorded)

    total_received += received
    total_distributed += distributed
    total_damaged += damaged
    total_remaining += recorded

    print("\nLocation:", location)
    print("Received:", received)
    print("Distributed:", distributed)
    print("Damaged:", damaged)
    print("Expected Stock:", expected)
    print("Recorded Stock:", recorded)
    print("Discrepancy:", discrepancy)
    print("Replenishment Required:", replenishment)

    if discrepancy == 0:
        print("Status: Stock Matched")
    else:
        print("Status: Stock Mismatch")

print("\nOVERALL SUMMARY")
print("Total Received:", total_received)
print("Total Distributed:", total_distributed)
print("Total Damaged:", total_damaged)
print("Total Recorded Stock:", total_remaining)
print("Total Expected Stock:",
      total_received - total_distributed - total_damaged)
print("Total Replenishment:",
      sum(max(0, minimum_stock - d["recorded_stock"])
          for d in locations.values()))
