import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="SQL@2023",
    database="nprproject"
)

# Create a cursor object
cursor = connection.cursor()

connection.commit()

def create_record(owner_name, vehicle_number, flat_no, tower_no, car_color):
    # Insert record into the table
    insert_query = "INSERT INTO RegistrationInfo (OwnerName, VehicleNumber, FlatNo, TowerNo, CarColor) VALUES (%s, %s, %s, %s, %s)"
    values = (owner_name, vehicle_number, flat_no, tower_no, car_color)
    cursor.execute(insert_query, values)
    connection.commit()

def read_records():
    # Select all records from the table
    select_query = "SELECT * FROM RegistrationInfo"
    cursor.execute(select_query)
    records = cursor.fetchall()
    for record in records:
        print(record)

def update_record(vehicle_number, new_owner_name):
    # Update record in the table
    update_query = "UPDATE RegistrationInfo SET OwnerName = %s WHERE VehicleNumber = %s"
    values = (new_owner_name, vehicle_number)
    cursor.execute(update_query, values)
    connection.commit()

def delete_record(vehicle_number):
    # Delete record from the table
    delete_query = "DELETE FROM RegistrationInfo WHERE VehicleNumber = %s"
    values = (vehicle_number,)
    cursor.execute(delete_query, values)
    connection.commit()

# Example usage
#create_record("John Doe", "ABC123", "101", "A", "Blue")
create_record("Avika Shudhanshu Maurya" , "UP32HG9809" , "B415" , "5" , "Kaali")


# Close the cursor and connection
cursor.close()
connection.close()