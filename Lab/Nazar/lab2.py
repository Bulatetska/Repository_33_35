def main():
    price = int(input("Впишіть кількість гривень:"))
    print("1)")
    if (price > 100) and (price <= 500):
        print("Ціна зі знижкою: ", price - (price*3)/100, "Знижка:", (price*3)/100)
    elif (price > 500) and (price <= 1000):
        print("Ціна зі знижкою: ", price - (price * 5) / 100, "Знижка:", (price * 5) / 100)
    elif (price > 1000):
        print("Ціна зі знижкою: ", price - (price * 10) / 100, "Знижка:", (price * 10) / 100)
    else:
        print("Немає знижки")
    print("2)")
    sequence = str(input("Введіть будь-яке стрінг значення:"))
    b = sequence if (len(sequence) >= 1) else None
    print(b)

main()