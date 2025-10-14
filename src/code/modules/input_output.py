import pandas as pd
from typing import Optional
import os


class input_func:

    # Loading CSV or Excel files into a DataFrame
    def load_file(file_path: str, sheet_name: Optional[str] = None, skip_rows: Optional[int] = 0) -> pd.DataFrame:
        """
        Load a CSV or Excel file into a DataFrame.

        Parameters:
        - file_path (str): The path to the file to be loaded.
        - sheet_name (Optional[str]): The name of the sheet in an Excel file. Default is None.
        - skip_rows (Optional[int]): The number of rows to skip when loading the file. Default is 0.

        Returns:
        - DataFrame: The loaded data.
        """
        # Check the file extension to determine the file type
        file_extension = file_path.split('.')[-1].lower()
        
        try:
            if file_extension == 'csv':
                # Load CSV file
                df = pd.read_csv(file_path, sep=';', skiprows=skip_rows)
            elif file_extension in ['xls', 'xlsx', 'xlsm']:
                # Load Excel file
                df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
            else:
                raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
            print(df.shape, df.columns)
            return df
        
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

    # Example usage:
    # df1 = load_file('C:\Python repositories\Main project\data\input\mapping_file.csv')
    # df2 = load_file('C:\Python repositories\Main project\data\input\Table template.xlsx', sheet_name='Plan', skip_rows=0)


class output_func:

    # Saving in the same folder as the Python (py or ipynb) file using one of two popular Excel libraries
    def save_file(data: pd.DataFrame, name: str) -> None:
        """
        Saves a DataFrame to an Excel file using the preferred engine.
        Falls back to openpyxl if xlsxwriter is unavailable.
        """
        dump_file_name = f"{name}.xlsx"
        data_dump = os.path.join(os.getcwd(), dump_file_name)

        try:
            # Try xlsxwriter first (faster, supports formatting)
            writer = pd.ExcelWriter(data_dump, engine="xlsxwriter")
        except ModuleNotFoundError:
            print("⚠️  xlsxwriter not found. Falling back to openpyxl.")
            writer = pd.ExcelWriter(data_dump, engine="openpyxl")

        # Write to Excel
        data.to_excel(writer, sheet_name=name, index=False)

        # Save and close the writer properly
        writer.close()
        print(f"✅ Data successfully saved as: {dump_file_name}")
