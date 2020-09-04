import pandas as pd


class DataServices:
    """
    This class prepares the data required by CashRegister to calculate the total bill
        - Checks if the barcode and inventory data are valid
        - Pre-processes the data
        - If the previous two steps raise any exceptions then aborts the process


        :param df: [type: Pandas DataFrame]: It will hold the loaded data from inventory.json
        :param barcode: [type: string]: A string of item IDs
        :param data: [type: string]:  path to the local data file
        :param object_cols: [type: list of str]: object data type columns that need to be converted to numerical
        :return: None
    """
    def __init__(self, barcode, data, object_cols):
        self.df = None
        self.barcode = barcode
        self.data = data
        self.object_cols = object_cols


    def load_inventory(self):
        """
        Loads inventory info from local json file into a pandas dataframe
        :param: None
        :return: None
        """
        try:
            self.df = pd.read_json(self.data).T
        except Exception:
            raise Exception("Could not load inventory. Please check the data file path and data")

    def preprocessor(self):
        """
        Processes both DataFrame and barcode before handing them over for calculation
        - Converts selected object type data in dataframe to float and fills NaN values with 0
        - Converts all character in barcode to uppercase
        :param: None
        :return: None
        """
        for col in self.object_cols:
            self.df[col] = self.df[col].astype(float)
            self.df[col] = self.df[col].fillna(0)
        self.barcode = self.barcode.upper().replace(" ", "")

    def validate_code(self, code):
        """
        Validates:
        - If the barcode is empty or it's not of type string
        - If there is any code that's not present in the current inventory
        If validation fails, throws exception and aborts calculation
        :param code: [type: string]: A string of item IDs
        :return: None
        """
        if not code or not isinstance(code, str):
            raise Exception(f"{code} is not a valid barcode. Please enter barcode in string format")
        for char in code:
            if char.upper() not in self.df.index:
                raise Exception(f"This code: {char} is not available in the inventory")


