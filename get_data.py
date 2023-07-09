import pandas as pd
# CSV file settings
csv_file_path = "data.csv"
# Read CSV file using pandas
df = pd.read_csv(csv_file_path)
df = df.fillna("-")
# Convert CSV data into the treeview_data list
data = df.apply(lambda row: ("", "end", row.name, row.name, (row["B"], row["C"])), axis=1).tolist()

