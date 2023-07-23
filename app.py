from car import Car
from owner import Owner
from files import save_data,load_data
from functions import create,read,update_visit,delete


while True:
    options='''menu:
    1.new entry
    2.view all entries
    3.update entry
    4.delete entry
    '''
    if options=="1":
        name=input("enter car brand")
        year=input("enter car year")
        color=input("enter car color")
        plate_num=input("enter plate number")
        