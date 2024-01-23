import PySimpleGUI as sg
import pandas as pd
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="SQL@2023",
    database="nprproject"
)
cursor = connection.cursor()

connection.commit()

xlFile = pd.read_excel("Registration_Info.xlsx")

def create_window(layout):
    sg.theme('SystemDefault')
    return sg.Window('Vehicle Registratioin' , layout)


def registration():
    fontt = 'Franklin 14'
    marginSpace = '    '
    midSpace = '                                            '
    layout = [
        [sg.Text("Enter information to register new vehicle", font = 'Franklin 20' , justification='center' , expand_x=True , pad=(10,10))],
        [sg.Text(midSpace),sg.Image('Images/Reg_img3.png')],
        [sg.Push(),sg.Text(' ' , font = '10')],
        [sg.Text(marginSpace),sg.Text("Name :" ,font = fontt, size=(15,1)) , sg.InputText(key='Name'),sg.Text(marginSpace)],
        [sg.Push(),sg.Text(' ' , font = '10')],
        [sg.Text(marginSpace),sg.Text("Vehicle Number :" , font = fontt , size=(15,1)) , sg.InputText(key='Vehicle_Number'),sg.Text(marginSpace)],
        [sg.Push(),sg.Text(' ' , font = '10')],
        [sg.Text(marginSpace),sg.Text("Tower Number : ", font = fontt , size = (15,1)) , sg.InputText(key='Tower_Number'),sg.Text(marginSpace)],
        [sg.Push(),sg.Text(' ' , font = '10')],
        [sg.Text(marginSpace),sg.Text("Flat Number :" , font = fontt , size = (15,1)) , sg.InputText(key='Flat_Number'),sg.Text(marginSpace)],
        [sg.Push(),sg.Text(' ' , font = '10')],
        [sg.Push(),sg.Button('Clear' , size=(20,2)),sg.Image('Images/clear.png')],
        [sg.Push(),sg.Button('Submit' , size=(20,2)),sg.Image('Images/upload.png')]
    ]
    window = create_window(layout)
    while True:
        event , values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
        if event == 'Submit':
          '''
          xlFile = pd.read_excel('Registration_Info.xlsx')
          values_df = pd.DataFrame.from_dict(values, orient='index').T
          xlFile = pd.concat([xlFile, values_df], ignore_index=True)
          #xlFile = xlFile.concat(values , ignore_index = True)
          xlFile.to_excel('Registration_Info.xlsx' , index=True)'''
          create_record(values['Name'],values['Vehicle_Number'],values['Flat_Number'],values['Tower_Number'],"Black")
          sg.popup("Vehicle Registered successfully !")
    
        if event == 'Clear':
          for key in values:
              window[key]('')


def delete_record():
    margin = '                       '
    sg.theme('SystemDefault')
    layout = [
        [sg.Text("Delete Record" , font='Franklin 20' , justification='center' , expand_x=True)],
        [sg.Text(' ' ,font = '20')],
        [sg.Text("Enter vehicle number: ", font='Franklin 14'),sg.InputText(key='Vehicle_Number')],
        [sg.Text(' ' ,font = '20')],
        [sg.Text(margin),sg.Button('Clear', size=(40,3))],
        [sg.Text(' ' ,font = '20')],
        [sg.Text(margin),sg.Button('Delete', size=(40,3)),sg.Image('Images/delete.png')]
    ]
    window = sg.Window('Delete Record' , layout)
    while True:
        event , values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Clear':
            for key in values:
              window[key]('')
        if event == 'Delete':
            xlFile = pd.read_excel('Registration_Info.xlsx')
            to_Delete = values['Vehicle_Number']
            xlFile = xlFile[xlFile['Vehicle_Number'] != to_Delete]
            xlFile.to_excel('RegistraTion_Info.xlsx' , index = False)
            sg.popup('Record Deleted Successfully')


def create_Admin_Window():
    sg.theme('SystemDefault')
    margin = '                     '
    buttonSize = (40,3)
    image_col = sg.Column([
        [sg.Image('Images/AdminPage1.png')]
    ])
    info_col = sg.Column([
        [sg.Text("Admin Page" , font='Franklin 40' , justification='center' , expand_x='True')],
        [sg.Text(' ' , size='40')],
        [sg.Text(margin+"                             "),sg.Image('Images/admin.png')],
        [sg.Text(margin),sg.Button('Register New Vehicle' , size=buttonSize),sg.Text(margin)],
        [sg.Text(' ' , size='40')],
        [sg.Text(margin),sg.Button('Delete Record', size=buttonSize),sg.Text(margin)],
        [sg.Text(' ' , size='40')],
        [sg.Text(margin),sg.Button('Show Entry Record', size=buttonSize),sg.Text(margin)],
        [sg.Text(' ' , size='40')],
        [sg.Text(margin),sg.Button('Show Exit Record' , size=buttonSize),sg.Text(margin)],
        [sg.Text(' ' , size='60')]
    ])
    layout = [
        [image_col , info_col]
    ]
    window = create_window(layout)
    while True:
        event , values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Register New Vehicle':
            registration()
        
        if event == 'Delete Record':
            delete_record()

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

def del_record(vehicle_number):
    # Delete record from the table
    delete_query = "DELETE FROM RegistrationInfo WHERE VehicleNumber = %s"
    values = (vehicle_number,)
    cursor.execute(delete_query, values)
    connection.commit()

# Example usage
#create_record("John Doe", "ABC123", "101", "A", "Blue")


# Close the cursor and connection


create_Admin_Window()

cursor.close()
connection.close()
