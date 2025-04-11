import pandas as pd

class SalesAnalysis:
    def __init__(self, file_path):
        pass
        """Load CSV data into a Pandas DataFrame."""
        # self.df = pd.read_csv(file_path)

    def display_head(self):
        pass
        """Return the first 5 rows of the DataFrame."""
        # return self.df.head()

    def dataframe_info(self):
        pass
        """Return DataFrame column names and data types."""
        # return self.df.info()

    def normalize_data(self):
        pass
        """Normalize 'Units Sold' and 'Price' using Min-Max scaling."""
        # self.df['Normalized_Units_Sold'] = self.df['Units_Sold'].apply(
        #     lambda x: (x - self.df['Units_Sold'].min()) / (self.df['Units_Sold'].max() - self.df['Units_Sold'].min())
        # )
        # self.df['Normalized_Price'] = self.df['Price'].apply(
        #     lambda x: (x - self.df['Price'].min()) / (self.df['Price'].max() - self.df['Price'].min())
        # )
        # return self.df

    def export_updated_csv(self, output_file="normalized_sales_data.csv"):
        pass
        """Save the normalized DataFrame to a new CSV file."""
        # self.df.to_csv(output_file, index=False)
