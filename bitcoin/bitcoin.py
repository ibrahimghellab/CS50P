import sys
import requests

try:
    nb=float(sys.argv[1])
    json=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bitcoin_value=float(json["bpi"]["USD"]["rate_float"])*nb
    print(f"${bitcoin_value:,.4f}")
except (ValueError):
    sys.exit("Command-line argument is not a number")
except(IndexError):
    sys.exit("Missing command-line argument")
except(requests.RequestException):
    sys.exit("Fail to fetch, the URL is maybe down")
