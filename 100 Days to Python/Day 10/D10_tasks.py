# Day 10 focuses on functions with outputs

# I'll be making a function that makes a name in Title Case
# Docstrings is a comment or description of a function

# .title() = title case function
def format_name(f_name,l_name):
    """Take a first and last name and format it to 
    return the title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("Enter your first name: "), input("Enter your last name: "))) # outputs the line 10

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("A leap year.")
                return True
            else:
                print("Not a leap year.")
                return False
        else:
            print("A leap year")
            return True
    else:
        print("Not a leap year.")
        return False
        
print(is_leap_year(2400))

# DOCSTRINGS