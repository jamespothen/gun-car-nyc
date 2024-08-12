# infile = open("csv/NYPD_Shooting_Incident_Data__Year_To_Date__20240727.csv", "r")
# outfile = open("csv/ShootingsByMonth.csv", "w")
#
#
# print(infile)
# print(outfile)
# print()
#
# for line in infile:
#     try:
#         murder = line.split(",")[9]
#         month = line.split(",")[1][0:2]
#         if murder == "Y":
#             print(month)
#             print(f"{month}", file=outfile)
#     except:
#         print("Error!")
#         print("Problem with the following line")
#         print(line)
#
# infile.close()
# outfile.close()
