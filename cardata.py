infile = open("csv/Motor_Vehicle_Collisions_-_Crashes_20240727.csv", "r")
outfile = open("csv/CollisionsByMonth.csv", "w")


print(infile)
print(outfile)
print()

for line in infile:
    try:
        date = line.split(",")[0]
        year = date[-4:]
        if year == "2024":
            numpeoplekilled = int(line.split(",")[11])
            if numpeoplekilled > 0:
                print(date, numpeoplekilled)
                print(f"{date}, {numpeoplekilled}", file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
