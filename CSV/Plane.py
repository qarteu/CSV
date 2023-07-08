import pandas as pd
import csv;

#reads csv file of AirTrafficPassengers and for each new date found, sum up amount of passagners in each of the 3 different activity type codes and write new

with open('/Users/kartik/Downloads/Air_Traffic_Passenger_Statistics (2).csv', newline='') as input:
    reader = csv.reader(input);

    index = 0

    dict = {}
    for row in reader:
        if index == 0:
            index += 1;
            continue;

        date = row[0]
        atc = row[7]
        cnt = row[11]

        if not date in dict:
            dict[date] = {'Enplaned': 0, 'Deplaned': 0, 'Thru / Transit': 0}
        dict[date][atc] += int(cnt)

    print(dict)

    with open('/Users/kartik/Downloads/NewAir.csv', 'w') as file:
        file.write("Date,Enplaned,Deplaned,Thru/Transit")
        file.write("\n")
        for key in dict:
            file.write(key + "," + str(dict[key]["Enplaned"]) + "," + str(dict[key]["Deplaned"]) + "," + str(
                dict[key]["Thru / Transit"]))
            file.write("\n")
