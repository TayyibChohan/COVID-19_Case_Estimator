import csv
from datetime import date

double_rate = float(input('approximate doubling time (5 is likely a fair conservative estimate): '))
time_to_death = float(input("days for an infected person to die (shown to be 20 days currently): "))
days_to_recover = float(input("days for an infected person to recover (shown to be 14 days currently): "))

current_date = date.today()  # Get Current Date

deaths = []
total_infected = 0
total_removed = 0

# import csv file and append data to array
with open('Death Dates.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x = [row[1], row[2], row[3], row[4]]
            deaths.append(x)
            line_count += 1
    print(f'Processed {line_count-1} dates.')

# calculate associated infections for each death
for i in deaths:
    death_day = date(int(i[0]), int(i[1]), int(i[2]))  # Get the date of each death
    people_infected_earlier = 100/float(i[3])
    dif = (current_date - death_day)
    days = (float(dif.days)+ time_to_death)  # Days since the intial infection
    double_periods = days/double_rate
    removed_periods = (days - days_to_recover)/double_rate
    infected = people_infected_earlier*(2**double_periods)
    removed = people_infected_earlier*(2**removed_periods)  # How many people recovered
    total_infected = total_infected + infected
    total_removed = total_removed + removed

print("approximate total infected individuals " + str(total_infected))
print("approximate total removed/cured individuals " + str(total_removed))
print("approximate net infected individuals " + str(total_infected - total_removed))
print("total deaths " + str(len(deaths)))
