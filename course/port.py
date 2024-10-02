import csv
import sys
import urllib.request

def cost(filename, *, errors='warn'):
    """
    Computes total shares*price for a CSV file with name, date, shares, price data
    :param filename:
    :return total:
    """
    if errors not in {"warn", "silent", "raise"}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    portfolio = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print("ERROR", "Bad row:", i, row)
                    print("ERROR", "Reason:", err)
                elif errors == "raise":
                    raise # Reraises the last exception
                else:
                    pass # ignore
                continue
            # record = tuple(row)
            portfolio.append({'name': row[0],
                              'date': row[1],
                              'shares': row[2],
                              'price': row[3]
                              })
    return portfolio

portfolio = cost(sys.argv[1])
total = 0.0
for p in portfolio:
    total += p['shares'] * p['price']


print(f"Total cost: {total}")

sum = sum([holding["shares"] * holding["price"] for holding in portfolio])
print(f"Sum: {sum}")

sum100 = [holding["name"] for holding in portfolio if holding["shares"] > 100]
print(f"Sum100: {set(sum100)}")

y100 = {holding["name"] for holding in portfolio} # make a set of unique names
un = ",".join(y100)
print(un)
u = urllib.request.urlopen(f"http://finance.yahoo.com/d/quotes.csv?s={un}&f=l1")
data = u.read
for name, price in zip(y100, data):
    print(f"{name} = {price}")

