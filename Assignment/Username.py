

class NameNotFound(Exception):
    def __int__(self,msg="name not found!"):
        Exception.__init__(self,msg)
try:
    d = {
        "Sachin": "icc",
        "Saurav": "BCCI"

    }

    u = str(input("enter the username"))
    p = str(input("enter the password"))

    if u not in d.keys():
        if p not in d.values():
            raise NameNotFound
            print("incorrect password and name")
    if u in d.keys():
        if p in d.values():
            print("Welcome "+u)


except (ZeroDivisionError,ValueError) as e:
    print("please enter the non-zero numeric value")


