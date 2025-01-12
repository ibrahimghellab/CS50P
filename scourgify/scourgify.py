import sys
import csv


try:
    before=sys.argv[1]
    after=sys.argv[2]
except IndexError:
    sys.exit("Too few command-line arguments")
else:
    try:
        error=sys.argv[3]
    except IndexError:
        try:
            with open(before,"r") as b:
                reader=csv.DictReader(b)
                with open(after,"w") as a:
                    writer=csv.DictWriter(a,fieldnames=["first"]+["last"]+["house"])
                    writer.writeheader()
                    for row in reader:
                        fullName=row["name"].split(", ")
                        writer.writerow(
                            {
                                "first" : fullName[1],
                                "last" : fullName[0],
                                "house" : row["house"]
                            }
                        )


        except FileNotFoundError:
            sys.exit(f"Could not read {before}")
    else:
        sys.exit("Too many command-line arguments")


