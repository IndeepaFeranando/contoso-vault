DAYS_IN_WEEK = 7
day: int = int(input("Enter day of the week: "))
days_to_wait = int(input("Enter days to wait: "))

delivery_day = int(day + days_to_wait)
if delivery_day > DAYS_IN_WEEK:
    delivery_day -= DAYS_IN_WEEK
    

print(delivery_day)

assert 1 <= delivery_day <= DAYS_IN_WEEK
