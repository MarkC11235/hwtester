import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1
# Load data from CSV "data1"
data1 = pd.read_csv("data1.csv")

# Delete the column named "to_be_deleted"
data1 = data1.drop("to_be_deleted", axis=1)

# Add two new columns
dt = 1  # time step in seconds
data1["fuel_consumed_total_kg"] = (data1["fuel_rate_kgps"] * dt).cumsum()
data1["travel_distance_m"] = (data1["speed_mph"] * 0.44704 * dt).cumsum()

# Plot accumulative fuel rate over travel distance
data1[["travel_distance_m", "fuel_consumed_total_kg"]].to_csv("data1_updated.csv", index=False)

# Save as a new CSV file "data1_updated"
data1.to_csv("data1_updated.csv", index=False)

# Task 2
# Create a new file, load data from two CSV files "data1" and "data2"
data1 = pd.read_csv("data1.csv")
data2 = pd.read_csv("data2.csv")

# Add two columns "fuel_rate_kgps" from two files and name the new column "fuel_rate_kps_two_vehicles"
data2["fuel_rate_kps_two_vehicles"] = data1["fuel_rate_kgps"] + data2["fuel_rate_kgps"]

# Save as "data2_updated"
data2.to_csv("data2_updated.csv", index=False)

# Task 3
class Bus:
    def __init__(self, gas_tank_gal, passenger_num):
        self.gas_tank_gal = gas_tank_gal
        self.passenger_num = passenger_num
        print(f"A bus object is constructed with {gas_tank_gal} gallons of fuel in the tank and {passenger_num} passengers on board.")

    def fill(self, gallons):
        self.gas_tank_gal += gallons
        print(f"{gallons} gallons of fuel is filled into the tank!\nThe bus currently has {self.gas_tank_gal} gallons of fuel in the tank and {self.passenger_num} passengers on board.")

    def drive(self, mpg, miles):
        fuel_used = miles / mpg
        self.gas_tank_gal -= fuel_used
        print(f"The bus travels {miles} miles!\nThe bus currently has {self.gas_tank_gal} gallons of fuel in the tank and {self.passenger_num} passengers on board.")

    def load(self, passengers):
        self.passenger_num += passengers
        print(f"{passengers} new passengers are loaded!\nThe bus currently has {self.gas_tank_gal} gallons of fuel in the tank and {self.passenger_num} passengers on board.")

    def offload(self, passengers):
        self.passenger_num -= passengers
        print(f"{passengers} passengers are offloaded!\nThe bus currently has {self.gas_tank_gal} gallons of fuel in the tank and {self.passenger_num} passengers on board.")

# Test the Bus class
z = Bus(30, 0)
z.load(15)
z.drive(8, 80)
z.offload(5)
z.fill(10)
