#I used a local DB for testing purpose
dbConnection = "PATH_TO_DB"


def getCustomer(customer_id):
    import sqlite3
    connection = sqlite3.connect(dbConnection)
    c = connection.cursor()
    c.execute("SELECT customer_id, discount, price_service_A, price_service_B, price_service_C, free_days FROM customer WHERE customer_id = (?) ", (customer_id,))
    customer = c.fetchall()
    obj = {
            "customer_id": customer[0][0],
            "discount": customer[0][1],
            "price-A": customer[0][2],
            "price-B": customer[0][3],
            "price-C": customer[0][4],
            "free_days": customer[0][5]
    }
    connection.commit()
    c.close()
    return obj


def updateFreeDays(customer_id, amount):
    import sqlite3
    connection = sqlite3.connect(dbConnection)
    c = connection.cursor()
    c.execute("UPDATE customer set free_days = (?) WHERE customer_id = (?)", (amount, customer_id,))
    connection.commit()
    c.close()


def insertStartDate(customer_id,date, service=None):
    import sqlite3
    connection = sqlite3.connect(dbConnection)
    c = connection.cursor()
    c.execute(f"INSERT INTO service_{service} (customer_id, start_date) VALUES (?,?)",(customer_id,date))
    connection.commit()
    c.close()
