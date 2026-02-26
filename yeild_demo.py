import csv
import random
import requests 

# try:
#     file = open("customers.csv","r")
#     content = file.read()
#     print(content)

# except:
#     print("Memory Error")

def read_file(file_name):
    with open(file_name,"r") as f:
        for line in f:
            yield line

# for line in read_file("customers.csv"):
#     print(line)


class WeatherMan:
    def __init__(self,name,num):
        self.generate_cities(name, num)
        

    def generate_cities(self, filename, num_rows):
        cities = [ "Lahore", "Karachi","Islamabad","Quetta","Peshawar"]
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["city", "temp"])
            for _ in range(num_rows):
                writer.writerow([random.choice(cities), random.uniform(-10, 40)])

    def stream_csv_data(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row 

    def upload_data(self, city_summary):
        
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.post(url, json=city_summary)
        return response.status_code
    
    def avg_temps(self):
        city_totals = {}

        for record in self.stream_csv_data("weather.csv"):
            city = record['city']
            temp = float(record['temp'])

            if city in city_totals:
                city_totals[city][0] +=1
                city_totals[city][1] += temp
            else:
                city_totals[city] = [0,0]
                city_totals[city][0] = 0
                city_totals[city][1] = temp
        
        return city_totals



weather_man = WeatherMan("weather.csv",1000)

avg_temps = weather_man.avg_temps()    
for key,val  in avg_temps.items():
    print(f"City:{key} Avg Temp:{float(val[1]/val[0])}")