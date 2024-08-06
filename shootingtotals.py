infile = open("csv/ShootingsByMonth.csv")
# outfile = open("shootingmonthlytotals.csv", "w")
#
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
    # print(monthcountdict[month])
    # print(f"{year}: {monthcountdict[month]}")
infile.close()
print(monthcountdict)
#
# for year in yearcountdict.keys():
#     print(f"{year}, {yearcountdict[year]}", file=outfile)
#
# outfile.close()
