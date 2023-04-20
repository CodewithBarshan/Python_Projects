import phonenumbers
from phonenumbers import timezone,geocoder,carrier #geocoder will give information about location & carrier will brief information about sim
number=input("Please Enter Phone No with +: ")
phone=phonenumbers.parse(number)  #parse will give all the details about number
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en") #en will write the name of comapny in english
reg=geocoder.description_for_number(phone,"en") #will give the details about sim registration
print(phone)
print(time)
print(car) 
print(reg)
