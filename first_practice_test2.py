def product_sum(number1, number2):
    product = number1 * number2
    sum = number1 + number2
    if product <= 1000:
        return product
    else:
        return sum

result = product_sum(100,200)
print(result)