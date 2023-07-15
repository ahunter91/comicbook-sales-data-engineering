import pandas as pd
import random

data_files = ['Boom! Studios.csv', 'Dark Horse Comics.csv', 'DC Comics.csv', 'IDW Comics.csv', 'Image Comics.csv',
              'Marvel Comics.csv', 'VizData.csv']


comics_df = pd.concat(
    (pd.read_csv(filename, usecols=['comic_id', 'title', 'binding', 'publishing_format', 'year_published',
                                    'publisher_id', 'publisher_name']) for filename in data_files),
    ignore_index=True
)


# Generate random unit_cost for each comic book
comics_df['unit_cost'] = [round(random.uniform(9.95, 19.99), 2) for i in range(len(comics_df))]
comics_df['unit_cost'] = comics_df['unit_cost'].map('{:.2f}'.format)

comics_df.to_csv('filepath', index=False) # replace 'filepath' with your filepath