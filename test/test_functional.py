import unittest
import pandas as pd
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = SalesAnalysis("sales_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")

    def test_normalize_data(self):
        """Test if the data normalization is done correctly."""
        try:
            normalized_df = self.analysis.normalize_data()
            obj = 'Normalized_Units_Sold' in normalized_df.columns and 'Normalized_Price' in normalized_df.columns
            self.test_obj.yakshaAssert("TestNormalizeData", obj, "functional")
            print("TestNormalizeData = Passed" if obj else "TestNormalizeData = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestNormalizeData", False, "functional")
            print("TestNormalizeData = Failed")

    def test_export_updated_csv(self):
        """Check if the updated CSV file is saved correctly."""
        self.analysis.export_updated_csv()
        try:
            pd.read_csv("normalized_sales_data.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
        print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")
