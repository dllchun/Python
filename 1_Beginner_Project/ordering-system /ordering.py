ramen = {
    "鹽味拉面": 220,
    "醬油拉面": 240, 
    "蔥油拉面": 280
}



print("歡迎使用拉面機點餐")
for key, value in ramen.items(): 
    print(key +": $" + str(value))

ramen_favour = input("Please choose your ramen favor (Input 1, 2, 3) ")

total_price = 0

if ramen_favour == str(1):
    total_price += ramen.get("鹽味拉面")
elif ramen_favour == str(2):
    total_price += ramen.get("醬油拉面")
else:
    total_price += ramen.get("蔥油拉面")

need_L = input("Do you need larger size, 醬油 +$50, other +$30 (Y/N) ")

if need_L == "Y" or "y":
    if ramen_favour == str(2):
        total_price += 50
    else:
        total_price += 30
else: 
    total_price += 0





