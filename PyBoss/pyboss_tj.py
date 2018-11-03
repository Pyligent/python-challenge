#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:30:55 2018

@author: Tao Jin
"""

# Path to collect data from the Resources folder
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Path to collect data from the Resources folder
csvpath = 'employee_data.csv'


# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    employee_data = []
    
    for row in csvreader:
        employee_data.append(row)
        

for i in range(len(employee_data)):
    #Split the name:
    Firstname_Lastname = employee_data[i][1].split(' ')
    
    #Format the DOB:
    DOB_date = datetime.strptime(employee_data[i][2],'%Y-%m-%d')
    DOB_date_MMDDYY = datetime.strftime(DOB_date,'%m/%d/%Y')
    
    #Format the SSN
    SSN_lastfour = employee_data[i][3][6:]
    Hidden_SSN = '***-**' + SSN_lastfour
    
    # Format the State:
    State_Abbr = us_state_abbrev.get(employee_data[i][4])
    
    #Build new data list
    employee_data[i] = employee_data[i][:1] 
    employee_data[i].append(Firstname_Lastname[0])
    employee_data[i].append(Firstname_Lastname[1])
    employee_data[i].append(DOB_date_MMDDYY)
    employee_data[i].append(Hidden_SSN)
    employee_data[i].append(State_Abbr)


# Output new date file
# New Data is in employee_file.csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    for newdata in employee_data:
        employee_writer.writerow(newdata)  

