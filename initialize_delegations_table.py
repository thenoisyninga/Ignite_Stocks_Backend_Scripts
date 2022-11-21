import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from db_connection import connect_to_stock_admin_db


def migrate_data_from_firebase_to_stocks_db():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    print("[+] Connecting to the Firebase database...")
    db = firestore.client()

    print("[+] Reading Data from Firestore..")
    del_passwords = db.collection('delegations_list').order_by("Delegation_Number").get()

    pass_list = []
    del_list = []

    print("[+] Parsing that data...")
    for i in del_passwords:
        i = i.to_dict()
        password = i["Password"]
        pass_list.append(password)

        del_id = i["Delegation_Number"]
        del_list.append(del_id)
    db.close()

    db = connect_to_stock_admin_db()
    my_cursor = db.cursor()

    print("[+] Writing to the SQL database...")
    for count in range(0,1):
        query = f"INSERT INTO delegations(DelID, Pass, IsLoggedIn, ICs) VALUES('{del_list[count]}', '{pass_list[count]}', 0, 5000);"
        print(query)
        my_cursor.execute(query)

    db.commit()
    db.close()

    print("[+] Dunn :p")