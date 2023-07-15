import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# read data from the customers and comics csv files
customer_df = pd.read_csv('/filepath/customers.csv')
comic_df = pd.read_csv('/filepath/comics.csv')


# generate 11 random digits (0-9 inclusive) and add a non-zero digit at the beginning
def generate_random_transaction_id():
    return str(random.randint(1, 9)) + ''.join(str(random.randint(0, 9)) for i in range(11))


transactions_df = pd.DataFrame()

# sample 3000 rows from both customer_df and comic_df
transactions_df['customer_id'] = customer_df['customer_id'].sample(n=3000, replace=True, ignore_index=True)
transactions_df['comic_id'] = comic_df['comic_id'].sample(n=3000, replace=True, ignore_index=True)

# merge with comic_df to fetch the corresponding unit_cost
transactions_df = pd.merge(transactions_df, comic_df[['comic_id', 'unit_cost']], on='comic_id', how='left')

# generate 3000 random transaction dates within the last 3 years
transaction_dates = pd.date_range(end=pd.to_datetime('today'), periods=3000).tolist()
transactions_df['transaction_date'] = pd.Series(transaction_dates).sample(n=3000, replace=True).sort_values().reset_index(drop=True)

# generate random quantity between 1 and 10
transactions_df['quantity'] = pd.Series([random.randint(1, 10) for i in range(3000)])

# generate random transaction_id
transactions_df['transaction_id'] = pd.Series([generate_random_transaction_id() for i in range(3000)])

# calculate total_amount based on quantity and unit_cost
transactions_df['total_amount'] = transactions_df['quantity'] * transactions_df['unit_cost']

# format unit_cost and total_amount as strings with 2 decimal places
transactions_df['unit_cost'] = transactions_df['unit_cost'].map('{:.2f}'.format)
transactions_df['total_amount'] = transactions_df['total_amount'].map('{:.2f}'.format)

# save transactions_df to transactions.csv
transactions_df.to_csv('/filepath/transactions.csv', index=False)
