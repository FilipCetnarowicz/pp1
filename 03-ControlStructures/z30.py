
hour24=int(input("hours: "))
min60=int(input("minutes: "))
if hour24>12:
    hour12=hour24-12
    period="PM"
elif hour24<=12:
    hour12=hour24
    period="AM"
print(f"in 24h format: {hour24}:{min60}")
print(f"in 12h format: {hour12}:{min60}{period}")