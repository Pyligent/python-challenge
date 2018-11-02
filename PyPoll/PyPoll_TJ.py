#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 08:52:22 2018

@author: Tao Jin
"""

import csv

# Path to collect data from the Resources folder
csvpath = 'Resources/election_data.csv'


# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    Candidate_List = []
    
    for row in csvreader:
        Name = row[2]
        Candidate_List.append(Name)


Total_Votes = len(Candidate_List)

# Creating a dictionary  
Count_Voting = {} 
for name in Candidate_List: 
    if (name in Count_Voting): 
        Count_Voting[name] += 1
    else: 
        Count_Voting[name] = 1


Winner = max(Count_Voting.keys(), key =(lambda k: Count_Voting[k]))
        

print ('Election Results \n-------------------------')

file = open('pypoll.txt','a')
file.write('Election Results \n')
file.write('----------------------------------\n')

for name in Count_Voting:
    percent_votes = Count_Voting[name]/Total_Votes
    percent_votes_format = "{:.3%}".format(percent_votes)
    print(f'{name}: {percent_votes_format} ({Count_Voting[name]})')
    file.write(f'{name}: {percent_votes_format} ({Count_Voting[name]})\n')
    
print ('------------------------- ')
print(f'Winner :{Winner}')

file.write('----------------------------------\n')
file.write(f'Winner :{Winner}')
file.close()

    
    