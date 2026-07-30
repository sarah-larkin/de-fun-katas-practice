# update missing location info for students 
# arg: list of dicts 
# returns: new list - if location missing, "remote" added
# must be pure function 

#----------------
# First attempt 
#----------------

# import copy

# def update_remote_students(std_info): 
    
#     std_info_copy = copy.deepcopy(std_info) 

#     for student in std_info_copy: 
#         if 'location' not in student: 
#             student['location'] = 'remote'

#     return std_info_copy


# ALTERNATIVE 

def update_remote_students(std_info):
    result = []    # new list 

    for student in std_info:
        new_student = student.copy()  # new dict each time 
        if "location" not in new_student:
            new_student["location"] = "remote"
        result.append(new_student)  # copied dict added to new list for every student

    return result

"""NOTES
Remember it is a list of dicts!!
To access location key, need to specify list index first --> std_info[0]['location']
For loop over the list - each student is the dict 

Using IN to check a dict will check keys only - so do not neet to include 
To check values would need to use student.values() 
"""
