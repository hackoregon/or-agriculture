# Methods for normalizing and filtering our raw data



def normalize_value_field(val):
    """ 
    Removes 'thousands commas' and casts str to float or integer.
    Any non-numeric values like '(D)' go to None / null.

    (Remember 'value' is actually the name of a field.)
    """
    num_string = val.replace(',', '')
    try:
        if '.' in num_string:
            return float(num_string)
        else:
            return int(num_string)
    except ValueError:
            return None 
