import mysql.connector


def read_password():
    file = open('password.txt', 'r')
    password = file.read().rstrip().lstrip()
    return password


def connect_to_stock_admin_db():
    print("\n[+] Connecting to the stocks' admin database...")
    db = mysql.connector.connect(
        host="185.212.70.52",
        user="u168617617_root",
        passwd="Lpahdbktm1:)",
        port="3306",
        database="u168617617_Stocks"
    )
    print("[+] Connected.")
    return db
