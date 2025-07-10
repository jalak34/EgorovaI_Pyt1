from address import Address
from mailing import Mailing

to_address = Address("123456", "Санкт-Петербург", "Шостаковича", "10", "5")

from_address = Address("654321", "Всеволожск", "Межевая", "5", "9")
cost = 100
track = 456780

mailing = Mailing (to_address, from_address, cost, track)


print(mailing)