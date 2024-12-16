temperature_readings = list(map(int,input().split(",")))
sum=0
for i in temperature_readings:
    sum+=i
l=len(temperature_readings)
print("Average Temperature:",sum/l)
print("Highest Temperature",max(temperature_readings))
print("Lowest Temperature:",min(temperature_readings))