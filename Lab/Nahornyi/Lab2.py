price = input("PRICE: ")


if int(price) <= 100 :
   print("ціна: ", str(price))
elif int(price) > 100 and int(price) <= 500:
   zn = 0.03 * int(price)
   print("ціна зі знижкою = ", int(price) - zn)
elif int(price) > 500 and int(price) <= 1000:
   zn = 0.05 * int(price)
   print("ціна зі знижкою = ", int(price) - zn)
elif int(price) > 1000:
   zn = 0.1 * int(price)
   print("ціна зі знижкою = ", int(price) - zn)



aaaa = input("ВВЕДІТЬ: ")
aaaa_len = len(aaaa)
not_empty = False
if(aaaa_len > 0):
   not_empty = True
state = aaaa if not_empty else "None"
print (state)