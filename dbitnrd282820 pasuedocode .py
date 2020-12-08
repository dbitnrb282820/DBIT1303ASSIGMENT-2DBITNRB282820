# This is a resturant ordering script



client_name= string
#input of client details
table=input("table_number")
#input  of table number
order_number=input("order_number")
#input of order
print("hi " +client_name+ table + order_number)

#menu list

print("menu list ")
print ("1.chicken_fry +rice")
print( "2 beef_stew + ugali")
print ("3 fufu +goat_stew")
print ("4 ugali+ fish")
print ("5 pilau")
print ("6 mukimo + stew")
print ("7 matoke_nyama")
print ("8 grilled_chicken")
print ("9 wali_wanazi")

input("enter food number:")


waiter_order=1-9
while waiter_order <=1-9:
    print ("your order has been noted.")
    waiter_order+=1
    print ("order complete")

def order():
        print ("hello you have ordered" + food)
# you get the food you had ordered.
#payment

# one enters the code
secret_code="fall"
payment_code=""
not_paid =false

#create a script

#varification of payments
while payment_code!=payment_code and not("not_paid"):
    if payment_code< limit:
        payment_code=input("enter payment_code")
        payment_code +=1
        print("not paid ,please play")
    else:print("you have paid")
    # same could be sighted and recorded on scripts