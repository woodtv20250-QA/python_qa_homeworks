from address import Address
from mailing import Mailing

from_address = Address("633159", "Новосибирск", "Трикотажная", "12", "85")

to_address = Address("455025", "Магнитогорск", "Правды", "86", "48")

my_mailing = Mailing(to_address, from_address, 16.40, "TRACK999999999")

print(
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.postcode}, " 
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.building} - "
    f"{my_mailing.from_address.flat} в "
    f"{my_mailing.to_address.postcode}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.building} - "
    f"{my_mailing.to_address.flat}. Стоимость "
    f"{my_mailing.cost} рублей."
)

