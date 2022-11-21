import time

from add_test_users import add_test_users
from db_connection import connect_to_stock_admin_db
from initalize_assetsOwned_table import initialize_all_owned_assets
from initialize_assetvalues_table import set_all_values_to_0
from initialize_delegations_table import migrate_data_from_firebase_to_stocks_db

print("\n\n=======================================================================")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("       WELCOME TO IGNITE STOCK MARKET ADMIN CONTROLS © Sarim Ahmed")
print("=======================================================================\n\n")

# Groups Lists

groupA1List = [
    '29',
    '31',
    '08',
    '34',
    '47',
    '46',
    '43',
    '01',
    '11',
    '14',
    '49',
    '38',
    '25',
]
groupA2List = [
    '45',
    '12',
    '10',
    '33',
    '26',
    '02',
    '42',
    '15',
    '04',
    '50',
    '07',
    '32',
]
groupB1List = [
    '17',
    '06',
    '27',
    '05',
    '39',
    '35',
    '40',
    '37',
    '36',
    '30',
    '23',
    '44',
]
groupB2List = [
    '21',
    '41',
    '18',
    '16',
    '13',
    '09',
    '28',
    '48',
    '03',
    '20',
    '22',
    '19',
    '24',
]
running = True

while running:
    try:
        print("\n\nOptions..")
        print("[1] Initialise all Stock Market Values.")
        print("[2] Set a delegation's login flag to 0.")
        print("[3] Log out all delegations.")
        print("[4] Check how many people are logged in.")
        print("[5] Open the Stock Market (Allow Logins).")
        print("[6] Close the Stock Market (Block All Logins).")
        print("[7] Change a Delegation's ICs hahahahahahahahahaha.")
        print("[8] Set Group A1 Logins to 0.")
        print("[9] Set Group A2 Logins to 0.")
        print("[10] Set Group B1 Logins to 0.")
        print("[11] Set Group B2 Logins to 0.")
        print("[12] Set All Logins to 1.")
        print("[13] Set all owned assets to 0.")
        print("[14] Set all asset values to 1 IC.")
        print("[15] Copy passwords and ids from firestore database to stocks database.")
        print("[16] Delete Users and repopulate with test data.")
        print("[99] Quit Program.")

        option = input("\nEnter your choice: ")

        time.sleep(1)

        if int(option) == 1:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            option = input("Are you sure? (Y/n): ")
            if option == 'Y':
                print("\n[+] Setting all ICs to 600...")
                query = f"UPDATE `delegations` SET `ICs`='600' WHERE 1"
                my_cursor.execute(query)
                db.commit()

                print("\n>>>>>>> Ressetting all owned stocks to 0...\n")
                time.sleep(2)
                query = f"UPDATE `assetsowned` SET `Military`=0,`Auto`=0,`FoodAgriculture`=0,`Infrastructure`=0,`Pharmaceutical`=0,`Power`=0 WHERE 1"
                my_cursor.execute(query)
                db.commit()
            else:
                print("\n[-] Values weren't initialised.")
        elif int(option) == 2:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            id = input("\nEnter the Delegation ID to log out: ")
            query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE DelID = '{id}';"
            my_cursor.execute(query)
            db.commit()
            print(f"\n>>>>>>> Delegation {id} was logged out.\n")
            time.sleep(2)
        elif int(option) == 3:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            option = input("Are you sure? (Y/n): ")
            if option.lower() == 'y':
                query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE true;"
                my_cursor.execute(query)
                db.commit()
                print(f"\n>>>>>>> All delegations were logged out.\n")
                time.sleep(2)
        elif int(option) == 4:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            query = f"SELECT COUNT(IsLoggedIn) FROM delegations WHERE IsLoggedIn = true;"
            my_cursor.execute(query)
            for x in my_cursor:
                count = x[0]
            print(f"\n>>>>>>> {count} delegations are logged in.\n")
            time.sleep(2)
        elif int(option) == 5:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            query = f"UPDATE `permission` SET `Allowed`= true WHERE Permission = 'RoundLive';"
            my_cursor.execute(query)
            db.commit()
            print(f"\n>>>>>>> Logins Allowed, Make sure to block them after testing.\n")
            time.sleep(2)
        elif int(option) == 6:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            query = f"UPDATE `permission` SET `Allowed`= false WHERE Permission = 'RoundLive';"
            my_cursor.execute(query)
            db.commit()
            print(f"\n>>>>>>> Logins Blocked.\n")
            time.sleep(2)
        elif int(option) == 7:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()

            DelID = input("Enter the Delegation ID: ")

            query = f"SELECT `ICs` FROM `delegations` WHERE DelID = '{DelID}';"
            my_cursor.execute(query)
            for x in my_cursor:
                gotICs = x[0]
                print(gotICs)

            print(f"Delegation {DelID} has {gotICs} ICs currently...")
            time.sleep(1)
            ICs = int(input("Enter the number of ICs you want to add: "))
            ICs = ICs + gotICs
            print(ICs)
            query = f"UPDATE `delegations` SET `ICs`= {ICs} WHERE DelID = '{DelID}';"
            my_cursor.execute(query)
            db.commit()
            time.sleep(1)
            print(f"Delegation {DelID} now has {ICs} ICs.")
        elif int(option) == 8:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            for delNum in groupA1List:
                query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE DelID = '{delNum}';"
                my_cursor.execute(query)
            db.commit()
            print("[+] Flags 0 for A1 set.")
        elif int(option) == 9:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            for delNum in groupA2List:
                query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE DelID = '{delNum}';"
                my_cursor.execute(query)
            db.commit()
            print("[+] Flags 0 for A2 set.")
        elif int(option) == 10:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            for delNum in groupB1List:
                query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE DelID = '{delNum}';"
                my_cursor.execute(query)
            db.commit()
            print("[+] Flags 0 for B1 set.")
        elif int(option) == 11:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            for delNum in groupB2List:
                query = f"UPDATE `delegations` SET `IsLoggedIn`= false WHERE DelID = '{delNum}';"
                my_cursor.execute(query)
            db.commit()
            print("[+] Flags 0 for B2 set.")
        elif int(option) == 12:
            db = connect_to_stock_admin_db()
            my_cursor = db.cursor()
            query = f"UPDATE `delegations` SET `IsLoggedIn`= true WHERE true;"
            my_cursor.execute(query)
            db.commit()
            print("[+] Flags 1 for All set.")
        elif int(option) == 13:
            initialize_all_owned_assets()
        elif int(option) == 14:
            set_all_values_to_0()
        elif int(option) == 15:
            migrate_data_from_firebase_to_stocks_db()
        elif int(option) == 16:
            add_test_users()
        elif int(option) == 99:
            running = False
        else:
            print("\n[-] Your choice doesnt exist :p")
        time.sleep(1)
    except:
        print("[+] Error Occurred")

    print(
        "--------------------------------------------------------------------------------------------------------------------\n\n\n\n")


