""" 
Group 1. Collaboration with Klara, Marije, Sarab.

"""


def merge_dicts(dict1,dict2,dict3):
    """
    Change the for loop to a one line dict comprehension
    """
       
    new_dict = {k: v for d in [dict1,dict2,dict3] for k, v in d.items()}
    
    return new_dict

if __name__ == "__main__":
    dict1 = {'1':1, '2':2, '3':3}
    dict2 = {'a':'a', 'b':'b', 'c':'c'}
    dict3 = {'w':'w', 'z':'z', 'y':'y'}
    print(merge_dicts(dict1,dict2,dict3))
