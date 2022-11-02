hour,minut = map(int,input().split())
plus = int(input())
minut+=plus

if minut>=60:
    hour+=int(minut/60)
    minut%=60
    if hour>=24:
        hour-=24
print("{} {}".format(hour,minut))