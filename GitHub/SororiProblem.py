import numpy as np
import matplotlib.pyplot as plt


#Question 1
FirstDayGrain=1
Grain_of_day=0
total_of_grain=0
ListGrain=[]

for i in range(100):

    if i<1 :
        total_of_grain=FirstDayGrain
        Grain_of_day=FirstDayGrain
        ListGrain.append(total_of_grain)
        #print(Grain_of_day, "Day: ",i)
    Grain_of_day=Grain_of_day*2
    #print(Grain_of_day, "Day: ",i+1)
    total_of_grain=total_of_grain+Grain_of_day
    ListGrain.append(total_of_grain)
print("the amount of total grains is : {}".format(total_of_grain))

plt.title("Graines of rice")
plt.xlabel("Days")
plt.ylabel("Qtd Grains")
plt.plot(ListGrain)
plt.show()

# Question 2
# Manual input for number of days
def Sorori_Problem_function(Manual_Days):
    FirstDay=1
    Grain=0
    sum=0
    list_grain=[]

    for i in range(Manual_Days):
        if i<1 :
            sum=FirstDay
            Grain=FirstDay
            list_grain.append(sum)
        else:
            Grain=Grain*2
            sum=sum+Grain
            list_grain.append(sum)
    print("the amount of total grains is : {}".format(sum))
    
    plt.title("Graines of rice")
    plt.xlabel("Days")
    plt.ylabel("Qtd Grains")    
    plt.plot(list_grain)
    plt.show()

    return list_grain

Manual_Days=int(input("Insert the number of days to receive the grain : " ))
print(Sorori_Problem_function(Manual_Days))

# Question 3
# How many people can survive for how many days 

# On average a person needs between 1,500 and 2,500 calories a day ...for my teste i'm going to base it on 2,000 calories,
# a single grain of rice is known to have 0.025 grams. And white rice has 3.5 calories per gram of rice
# so a single grain would provide 0.025 x 3.5 == 0.0875 calories per grain 
# to achieve 2,000 calories we must do the following.
# 2000/0.0875==22,875 grains of white rice (interger)

def Sorori_Problem_Survival(Survive):
    FirstDay=1
    Grain=0
    sum=0
    list_grain=[]

    for i in range(Survive):
        if i<1 :
            sum=FirstDay
            Grain=FirstDay
            list_grain.append(sum)
        else:
            Grain=Grain*2
            sum=sum+Grain
            list_grain.append(sum)
 
    return sum

Survive=int(input("Insert the number of days to receive the grain : " ))
people=int(input("Insert the amount of people: "))

avg_grain=22875
day=0

Grain_Used=Sorori_Problem_Survival(Survive)

while Grain_Used>=avg_grain:
    day+=1
    for i in range (people):
        if Grain_Used<avg_grain:
            print("there isn't enough grain for the {} person on day {}".format(i,day))
            break
        Grain_Used=Grain_Used-avg_grain
print("{} (person/people) can survive {} days with {} of grain".format(people,day,Sorori_Problem_Survival(Survive)))
