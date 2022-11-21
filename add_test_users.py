from db_connection import connect_to_stock_admin_db


def add_test_users():
    db = connect_to_stock_admin_db()
    my_cursor = db.cursor()

    print("> All previous user data will be deleted if you proceed.")
    option = input("Proceed? (Y/n): ")

    if option.lower() == 'y':

        # Delete all rows from delegations
        print("[+] Clearing table delegations...")
        query = "DELETE FROM delegations WHERE 1"
        my_cursor.execute(query)
        db.commit()

        # Delete all rows from assetsowned
        print("[+] Clearing table assetsowned...")
        query = "DELETE FROM assetsowned WHERE 1"
        my_cursor.execute(query)
        db.commit()


        print("> How many users do you want to add?")
        num = int(input(": "))

        for i in range(1, num + 1):
            query = f"INSERT INTO `delegations`(`DelID`, `Pass`, `IsLoggedIn`, `ICs`) VALUES ('{i}','1234','0','600')"
            my_cursor.execute(query)
            db.commit()

            query = f"INSERT INTO `assetsowned`(`DelID`, `Military`, `Auto`, `FoodAgriculture`, `Infrastructure`, `Pharmaceutical`, `Power`) VALUES ('{i}','0','0','0','0','0','0')"
            my_cursor.execute(query)
            db.commit()

            print(f"[+] Created {i} test users")