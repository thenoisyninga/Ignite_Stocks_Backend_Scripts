from db_connection import connect_to_stock_admin_db


def set_all_values_to_0():
    db = connect_to_stock_admin_db()

    mycursor = db.cursor()

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('Military', 1);"
    print(query)
    mycursor.execute(query)

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('Auto', 1);"
    print(query)
    mycursor.execute(query)

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('FoodAgriculture', 1);"
    print(query)
    mycursor.execute(query)

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('Infrastructure', 1);"
    print(query)
    mycursor.execute(query)

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('Pharmaceutical', 1);"
    print(query)
    mycursor.execute(query)

    query = f"INSERT INTO assetvalues(IndustryName, AssetValue)VALUES('Power', 1);"
    print(query)
    mycursor.execute(query)

    db.commit()
