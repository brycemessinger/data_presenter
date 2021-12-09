# -----------------------------
cup_cake_opener = open("CupcakeInvoice.csv")
# -----------------------------

for cupCakes in cup_cake_opener:
    print(cupCakes)
# -----------------------------

chocolate = ""
strawberry = "" 
vanilla = ""

for cupcake_type in cup_cake_opener:
    cupcake_type = cupcake_type.split(',')
    for value in cupcake_type:
        if value == "Chocolate":
            print(value)
        elif value == "Strawberry":
            print(value)
        elif value == "Vanilla":
            print(value)
print("Chocolates =",chocolate,"Strawberries=",strawberry,"Vanillas",vanilla)
# -----------------------------

for invoice_total in cup_cake_opener:
    arr = (invoice_total.split(','))

    print(float(arr[3])*(float(arr[4])))
#------------------------------

for invoice_total in cup_cake_opener:
    arr = (invoice_total.split(','))
    total = 0
    total_function = (float(arr[3])*(float(arr[4])))

cup_cake_opener.close()