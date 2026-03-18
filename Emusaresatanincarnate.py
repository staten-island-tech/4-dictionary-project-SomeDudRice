items = [
 {
   "name": "baseball",
     "price": 5,
     "weight": 150,},
 {
   "name": "basket ball",
     "price": 20,
     "weight": 600,},
 {
   "name": "volley ball",
     "price": 25,
     "weight": 400,},
 {
   "name": "bowling ball",
     "price": 75,
     "weight": 7000,},
 {
   "name": "tennis ball",
     "price": 2,
     "weight": 60,},
 {
   "name": "soccer ball",
     "price": 50,
     "weight": 450,},
]
for index, items in enumerate(items):
    print(index, ":", items["name"])