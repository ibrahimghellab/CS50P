import re
import sys


def main():
        print(convert(input("Hours: ")))

def convert(s):

    match=re.search(r"^(\d{1,2}):?(\d{1,2})? (AM|PM) (to) (\d{1,2}):?(\d{1,2})? (AM|PM)$",s.strip())

    try:
        if(match):
            if(len(match.groups())<7):
                raise ValueError("ValueError")
        else:
            raise ValueError("ValueError")


        first_hour=match.group(1)
        first_minute=match.group(2)
        first_type=match.group(3)

        second_hour=match.group(5)
        second_minute=match.group(6)
        second_type=match.group(7)


        if(int(first_hour)>12 or int(second_hour)>12):
            raise ValueError("ValueError")

        if(first_minute):
            if(int(first_minute)>=60):
                raise ValueError("ValueError")

        if(second_minute):
            if(int(second_minute)>=60):
                raise ValueError("ValueError")

        if(match.group(4)!="to"):
            raise ValueError("ValueError")
    except ValueError:
        raise ValueError("ValueError")




    if(first_type=="PM"):
        if(first_hour!="12"):
            first_hour=str(int(first_hour)+12)
    else:
        if(first_hour=="12"):
            first_hour="00"

    if(not first_minute):
        first_minute="00"

    if(second_type=="PM"):
        if(second_hour!="12"):
            second_hour=str(int(second_hour)+12)
    else:
         if(second_hour=="12"):
            second_hour="00"

    if(not second_minute):
        second_minute="00"

    return f"{f"{int(first_hour):02}"}:{first_minute} to {f"{int(second_hour):02}"}:{second_minute}"


# 12 into 00 et 00 into 12
#ValueError
#Test



if __name__ == "__main__":
    main()


