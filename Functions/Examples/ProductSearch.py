products = [
    {'id' : 101, 'name' : 'Apple', 'price' : 45000, 'color': 'white'},
    {'id' : 102, 'name' : 'Samsung', 'price' : 55000, 'color': 'black'},
    {'id' : 103, 'name' : 'Vivo', 'price' : 22000, 'color': 'white'},
    {'id' : 104, 'name' : 'Apple', 'price' : 75000, 'color': 'white'},
    {'id' : 105, 'name' : 'Vivo', 'price' : 20000, 'color': 'silver'},
    {'id' : 106, 'name' : 'Samsung', 'price' : 65000, 'color': 'gray'},
    {'id' : 107, 'name' : 'Redmi', 'price' : 15000, 'color': 'black'},
    {'id' : 108, 'name' : 'Redmi', 'price' : 12000, 'color': 'black'},
    {'id' : 109, 'name' : 'Vivo', 'price' : 18000, 'color': 'white'},
    {'id' : 110, 'name' : 'Apple', 'price' : 35000, 'color': 'silver'}
]

product_name = input("Enter name of product : ")

for data in products:
    if data['name'] == product_name and data['price'] < 50000:
        print(data)






