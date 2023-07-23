from files import save_data,load_data
from owner import Owner
from car import Car



def create(car:Car):
    data=load_data()
    data.append(car)
    save_data(data=data)    

def read():
    data=load_data()
    for i in data:
        print(i)

def update_visit(license="",date=""):
        data=load_data()
        for i in data:
            if str(i.license)==license:
                i.last_visit=date
                print("date has been updated")
        save_data(data)

def delete(name="name"):
    data=load_data()
    for i in data:
        if i.name==name:
            data.remove(i)
            print("item has been removed")
    save_data(data)
