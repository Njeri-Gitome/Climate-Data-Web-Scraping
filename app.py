import time

# Convert date to Unix timestamp
start_date = "2024-01-01"
end_date = "2024-01-01"

start_timestamp = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
end_timestamp = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))

print(f"Start timestamp: {start_timestamp}")
print(f"End timestamp: {end_timestamp}")
