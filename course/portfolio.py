import csv
import sys

def cost(filename, *, errors='silent'):
    """
    Computes total shares*price for a CSV file with name, date, shares, price data
    :param filename:
    :return total:
    """
    if errors not in {"warn", "silent", "raise"}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    total = 0.0
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
            total += row[2]*row[3]
    return total

print(f"Total: {cost(sys.argv[1])}")