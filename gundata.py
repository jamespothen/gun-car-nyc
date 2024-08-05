infile = open("csv/NYPD_Shooting_Incident_Data__Year_To_Date__20240727.csv", "r")
# outfile = open(filedict[file], "w")


print(infile)
# print(filedict[file])
print()



# for line in infile:
#     try:
#         pickuplongitude = line.split(",")[5]
#         pickuplatitude = line.split(",")[6]
#         if pickuplongitude != "0" and pickuplatitude != "0":
#             print(infile)
#             print(f"{pickuplongitude}, {pickuplatitude}")
#             print(f"{pickuplongitude}, {pickuplatitude}", file=outfile)
#             print()
#     except:
#         print("Error!")
#         print("Problem with the following line")
#         print(line)

infile.close()
# outfile.close()
