count = 1
product = {}
while count != 5:
    n = input('Product {}: '.format(count))
    x = int(input('Price : '))
    product.update({n:x})
    count +=1
max_val = max(product.values())
max_item = max(product, key=product.get)
print('Product in dictionary: {}'.format(product))
print('Product with the highest price is "{}".\nIts price is "{}" baht.'.format(max_item,max_val))