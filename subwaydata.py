infile = open("csv/MTA_Major_Felonies_20240812.csv", "r")
outfile = open("csv/SubwayDeathsByMonth.csv", "w")


print(infile)
print(outfile)
print()

for line in infile:
    try:
        crime = line.split(",")[3]
        year = line.split(",")[0][-4:]
        if crime == 'Murder' and year == '2024':
            print(line)
        # murder = line.split(",")[9]
        # month = line.split(",")[1][0:2]
        # if murder == "Y":
        #     print(month)
        #     print(f"{month}", file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
