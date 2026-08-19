name=input("Enter your name: ")

#List of Items
lists="""
Rice     Rs 10/Kg
Sugar    Rs  8/kg
Oil      Rs 30/litre
Salt     Rs 25/kg
paneer   Rs 40/kg
Maggie   Rs 12/pack
Boost    Rs 200/bottle
"""
#declaration

price=0
pricelist=[]
finalprice=0
totalprice=0
ilist=[]
qlist=[]
plist=[]

#Rate for each item
items={
    
    "rice":20,
    "sugar":8,
    "oil":30,
    "salt":25,
    "paneer":40,
    "maggie":12,
    "boost":200
}

while True:
    option=input("Press1 enter to list or press2 to exit: ")
    if option=="2":
        print("Thankyou for Shopping")
        break
    elif option=="1":
        print(lists)

        while True:
            inp1=input("Press1 enter to buy or press2 to exit: ")
            if inp1=="2":
                print("Thankyou for Shopping")
                break
            elif inp1=="1":
                item=input("Choose your item: ").lower()
                while True:
                    quantity_input=input("Enter Quantity:")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("Enter a Valid Quantity input:")
                if item in items:
                    price=quantity*items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice+=price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available.Sorry for inconvenience")
        if totalprice>0:
            tax= (totalprice*12)/100
            finalamount=totalprice+tax
            print("#"*25+" PythonLife Supermarket "+"#"*25)
            print(" "*28+"Hyderabad")
            print("Name: ",name," "*30,"05 August 2026")
            print("_"*75)
            print("SNo",10*" ","Items"," "*8,"Quantity"," "*8,"Price")
            for i in range(len(pricelist)):
                print(i,13*" ",ilist[i]," "*9,qlist[i]," "*10,plist[i])
            print(75*"_")
            print(" "*50,"Total Amount: ","Rs",totalprice)
            print(" "*50,"Tax Amount:    RS",tax)
            print("_"*75)
            print(" "*50,"Final Amount:  RS",finalamount)
            print("_"*75)
            print(" "*30,"Thankyou Visit Again")
            print("_"*75)
        else:
            print("Please cart your items")
            break
