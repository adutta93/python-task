list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

'''
Created on 19-Apr-2023

@author: Akash Dutta
'''

def merge_lists(list_1, list_2) -> list:
    # Creating an empty dictionary information
    list_3 = {}
  
    # Loop through both lists add student's information to the new dictionary
    for list_elem in list_1 + list_2:
       if list_elem['id'] not in list_3:
           # entering a new element in the dictionary
           list_3[list_elem['id']] = list_elem
       else:
            # the elemenet already exists, updating the element instead
           list_3[list_elem['id']].update(list_elem)    
 
    
 # Convert the dictionary to a list 
    merged_list = list( list_3.values())
    return merged_list

# calling the 'merge_lists' function and storing the final value in a variable
list_3 = merge_lists(list_1, list_2)
# print(list_3)