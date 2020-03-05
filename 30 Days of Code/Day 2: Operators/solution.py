meal = float(input())
tip = int(input())
tax = int(input())
tip /= 100
tax /= 100
total = meal + (meal*tip) + (meal*tax)
print(int(round(total)))
