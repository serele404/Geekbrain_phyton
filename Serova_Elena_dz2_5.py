price = [58.43, 15.12, 78.05, 901.02, 106.31, 40.16, 21.15, 47.67, 57.33]

price.sort()

price_new = []
for el in price:
    el = str(el)
    list = el.split('.')
    stroke = f'{list[0]} руб. {list[1]:0<2} коп.'
    price_new.append(stroke)
reverse = price_new.copy()[::-1]

print(price_new)
print(reverse)
print(price_new[-5:])