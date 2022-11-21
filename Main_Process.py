# Credits:
#
# Created By Hamza Khurram.
# Upgraded By Sarim Ahmed.


from datetime import *
from time import *

from db_connection import connect_to_stock_admin_db

print("\n\n")

# This is the time at which the round is scheduled to start
startTime = datetime(year=2022, month=10, day=26, hour=14, minute=28)

# This is the number of minutes after which the values are updated...
value_change_time_in_minutes = 1

# Group A
# Timeline for the prices...
prices = [
    [4, 1, 1000, 10, 9, 8, 8, 1, 100, 15, 15, 50000],  # Military Timeline
    [4, 5, 1, 2, 6, 7, 6, 7, 9, 4, 5, 1],  # Auto Timeline
    [3, 2, 3, 5, 6, 7, 8, 2, 1, 2, 3, 1],  # Food-Agriculture Timeline
    [5, 6, 8, 9, 3, 1, 2, 29, 9, 15, 2, -400],  # Construction Timeline
    [8, 3, 4, 1, 4, 5, 6, 7, 8, 3, 4, 1],  # Health Timeline
    [1, 2, 3, 4, 3, 5, 4, 7, 8, 7, 800, -16000]  # Power Timeline
    # ------------------------------------------> increase in time
]

# Group B
# Timeline for the prices...
# prices = [
#     [23, 1, 3, 10, 9, 8, 8, 1, 100, 15, 15, 50000],  # Military Timeline
#     [4, 5, 1, 2, 6, 7, 6, 7, 9, 4, 5, 1],  # Auto Timeline
#     [3, 2, 3, 5, 6, 7, 8, 2, 1, 2, 3, 1],  # Food-Agriculture Timeline
#     [5, 6, 8, 9, 3, 1, 2, 29, 9, 15, 2, -400],  # Construction Timeline
#     [8, 3, 4, 1, 4, 5, 6, 7, 8, 3, 4, 1],  # Health Timeline
#     [1, 2, 3, 4, 3, 5, 4, 7, 8, 7, 800, -16000]  # Power Timeline
#     # ------------------------------------------> increase in time
# ]

print("===============================================================")
print("                       Program Started! ")
print("===============================================================\n\n")

print("Woah i am alive.")

print("[+] Initializing things...")


def show_data():
    mycursor.execute("SELECT * FROM assetvalues")
    print("\n")
    print("\n")
    print("\n")
    print(f"Stock Values at the moment...")
    for x in mycursor:
        print(f"[-] {x[0]}'s Cost: {x[1]}")


def tick():
    global startTime
    current_time = datetime.now()
    time_since_start = (current_time - startTime)
    total_seconds = time_since_start.seconds
    minutes = int(total_seconds / 60)
    d_years = int(minutes / value_change_time_in_minutes)
    return d_years


def update_prices(time_delta):
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[0][time_delta]} WHERE IndustryName = 'Military'")
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[1][time_delta]} WHERE IndustryName = 'Auto'")
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[2][time_delta]} WHERE IndustryName = 'FoodAgriculture'")
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[3][time_delta]} WHERE IndustryName = 'Infrastructure'")
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[4][time_delta]} WHERE IndustryName = 'Pharmaceutical'")
    mycursor.execute(f"UPDATE assetvalues SET AssetValue = {prices[5][time_delta]} WHERE IndustryName = 'Power'")
    db.commit()


while True:
    currentTime = datetime.now()
    if startTime <= currentTime:
        break
    else:
        print(f"\n[-] Round Not Started yet..\n[-] Scheduled to start at {startTime}.")
        print("Ruko zara.. Sabar karo :/")
        sleep(5)

cont = True

print("\n===>>>  It's time 0_0...")

db = connect_to_stock_admin_db()

print("[+] Connection Successful Boii\n")

mycursor = db.cursor()
mycursor.execute(f"UPDATE permission SET Allowed = true WHERE Permission = 'RoundLive'")
print("===============================================================")
print("======= Stock Exchange Round Started: LOGINS ARE LIVE! =======")
print("======= Stock Exchange Round Started: LOGINS ARE LIVE! =======")
print("======= Stock Exchange Round Started: LOGINS ARE LIVE! =======")
print("======= Stock Exchange Round Started: LOGINS ARE LIVE! =======")
print("======= Stock Exchange Round Started: LOGINS ARE LIVE! =======")
print("===============================================================")

while cont:
    # startYear = 2020
    # currentYear = 2020
    delta = tick()
    if delta >= len(prices[0]):
        print("\n\n[+] Time up!")
        mycursor.execute(f"UPDATE permission SET Allowed = false WHERE Permission = 'RoundLive'")
        db.commit()
        print("[+] Logins Closed!!!")
        print("===============================================================")
        print("================== Stock Exchange Round Over! =================")
        print("================== Stock Exchange Round Over! =================")
        print("================== Stock Exchange Round Over! =================")
        print("================== Stock Exchange Round Over! =================")
        print("===============================================================")
        print("\nGood job me!")
        print("Now I die.")
        cont = False

    if cont:
        update_prices(delta)
        show_data()
        sleep(5)
