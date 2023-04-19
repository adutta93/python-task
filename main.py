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


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.
    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    list_3 = {}
  
     
    for list_elem in list_1 + list_2:
       if list_elem['id'] not in list_3:
           list_3[list_elem['id']] = list_elem
       else:
           list_3[list_elem['id']].update(list_elem)    
 
    
 # Convert the dictionary to a list 
    merged_list = list( list_3.values())
    return merged_list
list_3 = merge_lists(list_1, list_2)

print(list_3)