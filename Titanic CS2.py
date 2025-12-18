def print_data(data):
    '''
    Finds and loads the titanic.csv file and display the first 10 rows
    Args:
        data(int,str): data from excel spreadsheet
    Returns:
        display and writes the first 10 rows to an excel file
    '''
    with open('print_data_csv.csv', 'w') as print_data:                #writes out to an excel file
        #data = open('titanic.csv')
        counter = 0
        for line in data:
            data = line.split(",")

            excel = f'''{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}, {data[8]}, {data[9]}'''    
            print_data.write(excel + "\n")
            counter = counter + 1
            if counter == 10:
                break


def gender_count(file):
    '''
    countes the amount of men and women aboard the titanic
    Args:
        data(int,str): data from excel spreadsheet
    Returns:
        display and writes amount of men and women to an excel file
    '''
    male_count = 0
    female_count = 0

    for line in file:
        data = line.split(",")              #splits data by the comma 
        if data[5] == 'male':
            male_count += 1
        elif data[5] == "female": 
            female_count += 1

    excel = f'''There were this many males:, There were this many females:,
    {male_count}, {female_count}'''
 
    with open('gender_count.csv', 'x') as gender_count:
        gender_count.write(excel)

def survival_rate(file):
    '''
    calculates the survival rate and death rate
    Args:
        data(int,str): data from excel spreadsheet
    Returns:
        display and writes survival and death percentages to an excel file
    '''
    survival_count = 0
    total_count = 0

    for line in file:                                       #iterate through the data
        total_count += 1
        data = line.split(",")
        if data[1] == '1':
            survival_count += 1

    survival_rate = survival_count/total_count              #find survival rate by survival count divided by total count
    excel = f'''percentage of people who survived, percentage of people who died,
    {(survival_rate*100):.2f}%, {((1 - survival_rate)*100):.2f}%'''
 
    with open('survival_rate.csv', 'x') as survival_rate_file:
        survival_rate_file.write(excel)
    

def survival_by_gender(file):
    '''
    calculates the survival rate and death rate depending on gender 
    Args:
        data(int,str): data from excel spreadsheet
    Returns:
        display and writes survival and death percentages depending on gender to an excel file
    '''
    male_count = 0
    female_count = 0
    total_count = 0

    for line in file:
        total_count += 1
        data = line.split(",")
        if data[5] == 'male' and data [1] == '1':                          #if both male and survived 
            male_count += 1
        elif data[5] == "female" and data [1] == '1':                      #if both female and survived 
            female_count += 1

    male_survival_rate = male_count/total_count
    female_survival_rate = female_count/total_count

    excel = f'''percentage of males who survived, percentage of females who survived,
    {(male_survival_rate*100):.2f}%, {((female_survival_rate)*100):.2f}%'''
    
    with open('gender_survival_rate.csv', "w") as gender_survival_rate:
            gender_survival_rate.write(excel)
    
    
def age_analysis(data):
    '''
    calculates the average age of Passengers, average age of surviving Passengers, average age of dead passengers, oldest passenger, and youngest passenger
    Args:
        data(int,str): data from excel spreadsheet
    Returns:
        display and writes the average age of Passengers, average age of surviving Passengers, average age of dead passengers, oldest passenger, and youngest passenger to an excel file
    '''
    data.readline()

    age = 0
    total_ages = 0
    surv_total_ages = 0
    dead_total_ages = 0
    dead_counter = 0
    counter = 0
    surv_counter = 0
    
    for line in data:
        
        passenger = line.split(",") 

        counter += 1 
        age = passenger[6]
        if len(age) == 0:
            age = 0
        total_ages = total_ages + float(age)                           #add total ages plus next age it iterated through to find total ages                 
         
        if passenger[1] == '1':
            surv_counter +=1 
            age = passenger[6]                  
            if age == "":
                age = 0
            surv_total_ages = surv_total_ages + float(age)             #add total ages plus next age it iterated through to find total ages
        
        elif passenger[1] == '0':
            dead_counter +=1 
            age = passenger[6]
            if age == "":
                age = 0
            dead_total_ages = dead_total_ages + float(age)              #add total ages plus next age it iterated through to find total of dead ages

    
    oldest_passenger = 0
    data.seek(1)
    ages = passenger[6]
    for line in data: 
        passenger = line.split(',')
        if passenger[5] == "Age":
            pass
        else:
            if passenger[6] == '':                          #if age is zero, continue
                pass
            else:
                ages = float(passenger[6])
                if ages != "": 
                    if ages > oldest_passenger:             #if age of passenger is greater than oldest passenger
                        oldest_passenger = ages             #age becomes oldest passenger
                else:
                        ages = 0


    youngest_passenger = 100
    data.seek(1)                                            #skip the first line (header)
    next(data)

    for line in data:                                       #iterate through data
        passenger = line.strip().split(',')

        if passenger[6] == '':
            continue
        else:
            age = float(passenger[6])
            
            if age == 0:                                   #if age is zero, continue
                continue
            elif age < youngest_passenger:                 #if age of passenger is less than the youngest passenger
                youngest_passenger = age                    #age becomes youngest passenger

    average = total_ages/counter
    alive_average = surv_total_ages/surv_counter
    dead_average = dead_total_ages/dead_counter


    excel = f'''Average age of Passengers, average age of Surviving Passengers, average age of dead passengers, oldest passenger, youngest passenger
    {(average):.2f}, {((alive_average)):.2f}, {((dead_average)):.2f}, {((oldest_passenger)):.2f}, {((youngest_passenger)):.2f}'''

    with open('age_analysis.csv', "w") as age_analysis_file:
        age_analysis_file.write(excel)
         

def main():
    
    data = open('titanic.csv', 'r')

    while True:
        option = input('''What would you like to do?
                       1. Print first 10 rows of Data 
                       2. Find amount of males and females on titanic
                       3. find the survival and death rate by gender 
                       4. Find the average age of Passengers, average age of surviving Passengers, 
                       average age of dead passengers, oldest passenger, and youngest passenger''')
        if option == "1":
            print_data(data)
        elif option == "2":
            gender_count(data)
        elif option == "3":
            survival_by_gender(data)
        elif option == "4":
            age_analysis(data)
        elif option == "stop":
            break

main()


