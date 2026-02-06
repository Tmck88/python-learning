sales = [120, 250, 400, 180, 90]

for sale in sales:
    if sale > 200:
        print("High sale:", sale)

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print("Average sale:", average(sales))
