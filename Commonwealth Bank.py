#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the uploaded Excel file
file_path = 'supermarket_transactions.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
df.head()


# In[2]:


# Task 1: Count of Apples Purchased in Cash
apples_cash = df[(df['product_name'] == 'apple') & (df['payment_method'] == 'cash')]
total_apples_cash = apples_cash['quantity'].sum()

# Task 2: Total Cash Spent on Apples
total_cash_spent_on_apples = apples_cash['total_amount'].sum()

# Task 3: Money Spent by Non-Member Customers at Bakershire
bakershire_non_members = df[(df['store'] == 'Bakershire') & (df['customer_type'] == 'non-member')]
total_spent_bakershire_non_members = bakershire_non_members['total_amount'].sum()

total_apples_cash, total_cash_spent_on_apples, total_spent_bakershire_non_members


# In[4]:


# Save the results and formulas in an Excel file for submission

# Create a new DataFrame to hold the results
results = {
    'Metric': ['Total Apples Purchased in Cash', 'Total Cash Spent on Apples', 'Total Spent by Non-Members at Bakershire'],
    'Value': [total_apples_cash, total_cash_spent_on_apples, total_spent_bakershire_non_members]
}

results_df = pd.DataFrame(results)

# Save the results to a new Excel file
results_file_path = 'supermarket_analysis_results.xlsx'
results_df.to_excel(results_file_path, index=False)

results_file_path


# In[5]:


import pandas as pd

# Load the provided Excel file
file_path = 'mobile_customers.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()


# In[5]:


import pandas as pd

# Load the provided Excel file
file_path = 'mobile_customers.xlsx'
data = pd.read_excel(file_path)

# Remove sensitive columns
columns_to_remove = [
    'Unnamed: 0', 'customer_id', 'username', 'name', 'email', 'address',
    'residence', 'credit_card_number', 'credit_card_security_code', 'credit_card_expire'
]
anonymized_data = data.drop(columns=columns_to_remove)

# Generalize job titles
anonymized_data['job'] = anonymized_data['job'].apply(lambda x: 'Professional' if 'Officer' in x or 'Scientist' in x else 'Other')

# Generalize birthdate to age brackets
def age_bracket(age):
    if age < 20:
        return '<20'
    elif 20 <= age < 30:
        return '20-29'
    elif 30 <= age < 40:
        return '30-39'
    elif 40 <= age < 50:
        return '40-49'
    elif 50 <= age < 60:
        return '50-59'
    else:
        return '60+'

anonymized_data['age'] = anonymized_data['age'].apply(age_bracket)

# Generalize salary to salary brackets
def salary_bracket(salary):
    if salary < 30000:
        return '<30k'
    elif 30000 <= salary < 60000:
        return '30k-60k'
    elif 60000 <= salary < 90000:
        return '60k-90k'
    elif 90000 <= salary < 120000:
        return '90k-120k'
    elif 120000 <= salary < 150000:
        return '120k-150k'
    else:
        return '150k+'

anonymized_data['salary'] = anonymized_data['salary'].apply(salary_bracket)

# Mask current location by rounding coordinates
def mask_location(location):
    coords = eval(location)
    return [round(float(coords[0]), 1), round(float(coords[1]), 1)]

anonymized_data['current_location'] = anonymized_data['current_location'].apply(mask_location)

# Save the anonymized data to a CSV file
anonymized_file_path = 'anonymized_mobile_customers.csv'
anonymized_data.to_csv(anonymized_file_path, index=False)

# Display the first few rows of the anonymized data
print(anonymized_data.head())

anonymized_file_path

