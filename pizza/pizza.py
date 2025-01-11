import csv
import sys
from tabulate import tabulate
try:
    name=sys.argv[1]
except(IndexError):
    sys.exit("Too few command-line arguments")
else:
    try:
        error=sys.argv[2]
    except(IndexError):
         if(sys.argv[1][-4:]!=".csv"):
            sys.exit("Not a CSV file")
         else:
            try:
                with open(name,"r") as file:
                    reader=csv.DictReader(file)
                    pizza_name=name.replace(".csv","").title()+" Pizza"
                    headers=[f"{pizza_name}","Small","Large"]
                    table=[]
                    for row in reader:
                        table.append([row[headers[0]],row[headers[1]],row[headers[2]]])
                    print(tabulate(table, headers, tablefmt="grid"))
            except (FileNotFoundError):
                sys.exit("File does not exist")
    else:
        sys.exit("To many command-line arguments")



