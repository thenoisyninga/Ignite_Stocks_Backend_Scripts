from db_connection import connect_to_stock_admin_db


def initialize_all_owned_assets():
    db = connect_to_stock_admin_db()
    my_cursor = db.cursor()

    for del_id in range(1, 51):
        del_id = int(del_id)
        if int(del_id) == 1:
            del_id = "01"
        if int(del_id) == 2:
            del_id = "02"
        if int(del_id) == 3:
            del_id = "03"
        if int(del_id) == 4:
            del_id = "04"
        if int(del_id) == 5:
            del_id = "05"
        if int(del_id) == 6:
            del_id = "06"
        if int(del_id) == 7:
            del_id = "07"
        if int(del_id) == 8:
            del_id = "08"
        if int(del_id) == 9:
            del_id = "09"

        query = f"INSERT INTO assetsowned(DelID, Military, Auto, FoodAgriculture, Infrastructure, Pharmaceutical, Power) VALUES('{del_id}', 0, 0, 0, 0, 0, 0);"
        print(query)
        my_cursor.execute(query)

    db.commit()
