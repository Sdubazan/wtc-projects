import random

def find_min(element):
    """TODO: complete for Step 1"""
    i = 0
    while i <len(element):
        if type(element[i]) == str:
            return - 1
        i += 1

    if len(element) == 1:
        return element[0]
    elif len(element) == 0:
        return -1
    
    if element[0] < element[1]:
        element.append(element[0])
        return(find_min(element[1:]))
    else:
        return(find_min(element[1:]))

def sum_all(element):
    """TODO: complete for Step 2"""
    i = 0
    while i <len(element):
        if type(element[i]) == str:
            return - 1
        i += 1

    if len(element) == 1:
        return element[0]
    elif len(element) == 0:
        return -1
    else:
        return element[0] + sum_all(element[1:])


def find_possible_strings(character_set, n,c = [],x = 0):
    """TODO: complete for Step 3"""
    if n == 1:
        return character_set
    elif len(character_set) == 0 or n == 0:
        return []
    else:
        for i in character_set:
            if type(i) == int:
                return []
    
    a = len(character_set) ** n
    char = ''
    for i in range(n):
        rand_char = random.choice(character_set)
        char = char + rand_char
    
    if x == a:
        return(sorted(c))
    else:
        if char not in c:
            x += 1
            return find_possible_strings(character_set,n,c + [char],x)
        else:
            return find_possible_strings(character_set,n,c,x)
print(find_possible_strings(['a','b'],2))


