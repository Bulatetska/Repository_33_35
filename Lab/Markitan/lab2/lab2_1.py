# 1st task:
price = str(input('enter your price: '))

if not price or not price.isdigit():
    quit()
else:
    discount = 0
    price = int(price)
    if 100 < price <= 500:
        discount = 3
        price_with_disc = price - price * (discount / 100)
        print('your discount is ' + str(discount) + '%. final price: ' + str(price_with_disc))
    elif 500 < price <= 1000:
        discount = 5
        price_with_disc = price - price * (discount / 100)
        print('your discount is ' + str(discount) + '%. final price: ' + str(price_with_disc))
    elif price > 1000:
        discount = 10
        price_with_disc = price - price * (discount / 100)
        print('your discount is ' + str(discount) + '%. final Price: ' + str(price_with_disc))
    else:
        print("there's no discount for ya ")
