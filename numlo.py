import phonenumbers

from myNumb import number

from phonenumbers import geocoder
sanNumb= phonenumbers.parse(number,"CH")
yourLocation=geocoder.description_for_number(sanNumb,"en")
print(yourLocation)

from phonenumbers import carrier
sernumb=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(sernumb,"en"))
