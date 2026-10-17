def lift_up(floors, floors_clicked):
    for i in floors:
        if i in floors_clicked:
            print(f"Welcome to floor {i}")
            floors_clicked.remove(i)
            floors_clicked = open_lift(floors, floors_clicked)
            if i == 3:
                lift_down(floors, floors_clicked)
            else:
                lift_up(floors, floors_clicked)

def open_lift(floors, floors_clicked):
    passenger_count = int(input("Enter the number of passengers entering: "))
    for i in range(passenger_count):
        user_req = int(input("Enter the floor you wnat to go: "))
        if user_req in floors and user_req not in floors_clicked:
            floors_clicked.append(user_req)
    return floors_clicked  
      

def lift_down(floors, floors_clicked):
    for i in floors[::-1]:
        if i in floors_clicked:
            print(f"Welcome to floor {i}")
            floors_clicked.remove(i)
            floors_clicked = open_lift(floors, floors_clicked)
            