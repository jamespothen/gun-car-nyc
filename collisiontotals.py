infile = open("csv/CollisionsByMonth.csv")
outfile = open("csv/collisionmonthlytotals.csv", "w")

monthcountdict = {
    "01": 0,
    "02": 0,
    "03": 0,
    "04": 0,
    "05": 0,
    "06": 0,
    "07": 0,
}

for line in infile:
    month = line.split(",")[0][0:2]
    numpeoplekilled = int(line.split(",")[1])
    print(numpeoplekilled)
    monthcountdict[month] += numpeoplekilled
infile.close()

print(monthcountdict)

for month in monthcountdict.keys():
    print(f"{month}, {monthcountdict[month]}", file=outfile)

outfile.close()
