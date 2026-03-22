# This function is used to ensure that an input field cannot be left blank
def get_non_empty_text(message):
    text = input(message).strip()
    while not text:
        print("\n This field cannot be empty")
        text = input(message).strip()
    return text

# This function is used to verify that a number cannot be negative 
def get_positive_number(message):
    validate = True
    while validate:
        try:
            data = int(input(message).strip())
            if  data < 0:
                 print("\n The value cannot be negative")
            else:
                 validate=False 
                 return data   
            
        except ValueError:
                print("\n The input is invalid")