# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    Shape = ''
    while Shape == '':
        Shape = input('Shape?: ')
        if Shape.lower() == 'pyramid':
            return 'pyramid'
        elif Shape.lower() == 'square':
            return 'square'
        elif Shape.lower() == 'triangle':
            return 'triangle'
    

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = int(input())
    return height


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        for i in range(1,height+1):
            for j in range(1,height-i+1):
                print(end=' ')
            for j in range(i,0,-1):
                print('*',end='')
            for j in range(2,i+1):
                print('*',end='')
            print()
    else:
        row = 1
        while row <= height:
            col = 1
            while col <= 2*height - 1:
                if row == height or row + col == height + 1 or col - row == height - 1:
                    print('*',end='')
                else:
                    print(end=' ')
                col += 1
            row += 1
            print()

 
# TODO: Step 3
def draw_square(height, outline):
    rows = 0
    if outline == False:
        for rows in range (height):
           print('*'*height)
    else:
        rows = 1
        while rows<= height:
           cols = 1
           while cols <= height:
               if rows == 1 or rows == height or cols == 1 or cols == height:
                   print('*',end='')
               else:
                   print(' ', end='')
               cols += 1
           rows += 1
           print()

           



# TODO: Step 4
def draw_triangle(height, outline):
    rows = 1
    if outline == False:
        while rows <= height + 1:
            cols = 1
            while cols <= rows:
                print('*',end='')
                cols += 1
            rows += 1
            print(' ')
    else:
        rows = 0
        while rows <= height  + 1:
            cols = 0
            while cols <= height + 1:
                if cols == 0 or cols == rows or rows == cols or rows == height + 1:
                   print('*',end='')
                else:
                    print(end=' ')
                cols += 1
            rows += 1
            print()


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height,outline)
    elif shape == draw_diamond(height,outline):

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    user_input = input('Outline only? (y/n): ')
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
       return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)