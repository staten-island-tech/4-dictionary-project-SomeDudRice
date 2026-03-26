items = [
 {
   "name": "base ball",
   "price": 5,
   "weight": 150,
 },
 {
   "name": "basket ball",
    "price": 20,
    "weight": 600,
 },
 {
   "name": "volley ball",
   "price": 25,
   "weight": 400,
 },
 {
   "name": "bowling ball",
   "price": 75,
   "weight": 7000,
 },
 {
   "name": "tennis ball",
   "price": 1,
   "weight": 60,
 },
 {
   "name": "soccer ball",
   "price": 50,
   "weight": 450,
 }
]
total =0
order = 0
corder = 0
cart = []
for index, item in enumerate(items):
  print(index, ":", item["name"])
buying=0
while buying == 0:
  order = int(input("which one"))
  print ("would you like to buy",items[order]["name"],",",items[order]["price"],"$,",items[order]["weight"],"grams")
  if int(input("type 1 to buy, 2 to cancel")) == 1:
    cart.append(items[order]['name'])
    total = total + items[order]["price"]
  if int(input("would you like to continue shopping? 1 to continue, 2 to end")) == 2:
    buying= +1
print("youve pruchased",cart, "price is",total,"$")