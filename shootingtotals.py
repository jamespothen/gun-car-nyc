# infile = "csv/ShootingsByMonth.csv"
# outfile = open("shootingmonthlytotals.csv", "w")
#
# monthcountdict = {
#     "01": 0,
#     "02": 0,
#     "03": 0,
#     "04": 0,
#     "05": 0,
#     "06": 0,
# }
#
# for filename in infilelist:
#     infile = open(filename, "r")
#     year = filename[0:4]
#
#     for line in infile:
#         yearcountdict[year] += 1
#         print(f"{year}: {yearcountdict[year]}")
#     infile.close()
#
# for year in yearcountdict.keys():
#     print(f"{year}, {yearcountdict[year]}", file=outfile)
#
# outfile.close()
