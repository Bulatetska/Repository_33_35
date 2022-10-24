
#___1___
def sort_list(list):
    return sorted(list)


#___2___
def find_element_by_value(list, value):
    return print('Element ', value,' has index ', list.index(value))


#___3___
def find_sequence_of_elements(list):
    for i in range(len(list)): 
        print(i, ' element --> ', list[i])


#___4___
def find_five_min_elements(list):
    newArr = []
    for i in range(5):
        minValue = min(list)
        newArr.append(minValue)
        list.remove(minValue)
    return newArr


#___5___
def find_five_max_elements(list):
    newArr = []
    for i in range(5):
        maxValue = max(list)
        newArr.append(maxValue)
        list.remove(maxValue)
    return newArr


#___6___
def find_average_of_list(list):
    return sum(list) / len(list)


#___7___
def find_set_of_list(list):
    return set(list)
