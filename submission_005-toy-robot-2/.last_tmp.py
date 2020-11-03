def robot_name():
    """ function used to set robot name """
    set_name = input('What do you want to name your robot? ')
    if len(set_name) == 0:
        return robot_name()
    return set_name

def print_out(r_name,text):
    print(r_name+': '+text)

def get_command_input(r_name):
    """function to get robot name"""

    command_input = input('{}: What must I do next? '.format(r_name))
    if len(command_input) == 0 or not command_not_valid(command_input):
        print('{}: Sorry, I did not understand \'{}\'.'.format(r_name,command_input))
        return get_command_input(r_name)
    return command_input.lower()

def command_not_valid(r_command):
    """function for validating command"""

    commands_list = ['off','help','forward','back','left','right']
    command_arg_1, command_arg_2 = split_and_list(r_command)
    if command_arg_1.lower() in commands_list and len(command_arg_2) == 0 or command_arg_2.isdigit() == True:
        return True

def split_and_list(r_command):
    """ function for sorting the command input"""

    command = r_command.split(' ',1)
    if len(command) > 1:
        return command[0] , command[1]
    return command[0],''

def robot_switch(r_name):
    """ function for switching the robot off"""
    return False

def help_info(r_command):

    info = 'I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands \n'
    return True,info

def forwards_movement(r_name,steps,command):
    """function resposible for forwards movement"""

    if position_updator(steps,command):
        text = ' > '+r_name+' moved forward by '+str(steps)+' steps.'
        return True,text
    else:
        text = r_name+': Sorry, I cannot go outside my safe zone.'
        return True,text

def backwards_movement(r_name,steps,command):
    """function resposible for backwards movement"""

    if position_updator(-steps,command):
        text = ' > '+r_name+' moved back by '+str(steps)+' steps.'
        return True,text
    else:
        text = r_name+': Sorry, I cannot go outside my safe zone.'
        return True,text

def robot_sprint(r_name,steps):
    """ function responsible for robot sprint"""
    if  steps == 1:
        return forwards_movement(r_name, 1,'forward')
    else:
        next_command, text = forwards_movement(r_name,steps,'forward')
        print(text)
        return robot_sprint(r_name,steps - 1)

def make_right_turn(r_name,command):
    """function responsible for turning the robot right"""

    global direction_index

    direction_index += 1
    if direction_index > 3:
        direction_index = 0

    text = ' > '+r_name+' turned right.'
    return True , text

def make_left_turn(r_name,command):
    """function responsible for turning the robot left"""

    global direction_index

    direction_index -= 1
    if direction_index < 0:
        direction_index = 3
    text = ' > ' + r_name+ ' turned left.'
    return True, text

def show_position(r_name):
    print(' > {} now at position ({},{}).'.format(r_name,position_x,position_y))

def within_area_limit(x , y):
    """ function for managing the allowed position limit"""

    min_x = -100
    max_x = 200
    min_y = -100
    max_y = 100

    if min_x <= x <= max_x and min_y <= y <= max_y:
        return True

def position_updator(steps,r_command):

    directions = ['forward', 'right', 'back', 'left']
    global position_x,position_y,direction_index
    new_x = position_x
    new_y = position_y

    if directions[direction_index] == 'forward':
        new_y += steps
    elif directions[direction_index] == 'right':
        new_x += steps
    elif directions[direction_index] == 'back':
        new_y -= steps
    elif directions[direction_index] == 'left':
        new_x -= steps

    if within_area_limit(new_x,new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False

def command_handler(r_command,r_name):

    command, steps = split_and_list(r_command)
    next_command = True
    out_text = ''
    if command == 'off':
        return False
    elif command == 'help':
        next_command,out_text = help_info(r_command)
    elif command == 'forward':
        next_command, out_text = forwards_movement(r_name,int(steps),command)
    elif command == 'back':
        next_command, out_text = backwards_movement(r_name,int(steps),command)
    elif command == 'sprint':
        next_command, out_text = robot_sprint(r_name,int(steps))
    elif command == 'right':
        next_command, out_text = make_right_turn(r_name,command)
    elif command == 'left':
        next_command, out_text = make_left_turn(r_name,command)

    print(out_text)
    show_position(r_name)
    return next_command

def robot_start():
    """This is the entry function, do not change"""
    global position_x,position_y,direction_index
    position_x = 0
    position_y = 0
    direction_index = 0
    name = robot_name()
    print('{}: Hello kiddo!'.format(name))
    command = get_command_input(name)
    while command_handler(command,name):
        command = get_command_input(name)
    print_out(name,'Shutting down..')
if __name__ == "__main__":
    robot_start()