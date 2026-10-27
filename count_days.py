from datetime import datetime

alice_arrive = input("Alice arrival date (MM-DD): ")
alice_leave = input("Alice leaving date (MM-DD): ")
bob_arrive = input("Bob arrival date (MM-DD): ")
bob_leave = input("Bob leaving date (MM-DD): ")

def convert_date(date):
    return datetime.strptime("2021-" + date, "%Y-%m-%d")

start = max(convert_date(alice_arrive),
            convert_date(bob_arrive))

end = min(convert_date(alice_leave),
          convert_date(bob_leave))

if start <= end:
    print((end - start).days + 1)
else:
    print(0)