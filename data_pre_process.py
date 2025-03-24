import os 
import re
from datetime import datetime




class Sale:
    def __init__(self, date, price) -> None:
        self.date = date
        self.price = price 

class DataPoint():
    def __init__(self, product_name,retial_price, sales) -> None:
        self.product_name = product_name
        self.retial_price = retial_price
        self.sales = sales


def convert_to_datetime(time_str, date_str):
    # Combine the time and date strings into one full datetime string
    full_datetime_str = f"{date_str} {time_str}"
    
    # Convert to datetime object with 24-hour time format
    datetime_obj = datetime.strptime(full_datetime_str, "%m/%d/%y %I:%M %p")
    
    return datetime_obj

def clean_file(file):
    data = list(file)
    raw_data = []
    data = [val for val in data if val !='\n']
    data = [val.strip('\n') for val in data]
    data = [val.strip('\t') for val in data]
    data = [val.strip('\CA$') for val in data]
    
    for i in range(1, len(data),2):
        
        time_date = data[i-1].split(',')
        date = time_date[0]
        time = time_date[1][1:]
        date_time_obj = convert_to_datetime(time, date)
        price = data[i]
        raw_data.append(Sale(date_time_obj, price))
        
    return raw_data
        
        

def read_data(data_dir):

    data = os.listdir(data_dir)
    cleaned_data = []
    for file in data: 
        file_name = os.path.join(data_dir, file)
        if file_name.endswith('.txt'):
            with open(file_name) as f:
                
                product_name = file[:-4]

                try:
                    retial_price = next(f).strip()
                    # print(product_name)
                    sale_data = clean_file(f)
                    cleaned_data.append(DataPoint(product_name, retial_price,sale_data ))
                except StopIteration:
                    print("END")
    return cleaned_data

### - - - Testing - - - ###
# data_dir = r'/Users/dangriffith/Library/CloudStorage/OneDrive-CarletonUniversity/Data_Sceince_Seeminar_Project/Price-Forecast-Modeling/Data'
# data = read_data(data_dir)
# print(len(data))

# for i in data: 
#     print(len(i.sales))