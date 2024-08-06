infile = open("csv/Motor_Vehicle_Collisions_-_Crashes_20240727.csv", "r")
outfile = open("csv/CollisionsByMonth.csv", "w")


print(infile)
print(outfile)
print()

for line in infile:
    try:
        date = line.split(",")[0]
        year = date[-4:]
        # print(year)
        if year == "2024":
            month = date[0:2]
            print(month)
#         murder = line.split(",")[9]
#         month = line.split(",")[1][0:2]
#         if murder == "Y":
#             print(month)
#             print(f"{month}", file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
