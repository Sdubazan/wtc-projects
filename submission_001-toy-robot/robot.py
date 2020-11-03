

# TODO: Decompose into functions

def move_square():
    """
    funtion responsible for square movements
    """
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
    
def move_rectangle():
    """
    function responsible for rectanguler movements
    """
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
    
def move_circle():
    """
    function responsible for circle movements
    """
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
    
def square_dencing():
    """
    function responsible for dencing in squares movement
    """
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            degrees = 90
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")
           
    
def crop_circle():
    """
    function for crop circle movement
    """
    print("Crop circles - 4 circles")
    degrees = 1
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        for k in range(360):
            length = 1
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")

def move():
    """
    basic_robot_moves(), specifies the basic moviments the bot can move.
    """ 

    move_square()
    move_rectangle()
    move_circle()
    square_dencing()
    crop_circle()
    
def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
