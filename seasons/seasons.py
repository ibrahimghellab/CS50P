from datetime import date
import re
from sys import exit
import inflect


def seasons(user_date):
    match=re.search(r"^(\d{4})-(\d{2})-(\d{2})$",user_date)
    if(match):
        year=match.group(1)
        month=match.group(2)
        day=match.group(3)

        p=inflect.engine()
        current_year=str(date.today()).split("-")[0]
        current_month=str(date.today()).split("-")[1]
        current_day=str(date.today()).split("-")[2]
        current_date=date.today()

        birthday=date(day=int(day),month=int(month),year=int(year))
        date_between=current_date-birthday
        result=date_between.days*60*24


        return(str(re.sub(r" and","",p.number_to_words(result))).capitalize()+" minutes")


    else:
        exit("Invalid date")

def main():
    user_date=input("Date of birth: ")
    print(seasons(user_date))



if __name__ == "__main__":
    main()
