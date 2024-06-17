# Functions with outputs

# def my_function():
#    return 3*2

# output = my_function()


def format_name(f_name,l_name):
    '''This function takes first name and
    last name, and returns a formatted name'''
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
formatted_string = format_name("BHARGAV","Das")
print(formatted_string)

### Docstrings: These are explainations that we can insert
# in our code using three ''' ''' and docstrings are
# inserted in the first line after the function.