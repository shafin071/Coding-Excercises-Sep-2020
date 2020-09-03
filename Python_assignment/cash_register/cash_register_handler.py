import pandas as pd
from cash_register import CashRegister


class CashRegisterHandler(CashRegister):
    """
    This class inherits the functionality of CashRegister and provides the following functions on top of it:
        - Checks if the barcode and inventory data are valid
        - Pre-processes the data
        - If the previous two steps raise any exceptions then aborts the process
        - Otherwise, calculates the total after applying volume discount (if applicable)

        :param barcode: [type: string]: A string of item IDs
        :param data: [type: string]:  path to the local data file
        :param object_cols: [type: list of str]: object data type columns that need to be converted to numerical
        :return: None
    """
    def __init__(self, barcode, data, object_cols):
        self.barcode = barcode
        self.data = data
        self.object_cols = object_cols
        super(CashRegisterHandler, self).__init__(barcode)

    def _load_inventory(self):
        """
        Loads inventory info from local json file into a pandas dataframe
        :param: None
        :return: None
        """
        try:
            self.df = pd.read_json(self.data).T
        except Exception:
            raise Exception("Could not load inventory. Please check the data file path and data")

    def _preprocessor(self):
        """
        Processes both dataframe and barcode before handing them over for calculation
        - Converts selected object type data in dataframe to float and fills NaN values with 0
        - Converts all character in barcode to uppercase
        :param: None
        :return: None
        """
        for col in self.object_cols:
            self.df[col] = self.df[col].astype(float)
            self.df[col] = self.df[col].fillna(0)
        self.barcode = self.barcode.upper()

    def _validate_code(self, code):
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

    def call_cash_register(self):
        """
        - Loads, pre-processes and validates data
        - Then calls the calculate_total method from CashRegister
        :param: None
        :return: None
        """
        self._load_inventory()
        self._validate_code(self.barcode)
        self._preprocessor()
        self.calculate_total()
