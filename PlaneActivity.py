import pandas as pd
import csv;
#read file

with open('/Users/kartik/Downloads/Air_Traffic_Passenger_Statistics (2).csv', newline='') as input:
    with open('/Users/kartik/Downloads/NewAirTrafficthing.csv', 'w') as output:

        writer = csv.writer(output);
        reader = csv.reader(input);

        date = None;

        dict = {
            "Enplaned": 0,
            "Deplaned": 0,
            "Thru / Transit": 0
        }

        count = 0;
        passengerCount = 0;
        testCount = 0;
        index = 0;
        prev = count;


        for row in reader:
            if index == 0:
                writer.writerow(["Count", "Date", "Enplaned", "Deplaned", "Thru / Transit"])
                index += 1;
                continue;

            if date != None and date != row[0] and current != row[current+1]:
                current = date;

                newrow = [];


                newrow.append(count);
                newrow.append(date);
                newrow.append(dict["Enplaned"])
                newrow.append(dict["Deplaned"])
                newrow.append(dict["Thru / Transit"])

                writer.writerow(newrow);

                #print(newrow);

                dict["Enplaned"] = 0;
                dict["Deplaned"] = 0;
                dict["Thru / Transit"] = 0;

                print(newrow);

                count += 1;

            dict[row[7]] += int(row[11])

            index += 1;

            date = row[0];

        for row in reader:
            if date =



