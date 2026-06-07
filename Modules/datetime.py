import datetime

# Current date & time
print(datetime.datetime.now())

# Today's date
print(datetime.date.today())

# UTC time
print(datetime.datetime.utcnow())

# Current year
print(datetime.datetime.now().year)

# Current month
print(datetime.datetime.now().month)

# Current day
print(datetime.datetime.now().day)

# Custom time
print(datetime.time(10, 30, 45))

# Custom date
print(datetime.date(2026, 6, 7))

# Time difference
print(datetime.timedelta(days=5))

now = datetime.datetime.now()

# Format date
print(now.strftime("%Y-%m-%d"))

# Format time
print(now.strftime("%H:%M:%S"))

# Convert string to date
print(datetime.datetime.strptime("2026-06-07", "%Y-%m-%d"))

# Timestamp
print(now.timestamp())

# Weekday (0=Monday)
print(datetime.date.today().weekday())

# ISO weekday
print(datetime.date.today().isoweekday())

# ISO format date
print(datetime.date.today().isoformat())

# Current time string
print(datetime.datetime.now().ctime())

# Extract date only
print(datetime.datetime.now().date())

# Extract time only
print(datetime.datetime.now().time())

# Future date calculation
future = datetime.datetime.now() + datetime.timedelta(days=10)
print(future)