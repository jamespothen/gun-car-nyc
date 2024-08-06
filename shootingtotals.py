infile = open("csv/ShootingsByMonth.csv")
outfile = open("csv/shootingmonthlytotals.csv", "w")

monthcountdict = {
    "01": 0,
    "02": 0,
    "03": 0,
    "04": 0,
    "05": 0,
    "06": 0,
}


for line in infile:
    month = line[0:2]
    monthcountdict[month] += 1
infile.close()

for month in monthcountdict.keys():
    print(f"{month}, {monthcountdict[month]}", file=outfile)

outfile.close()
