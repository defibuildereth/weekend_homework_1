# WRITE YOUR FUNCTIONS HERE

import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_sold):
    pet_shop["admin"]["pets_sold"] += number_sold

def get_stock_count(pet_shop):
    stock = 0
    for pet in pet_shop["pets"]:
        stock += 1
    return stock

def get_pets_by_breed(pet_shop, breed):
    results = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            results.append(pet)
    return results

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    index = 0
    for pet in pet_shop["pets"]:
        index = pet_shop["pets"].index(pet)
        if pet["name"] == name:
            # pdb.set_trace()
            pet_shop["pets"].pop(index)

def add_pet_to_stock(pet_shop, new_pet):
    # pdb.set_trace()
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)