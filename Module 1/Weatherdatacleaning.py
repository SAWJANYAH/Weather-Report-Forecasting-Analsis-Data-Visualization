import pandas as pd
#output file
data_out = []
#counter used for year
counter = -1
counter_dict = {0: '2022', 1 : '2023', 2: '2024', 3: '2025', 4: '2026', 5: '2027', 6: '2028', 7: '2029', 8: '2030', 9: '2031', 10: '2032', 11: '2033'}

with open("weather_dataset_stage1.csv", "r", encoding='utf8') as f:
    for line in f:
        if line[0] != 'D':
            #strip the new line & ' and split with , for each line
            data_list = line.strip("\n").strip("'").split(",")
            
            if data_list[0].strip("'") == '2022-01-01':
                counter += 1
            # counter_dict has years with counter
            # Strip month ' and change the year accordingly using counter and excluding 2022
            #print(data_list[0])
            (year, month, date) = data_list[0].strip("'").split("-")
            input_year = counter_dict[counter] + "-" + month + "-" + date
            data_list[0] = input_year

            skip_rec=False
            if month == '02' and date == '29':
                if int(year)%4 != 0:
                    skip_rec = True
                    print(input_year)
            
            # Remove ' for all the data 
            for item in range(len(data_list)):
                data_list[item]=data_list[item].replace("'","")
                #Correct the data by removing ";"
                if ";" in data_list[item]:
                    print(data_list[item])
                    data_list[item]=data_list[item].replace(";","")
                    print(data_list[item])

            #removing duplicate Date and Month columns    
            data_list.pop(-3)
            data_list.pop(-2)            

            #append the output file with updated data
            #skip-rec is true for wrong dates like 2029-02-29;2033-02-29
            if not skip_rec:
                data_out.append(data_list)
        else:
            # remove ' from data
            data_list1=line.strip("\n").strip("'").split(",")

            # Remove duplicate date and Month columns
            data_list1.pop(-3)
            data_list1.pop(-2)

            #Correct the column labels
            for item in range(len(data_list1)):
                if "(" in data_list1[item]:
                    data_list1[item]=data_list1[item].split("(")[0]
            print(data_list1)
            data_out.append(data_list1)

#  Using pandas to create dataframe of processed list to create output csv file
df = pd.DataFrame(data_out)
df.to_csv("output.csv", index=False, header=False)


