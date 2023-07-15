import pandas as pd
from sqlalchemy import create_engine

# connect to MySQL server on RDS
host = ' ' # RDS endpoint
user = ' ' # username
password = ' ' # password
database = 'comiverse_db'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


def import_csv_to_table(table_name, csv_file):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


table_csv_mapping = {
    'comics': '/filepath/comics.csv', # location of comics.csv file
    'customers': '/filepath/customers.csv', # location of customers.csv file
    'inventory': '/filepath/inventory.csv', # location of inventory.csv file
    'transactions': '/filepath/transactions.csv' # location of transactions.csv file
}

for table_name, csv_file in table_csv_mapping.items():
    import_csv_to_table(table_name, csv_file)

engine.dispose()
