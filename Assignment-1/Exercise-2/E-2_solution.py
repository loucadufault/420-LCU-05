BASE_PRICE = 10*100 #in cents

#Plan A
A_FREE = 100 #number of free daytime minutes per month
A_DAYTIME = 15 #cost of additional daytime minutes, in cents
A_EVENING = 20 #cost of evening minutes, in cents
A_WEEKEND = 25 #cost of weekend minutes, in cents

#Plan B
B_FREE = 200
B_DAYTIME = 20
B_EVENING = 25
B_WEEKEND = 30

#Plan C
C_FREE = 250
C_DAYTIME = 30
C_EVENING = 35
C_WEEKEND = 40

while True: #loop until the user inputs are all validated
    try: #try to cast each str returned by input() to an int
        daytime_mins = int(input('Number of daytime minutes? ').strip()) #strip leading and trailing whitespace
        evening_mins = int(input('Number of evening minutes? ').strip())
        weekend_mins = int(input('Number of weekend minutes? ').strip())
        break #if all inputs were successfully cast to int, break out of while loop and into next section
    except TypeError:
        print('Please enter the number of minutes as an integer.')

#Plan A
a_cost = BASE_PRICE + evening_mins*A_EVENING + weekend_mins*A_WEEKEND #each plan has a cost based on the rates of evening and weekend calling, neither of which have free minutes (+ the base price)
if daytime_mins > A_FREE: #if the number of daytime minutes inputed exceeds the number of free minutes provided by the plan
    a_cost += (daytime_mins - A_FREE)*A_DAYTIME #increment the cost under this plan by the number of minutes above the free minutes threshold, multiplied by that plan's rate
#if the number of daytime minutes inputed is below the free minutes threshold, then the daytime minutes inputted come at no additional cost, and the cost under that plan remains unchanged

#Plan B
b_cost = BASE_PRICE + evening_mins*B_EVENING + weekend_mins*B_WEEKEND
if daytime_mins > B_FREE:
    b_cost += (daytime_mins - B_FREE)*B_DAYTIME

#Plan C
c_cost = BASE_PRICE + evening_mins*C_EVENING + weekend_mins*C_WEEKEND
if daytime_mins > C_FREE:
    c_cost += (daytime_mins - C_FREE)*C_DAYTIME

a_cost, b_cost, c_cost = a_cost/100, b_cost/100, c_cost/100 #convert each plan cost from cents to dollars

print('Plan A costs {:.2f}\nPlan B costs {:.2f}\nPlan C costs {:.2f}'.format(a_cost, b_cost, c_cost)) #the positional arguments (to the left of ':') in the placeholder brackets ('{}') are left empty here for automatic ordered insertion
#the format code '.2f' is used in each placeholder to round each argument to a 2 sig. figs. float

if (a_cost <= b_cost) and (a_cost <= b_cost): #find the cheapest plan and store its name (in the form of a letter) in the var cheapest_plan
    cheapest_plan = 'A'
elif (b_cost <= c_cost) and (b_cost <= c_cost): #we use '<=' instead of strictly lesser for comparaison here so that the first plan (alphabetically) is chosen in the case of multiple plans having the same cost (as per the instructions)
    cheapest_plan = 'B'
else:
    cheapest_plan = 'C'

print('choose Plan {}'.format(cheapest_plan))
