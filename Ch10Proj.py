list_new = ['hello', 'world', 12.3, 'orange', 987]

def reverse_characters (string_to_reverse):
    if type(string_to_reverse) != str:
        string_to_reverse = str(string_to_reverse)
    new_list = list(string_to_reverse)
    new_list.reverse()
    new_word = "".join(new_list)
    return new_word


def new_function(one_parameter):
    empty_list = []
    for item in one_parameter:
        item = reverse_characters(item)
        empty_list.append(item)
    empty_list.reverse()
    return empty_list


print(new_function(list_new))


test = 'Function'

def bonus_function(one_parameter):
    if int(len(one_parameter)) > 3:
        new_word = one_parameter[0:4]
    else:
        int(len(one_parameter)) < 3
        new_word = one_parameter[-1]
    
    phrase = 'we put the {fname} in {fname}.'.format(fname = new_word)
    return phrase

print(bonus_function(test))

def bonus_mission(length, width = 0):
    if width == 0:
        return length * length
    else:
        return length * width

print('the area is ' + str(bonus_mission(10, 4)) + ' cm^2')