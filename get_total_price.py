def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list
    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    data = data.split()[1:]
    count = 0.0

    for i in data:
        val = float(i.split(",")[1])
        count += val
        
    print("{:.1f}".format(count))

data = open('fruits.csv').read()
print(get_total_price(data))
