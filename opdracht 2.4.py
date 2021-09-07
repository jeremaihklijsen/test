#Get the five prices of the product
#product1, product2, product3, product4, product5
product1 = float(input('enter product cost: '))
product2 = float(input('enter product cost: '))
product3 = float(input('enter product cost: '))
product4 = float(input('enter product cost: '))
product5 = float(input('enter product cost: '))

#calculate the taxes paid for the products
cost = (product1 + product2 + product3 + product4 + product5) * 1.07

#display the cost
print('the product cost', cost)
