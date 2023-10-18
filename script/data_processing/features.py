import pandas as pd

train_data_path = '../../data/raw/california_housing_train.csv'
test_data_path = '../../data/raw/california_housing_test.csv'

train_df = pd.read_csv(train_data_path)
test_df = pd.read_csv(test_data_path)

features = ['longitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value' ]

train_df = train_df[features + ['Capacity']]
test_df = test_df[features + ['Capacity']]

train_save_path = '../../data/train.csv'
test_save_path = '../../data/test.csv'

train_df.to_csv(train_save_path, index=False)
test_df.to_csv(test_save_path, index=False)
