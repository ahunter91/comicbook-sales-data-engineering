import pandas as pd
from faker import Faker
import random


# define customer profile generation
def generate_customer_profiles(records):
    fake = Faker('en_US')
    customers = []
    used_customer_ids = set()
    used_loyalty_ids = set()

# unique ID for customers - no two customers should be assigned the same ID; IDs cannot begin with 0 but can contain 0
    def generate_unique_id(length):
        while True:
            unique_id = ''.join(random.choices('0123456789', k=length - 1)) 
            unique_id = random.choice('123456789') + unique_id 
            if unique_id not in used_customer_ids:
                return unique_id

# unique loyalty program ID - no two loyalty IDs should be the same; IDs cannot begin with 0
    def generate_unique_loyalty_id(length):
        while True:
            unique_id = ''.join(random.choices('0123456789', k=length - 1))
            unique_id = random.choice('123456789') + unique_id 
            if unique_id not in used_loyalty_ids:
                return unique_id

    for i in range(records):
        customer_id = generate_unique_id(10)
        used_customer_ids.add(customer_id)
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = str.lower(f"{first_name}.{last_name}@fake_domain.com")
        address = fake.street_address()
        city = fake.city()
        state = fake.state_abbr()
        zip_code = fake.postcode()

        # Generate 10-digit phone number in the format of ###-###-####
        phone_number = fake.numerify(text="###-###-####")

        # loyalty membership random. if membership exists, points balance exists. if no membership, points = null
        loyalty_id = generate_unique_loyalty_id(8) if fake.random_element([True, False]) else ''
        used_loyalty_ids.add(loyalty_id)

        # loyalty points balance between 0 and 100,000
        loyalty_points = fake.random_int(0, 100000)

        customers.append({
            'customer_id': customer_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip_code,
            'phone_number': phone_number,
            'loyalty_id': loyalty_id,
            'loyalty_points': loyalty_points,
        })

    return customers

# define number of profiles (rows) to generate and export DataFrame to CSV file
customer_df = pd.DataFrame(generate_customer_profiles(1000))
customer_table = customer_df.to_csv('/filepath/customers.csv', index=False)
