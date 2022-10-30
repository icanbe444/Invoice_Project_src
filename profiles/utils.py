import random


"""
This file is used to generate a 26 character nuber for the account number varaible in profile

"""

available_numbers= [x for x in range(100)]

size = 5

def generate_account_number():
    new_number_list = [str(random.choice(available_numbers)) for _  in range(size)]
    new_number_str  = "".join(new_number_list)
    return new_number_str



def generate_invoice_number():
    number_list = [str(random.choice(available_numbers)) for _  in range(size)]
    number_str  = "".join(number_list)
    return number_str