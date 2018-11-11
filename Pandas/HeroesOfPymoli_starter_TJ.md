
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
```

## Player Count

* Display the total number of players



```python
total_players_df = pd.DataFrame([purchase_data['SN'].nunique()],columns = ['Total Players'])
total_players_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
unique_item = len(purchase_data['Item ID'].unique())

average_price = '${:,.2f}'.format(purchase_data['Price'].mean())

number_purchases = len(purchase_data['Purchase ID'])

Total_Revenue= '${:,.2f}'.format(purchase_data['Price'].sum())

```


```python
Summary_data = [{'Number of Unique Items': unique_item, \
                 'Average Price': average_price, \
                 'Number of Purchases': number_purchases,
                 'Total Revenue': Total_Revenue \
                }]

Purchase_Analysis_df = pd.DataFrame(Summary_data)

new_col_order = ['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']
Purchase_Analysis_df = Purchase_Analysis_df[new_col_order]

Purchase_Analysis_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed





```python
Male_df = purchase_data.loc[purchase_data['Gender'] == 'Male']
Female_df = purchase_data.loc[purchase_data['Gender'] == 'Female']
Other_df = purchase_data.loc[((purchase_data['Gender'] != 'Male')&(purchase_data['Gender'] != 'Female'))]

Total_number = purchase_data['SN'].nunique()

Male_number = Male_df['SN'].nunique()
Female_number = Female_df['SN'].nunique()
Other_number = Other_df['SN'].nunique()

male_per = '{:.2f}'.format((Male_number/Total_number)*100)
female_per = '{:.2f}'.format((Female_number/Total_number)*100)
other_per = '{:.2f}'.format((Other_number/Total_number)*100)

```


```python
Gender_data = {'Total Count':[Male_number, Female_number, Other_number],\
               'Percentage of Players':[male_per,female_per,other_per]}

Gender_df = pd.DataFrame(Gender_data, index=['Male','Female','Other/Non-Disclosed'])

Gender_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>484</td>
      <td>84.03</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.06</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>11</td>
      <td>1.91</td>
    </tr>
  </tbody>
</table>
</div>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
# Gender : Male
male_purchase_count = Male_df['Item Name'].count()
male_purchase_value = '${:,.2f}'.format(Male_df['Price'].sum())
male_average_price = '${:,.2f}'.format(Male_df['Price'].sum()/Male_df['Item Name'].count())
male_average_price_per = '${:,.2f}'.format(Male_df['Price'].sum()/Male_number)
```


```python
# Gender : Female
female_purchase_count = Female_df['Item Name'].count()
female_purchase_value = '${:,.2f}'.format(Female_df['Price'].sum())
female_average_price = '${:,.2f}'.format(Female_df['Price'].sum()/Female_df['Item Name'].count())
female_average_price_per = '${:,.2f}'.format(Female_df['Price'].sum()/Female_number)
```


```python
# Gender : Other
other_purchase_count = Other_df['Item Name'].count()
other_purchase_value = '${:,.2f}'.format(Other_df['Price'].sum())
other_average_price = '${:,.2f}'.format(Other_df['Price'].sum()/Other_df['Item Name'].count())
other_average_price_per = '${:,.2f}'.format(Other_df['Price'].sum()/Other_number)

```


```python
purchase_data_gender = [{'Gender': 'Female',\
                         'Purchase Count': female_purchase_count,\
                         'Average Purchase Price': female_average_price, \
                         'Total Purchase Value': female_purchase_value,\
                         'Avg Total Purchase per Person': female_average_price_per },\
                       {'Gender': 'Male',\
                         'Purchase Count': male_purchase_count,\
                         'Average Purchase Price': male_average_price, \
                         'Total Purchase Value': male_purchase_value,\
                         'Avg Total Purchase per Person': male_average_price_per },\
                        {'Gender': 'Other/Non-Disclosed',\
                         'Purchase Count': other_purchase_count,\
                         'Average Purchase Price': other_average_price, \
                         'Total Purchase Value': other_purchase_value,\
                         'Avg Total Purchase per Person': other_average_price_per }]

col_order = ['Gender','Purchase Count','Average Purchase Price','Total Purchase Value','Avg Total Purchase per Person']

purchase_data_gender_df = pd.DataFrame(purchase_data_gender)
purchase_data_gender_df = purchase_data_gender_df[col_order]

purchase_data_gender_df.set_index('Gender', inplace = True) 
purchase_data_gender_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Avg Total Purchase per Person</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$4.47</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1,967.64</td>
      <td>$4.07</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$4.56</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
bins = [0,9,14,19,24,29,34,39,100]
group_labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']  
```


```python
age_demographic_df = purchase_data[['SN','Age']].drop_duplicates(subset='SN', keep='last')
age_demographic_group = age_demographic_df.groupby('Age')['SN'].count()

age_demographic_group_all = age_demographic_group.groupby(pd.cut(age_demographic_group.index,bins,labels=group_labels)).sum()
age_demographic_group_all
```




    <10       17
    10-14     22
    15-19    107
    20-24    258
    25-29     77
    30-34     52
    35-39     31
    40+       12
    Name: SN, dtype: int64




```python
age_demographic_group_df = age_demographic_group_all.to_frame()
age_demographic_group_df.columns = ['Total Count']
age_demographic_group_df['Total Count'] = pd.to_numeric(age_demographic_group_df['Total Count'])

age_demographic_group_df['Percentage of Players'] = age_demographic_group_df['Total Count']/Total_number
age_demographic_group_df['Percentage of Players'] = pd.Series(["{0:.2f}".format(val * 100) for val in age_demographic_group_df['Percentage of Players']], index = age_demographic_group_df.index)
age_demographic_group_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>17</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>22</td>
      <td>3.82</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>107</td>
      <td>18.58</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>258</td>
      <td>44.79</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>77</td>
      <td>13.37</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>52</td>
      <td>9.03</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>31</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>12</td>
      <td>2.08</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
purchase_age_df = purchase_data[['Age','Item ID','Price']]
purchase_age_price = purchase_age_df.groupby('Age')['Price'].sum()
purchase_age_item = purchase_age_df.groupby('Age')['Item ID'].count()
```


```python
purchase_age_group_price = purchase_age_price.groupby(pd.cut(purchase_age_price.index,bins,labels=group_labels)).sum()

purchase_age_group_item = purchase_age_item.groupby(pd.cut(purchase_age_item.index,bins,labels=group_labels)).sum()
```


```python
purchase_age_group_price_df = purchase_age_group_price.to_frame()
purchase_age_group_price_df.columns = ['Total Purchase Price']
purchase_age_group_price_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>77.13</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>82.78</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>412.89</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>1114.06</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>293.00</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>214.00</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>147.67</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>38.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_age_group_item_df = purchase_age_group_item.to_frame()
purchase_age_group_item_df.columns = ['Purchase Count']
purchase_age_group_item_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_age_group_df = purchase_age_group_item_df.join(purchase_age_group_price_df)
purchase_age_group_df 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>77.13</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>82.78</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>412.89</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>1114.06</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>293.00</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>214.00</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>147.67</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>38.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_age_group_df['Avg Total Purchase per Person'] = purchase_age_group_df['Total Purchase Price']/age_demographic_group_df['Total Count']
purchase_age_group_df['Average Purchase Price'] = purchase_age_group_df['Total Purchase Price']/purchase_age_group_df['Purchase Count']

purchase_age_group_df['Avg Total Purchase per Person']= pd.Series(["${0:.2f}".format(val) for val in purchase_age_group_df['Avg Total Purchase per Person']], index = purchase_age_group_df.index)
purchase_age_group_df['Average Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in purchase_age_group_df['Average Purchase Price']], index = purchase_age_group_df.index)
purchase_age_group_df['Total Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in purchase_age_group_df['Total Purchase Price']], index = purchase_age_group_df.index)
```


```python
new_col_order = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Price', 'Avg Total Purchase per Person']
purchase_age_group_df = purchase_age_group_df[new_col_order]
purchase_age_group_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
      <th>Avg Total Purchase per Person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>$3.35</td>
      <td>$77.13</td>
      <td>$4.54</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$2.96</td>
      <td>$82.78</td>
      <td>$3.76</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$3.04</td>
      <td>$412.89</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$3.05</td>
      <td>$1114.06</td>
      <td>$4.32</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$2.90</td>
      <td>$293.00</td>
      <td>$3.81</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$2.93</td>
      <td>$214.00</td>
      <td>$4.12</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$3.60</td>
      <td>$147.67</td>
      <td>$4.76</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$2.94</td>
      <td>$38.24</td>
      <td>$3.19</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
top_spenders_df  = purchase_data[['SN','Item ID','Price']]
```


```python
top_spenders_price = top_spenders_df.groupby('SN')['Price'].sum()
top_spenders_item = top_spenders_df.groupby('SN')['Item ID'].count()
```


```python
top_spenders_price_df = top_spenders_price.to_frame()
top_spenders_item_df = top_spenders_item.to_frame()
```


```python
top_spenders_item_df.columns = ['Purchase Count']
top_spenders_price_df.columns = ['Total Purchase Price']
```


```python
top_spenders_price_sorted_df = top_spenders_price_df.sort_values(by=['Total Purchase Price'], ascending=False)
top_spenders_price_sorted_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>13.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_spenders_ordered_df = top_spenders_price_sorted_df.join(top_spenders_item_df)
top_spenders_ordered_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Price</th>
      <th>Purchase Count</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>18.96</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>15.45</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>13.83</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>13.62</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>13.10</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_spenders_ordered_df['Average Purchase Price'] = top_spenders_ordered_df['Total Purchase Price']/top_spenders_ordered_df['Purchase Count']


```


```python
top_spenders_ordered_df['Average Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in top_spenders_ordered_df['Average Purchase Price']], index = top_spenders_ordered_df.index)
top_spenders_ordered_df['Total Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in top_spenders_ordered_df['Total Purchase Price']], index = top_spenders_ordered_df.index)
```


```python
new_col_order = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Price']
top_spenders_ordered_df = top_spenders_ordered_df[new_col_order]
top_spenders_ordered_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>$4.61</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>3</td>
      <td>$4.37</td>
      <td>$13.10</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
popular_items_df = purchase_data[['Item ID','Item Name','Price']]
```


```python
popular_items_price = popular_items_df.groupby(['Item ID','Item Name'])['Price'].sum()
popular_items_count = popular_items_df.groupby(['Item ID','Item Name'])['Price'].count()
```


```python
popular_items_price_group_df = popular_items_price.to_frame()
popular_items_price_group_df.columns = ['Total Purchase Price']

popular_items_count_group_df = popular_items_count.to_frame()
popular_items_count_group_df.columns = ['Purchase Count']

popular_items_count_sorted_df = popular_items_count_group_df.sort_values(by=['Purchase Count'],ascending=False)


```


```python
most_popular_items_df = popular_items_count_sorted_df.join(popular_items_price_group_df)
most_popular_items_df['Item Price'] = most_popular_items_df['Total Purchase Price']/most_popular_items_df['Purchase Count']

new_col_order = ['Purchase Count', 'Item Price', 'Total Purchase Price']
most_popular_items_df = most_popular_items_df[new_col_order]

```


```python
most_popular_items_df['Item Price']= pd.Series(["${0:.2f}".format(val) for val in most_popular_items_df['Item Price']], index = most_popular_items_df.index)
most_popular_items_df['Total Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in most_popular_items_df['Total Purchase Price']], index = most_popular_items_df.index)

most_popular_items_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python
popular_items_price_sorted_df = popular_items_price_group_df.sort_values(by=['Total Purchase Price'],ascending=False)
```


```python
most_pofitable_items_df = popular_items_price_sorted_df.join(popular_items_count_group_df)
most_pofitable_items_df['Item Price'] = most_pofitable_items_df['Total Purchase Price']/most_pofitable_items_df['Purchase Count']

new_col_order = ['Purchase Count', 'Item Price', 'Total Purchase Price']
most_pofitable_items_df = most_pofitable_items_df[new_col_order]
```


```python
most_pofitable_items_df['Item Price']= pd.Series(["${0:.2f}".format(val) for val in most_pofitable_items_df['Item Price']], index = most_pofitable_items_df.index)
most_pofitable_items_df['Total Purchase Price']= pd.Series(["${0:.2f}".format(val) for val in most_pofitable_items_df['Total Purchase Price']], index = most_pofitable_items_df.index)


most_pofitable_items_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
  </tbody>
</table>
</div>


