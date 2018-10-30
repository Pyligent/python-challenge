#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:22:36 2018

@author: Tao Jin
"""

import locale
import pandas as pd

csvpath = "Resources/budget_data.csv"
bank_pd = pd.read_csv(csvpath,encoding="utf-8")

Total_month = bank_pd['Date'].count()

Toral_net = bank_pd['Profit/Losses'].sum()

Profit_Losses_List = bank_pd['Profit/Losses'].tolist()

Average_Change_List = []
Average_Change_List_Org=[]

for i in range(1,len(Profit_Losses_List)):
    Ave_Change = Profit_Losses_List[i] - Profit_Losses_List[i - 1]
    Average_Change_List.append(Ave_Change)
    Average_Change_List_Org.append(Ave_Change)
    
Average_Change = sum(Average_Change_List)/len(Average_Change_List)

locale.setlocale( locale.LC_ALL, '')
locale.currency(Average_Change)

Average_Change_List.sort()

Greatest_Decrease = Average_Change_List[0]

Greatest_Increase = Average_Change_List[len(Average_Change_List)-1]

min_index = Average_Change_List_Org.index(Greatest_Decrease) + 1
max_index = Average_Change_List_Org.index(Greatest_Increase) + 1

Gr_Dec_Month = bank_pd['Date'][min_index]
Gr_Inc_Month = bank_pd['Date'][max_index]

# Print to console:

print('Financial Analysis')
print('----------------------------------')
print(f'Total Months: {Total_month}')
print(f'Total: {locale.currency(Toral_net)}')
print(f'Average  Change: {locale.currency(Average_Change)}')
print(f'Greatest Increase in Profits: {Gr_Inc_Month} ({locale.currency(Greatest_Increase)})')
print(f'Greatest Decrease in Profits: {Gr_Dec_Month} ({locale.currency(Greatest_Decrease)})')


# Output to file:
file = open('pybank.txt','a')

file.write('Financial Analysis\n')
file.write('----------------------------------\n')
file.write(f'Total Months: {Total_month}\n')
file.write(f'Total: {locale.currency(Toral_net)}\n')
file.write(f'Average  Change: {locale.currency(Average_Change)}\n')
file.write(f'Greatest Increase in Profits: {Gr_Inc_Month} ({locale.currency(Greatest_Increase)})\n')
file.write(f'Greatest Decrease in Profits: {Gr_Dec_Month} ({locale.currency(Greatest_Decrease)})\n')
file.close()

