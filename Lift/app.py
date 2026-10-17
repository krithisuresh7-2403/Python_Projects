from lift_functions import lift_down, lift_up, open_lift

floors = [0,1,2,3]



    
if __name__ == "__main__":
    floors_clicked = []
    floors_clicked = open_lift(floors, floors_clicked)
    lift_up(floors,floors_clicked)
        
    
    