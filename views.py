import sys
import csv

def add(i):
    with open ("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(i)
        
#add(["Toyota", "Corolla", "2333141"])
#add(["Honda", "Civic", "041132"])


# list_header = ["Car Maker", "Model", "VIN", "Plate", 
# "Year", "First Name", "Last Name", "IDNP", "Email"]

def view():
    data = []
    with open("data.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return(data)


def remove(i):
    
    def save(j):
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(j)
    
    newl = []
    vin = i
    
    with open("data.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            newl.append(row)
            
            for element in row:
                if element == vin:
                    newl.remove(row)
    save(newl)
    

def update(i):
    
    def update_newl(j):
        with open("data.csv", "w", newline="") as file:
            writer =csv.writer(file)
            writer.writerow(i)
        
    newl = []
    vin = i[0]
    
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            newl.append(row)
            
            for element in row:
                if element == vin:
                    Car_Maker = i[1]
                    Model = i[2]
                    VIN = i[3]
                    Plate = i[4]
                    Year = i[5]
                    First_Name = i[6]
                    IDNP = i[7]
                    Email = i[8]
                
                    data = [Car_Maker, Model, VIN, Plate, 
                            Year, First_Name, IDNP, Email]
                    index = newl.index(row)
                    newl[index] = data
                
                    
    update_newl(newl)

 
    
def search(i):
    data = []
    vin = i
    
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == vin:
                    data.append(row)               
    return data
