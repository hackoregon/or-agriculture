

def clean_value(val):
    num_string = val.replace(',', '')
    try:
        if '.' in num_string:
            return float(num_string)
        else:
            return int(num_string)
    except ValueError:
            return None 
