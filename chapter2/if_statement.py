age, vip = 12, False
if 0<=age <4 and vip:
    ticket_price = 0
elif age <18:
    ticket_price = 25
elif age < 65:
    ticket_price = 40
else:
    ticket_price = 20
print(f'ticket ptice is {ticket_price}') # ticket ptice is 25