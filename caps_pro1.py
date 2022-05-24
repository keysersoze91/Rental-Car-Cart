ListRental = [
    {
        'CarID' : '1',
        'Car_Name' : 'Nissan Skyline',
        'Plate_Number' : 'B2233DAK',
        'Region' : 'Jakarta',
        'Available' : 'Yes',
    },
    {
        'CarID' : '2',
        'Car_Name' : 'Toyota Supra',
        'Plate_Number' : 'D8651POP',
        'Region' : 'Bandung',
        'Available' : 'No',
    },
    {
        'CarID' : '3',
        'Car_Name' : 'Porsche Cayman',
        'Plate_Number' : 'B666DVL',
        'Region' : 'Jakarta',
        'Available' : 'Yes',
    }
]

# -- MAIN MENU--
def Menu():
    while True:
        MainMenu = input('''
        ====== WELCOME TO OMBOMBOM RENT CAR =====

        1. SHOW CAR
        2. ADD NEW CAR
        3. UPDATE CAR
        4. REMOVE CAR
        5. QUIT

        PLEASE CHOOSE OR DIE : ''')
        
        if (MainMenu == '1'):
            show_all()
        elif (MainMenu == '2'):
            new_car()
        elif (MainMenu == '3'):
            update_car()
        elif (MainMenu == '4'):
            del_car()
        elif (MainMenu == '5'):
            print('--- Thank you for using this apps ---\n')
            break

# -- MENU 1 Read all--

def view_all_car():
    if ListRental==[]:
        print('\n\t=== OUR RENT CAR ===\n')
        print('CarID\t| Car Name\t\t| Plate Number\t| Region\t| Available\t')
        print(' --- No Existing Car ---')
    else:
        print('\n\t=== OUR RENT CAR ===\n')
        print('CarID\t| Car Name\t\t| Plate Number\t| Region\t| Available\t')
        for i in range(len(ListRental)):
            print('{}\t| {}     \t| {}\t| {}\t| {}\t'.format(ListRental[i]['CarID'],ListRental[i]['Car_Name'],ListRental[i]['Plate_Number'],ListRental[i]['Region'],ListRental[i]['Available']))
    
def show_all():
    while True:
        ChRead=input('''
        === Rent Car OmBOmBOm ===
        1. View All Rent Car
        2. Choose your Rent Car
        3. Back to Main Menu

        Please Choose or Die: ''')

        if (ChRead=='1'):
            view_all_car()

        elif (ChRead=='2'):
            SpecShow=input('\n\tInput Your CarID :') 
            find=False
            for i in range(len(ListRental)):
                if ListRental[i]['CarID'] == SpecShow:
                    print('CarID\t| Car Name\t\t| Plate Number\t| Region\t| Available\t')
                    print('{}\t| {}     \t| {}\t| {}\t| {}\t'.format(ListRental[i]['CarID'],ListRental[i]['Car_Name'],ListRental[i]['Plate_Number'],ListRental[i]['Region'],ListRental[i]['Available']))          
                    find=True
            if find == False:
                print('--- No Existing Car ---')
                show_all()

        elif (ChRead=='3'):
            break
            

# -- Menu 2 tambah data baru --

def input_car():
    while True:
        global carid
        carid = input('Input NEW car id :')
        if any(d['CarID'] == carid for d in ListRental):
            print('Car ID already Exist')
        else:
          break

    global carname
    carname=input('Input a name of car :')
    
    while True:
        global platenum
        platenum=input('Input new Plate Number :')
        if any(d['Plate_Number'] == platenum for d in ListRental):
            print('Plate Number already Exist')
        else:
          break

    global region
    region=input('Input new Region :')
    
    global avail
    avail=input('Input Available (yes/no):')
    return

def add_car():
    ListRental.append({
        'CarID' : carid,
        'Car_Name' : carname,
        'Plate_Number' : platenum,
        'Region' : region,
        'Available' : avail
    })
    
def new_car():
    while True:
        pil_new=input('''
        === Rent Car OmBOmBOm ===
        1. Add New Car
        2. Back To Main Menu

        Please Choose or DIe:''')

        if(pil_new=='1'):
            find_new = input('Input your CarID :')
            if not any(d['CarID'] == find_new for d in ListRental):
                input_car()
                save_car = input('Do you want to save the car (y/n):')
                if save_car == "Y" or save_car == "y":
                    add_car()
                    print('--- Your car has been added --')
                elif save_car == "N" or save_car == "n":
                    new_car()
            else:
                print('--- You already had a car ---')
            
        else:
            break

# -- Menu 3 Update --

def update_car():
    while True:
        pil_up = input('''
        === Rent Car OmBomBom ===
        1. Update current car
        2. Back to main menu
        
        Please Choose :''')

        if (pil_up == '1'):
            find_up = input('Input your car id :') 
            find=False
            for i in range(len(ListRental)):
                if ListRental[i]['CarID'] == find_up:
                    print('CarID\t| Car Name\t\t| Plate Number\t| Region\t| Available\t')
                    print('{}\t| {}     \t| {}\t| {}\t| {}\t'.format(ListRental[i]['CarID'],ListRental[i]['Car_Name'],ListRental[i]['Plate_Number'],ListRental[i]['Region'],ListRental[i]['Available']))          
                    find=True
            if find == False:
                print('Your car not found')
            ch_up= input('Do you want to continue update the car (y/n) :')
            if ch_up == 'Y' or ch_up == 'y':
                up_item = input('Input data you want to change :')
                up_value = input('Input value data you want to change :')
                for i in ListRental:
                    if i["CarID"] == find_up:
                        i[up_item]=up_value
                        print('Your data has changed')
            elif ch_up == 'N' or ch_up == 'n':
                update_car()
        else:
            break
    
# -- Menu 4 delete --

def del_car():
    while True:
        pil_del = input('''
        === Rent Car OmBOmBOm ===
        1. Remove Current Car
        2. Back to main menu

        Please Choose :''')

        if (pil_del=='1'):
            find_del = input('Input your car id :') 
            find=False
            for i,v in enumerate(ListRental):
                if ListRental[i]['CarID'] == find_del:
                    print('CarID\t| Car Name\t\t| Plate Number\t| Region\t| Available\t')
                    print('{}\t| {}     \t| {}\t| {}\t| {}\t'.format(ListRental[i]['CarID'],ListRental[i]['Car_Name'],ListRental[i]['Plate_Number'],ListRental[i]['Region'],ListRental[i]['Available']))          
                    find=True
                    rem_car = input('\nAre you sure for remove the car (y/n) :')
                    if rem_car == 'Y' or rem_car == 'y':
                        ListRental.pop(i)
                        print('--- Your car has been removed ---')                
                    elif rem_car == 'N' or rem_car == 'n':
                        del_car()
            if find == False:
                print('--- Your car not found ---')       
        else:
            break
                
Menu()