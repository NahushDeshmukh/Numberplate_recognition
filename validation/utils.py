import pandas as pd



import pandas as pd

def read_allowed_numbers(csv_file_path='/home/pi/numberplate-recognition-raspberrypi/data.csv'):
    try:
        df = pd.read_csv(csv_file_path)
        return df['Allowed'].str.lower().unique()
    except FileNotFoundError:
        print(f"CSV file not found at path: {csv_file_path}")
        return []
