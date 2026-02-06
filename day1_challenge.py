sales = [120, 250, 400, 180, 90]

def analyze_sales(sales):
    total = 0
    for sale in sales:
        total += sale

    average = total / len(sales)

    print("Total Sales:", total)
    print("Average Sale:", average)

    for sale in sales:
        if sale > average:
            print("Above Average Sale:", sale)

analyze_sales(sales)
