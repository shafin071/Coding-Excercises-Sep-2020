from cash_register_app import DataServices


class CashRegister(DataServices):
    def __init__(self, barcode, data, object_cols):
        """
        Performs basic functions of cash register.
        - Calculates total from a shopping list presents as string of item IDs
        - Applies volume discount if applicable

        It inherits data preparation functionalities from DataServices

        :param: barcode [type: string]: List of shopping codes where each element is a string of item IDs
        :param: data [type: string]:  path to the local data file
        :param object_cols: [type: list of str]: object data type columns that need to be converted to numerical
        :return: total [type: float]: calculated total of shopping list
        """
        self.barcode = barcode
        self.initial_total = 0.0
        self.total = 0.0
        super(CashRegister, self).__init__(barcode, data, object_cols)

    def _apply_volume_discount(self):
        """
        Applies volume discount to the calculated total.
        :args: None
        :return: None
        """
        # Iterates through the bought item ids and if item count is greater then volume
        for _id in list(set(self.barcode)):
            item_count = self.barcode.count(_id)
            volume = self.df.loc[_id]['Volume']

            if item_count >= volume and volume != 0:
                cost = self.df.loc[_id]['Cost']
                discount = self.df.loc[_id]['Discount']

                # Then calculate discount per volume
                discount_per_vol = cost * volume - discount
                # Calculate the total discount for the item by multiplying discount_per_vol with the
                # number of discountable volumes (calculated by the floor division)
                # Then subtract it from the initial_total
                self.total = self.initial_total - (discount_per_vol * (item_count // volume))

                # Update the initial_total
                self.initial_total = self.total
            else:
                # Else if discount is not applicable, keep the same total value
                self.total = self.initial_total

    def calculate_total(self):
        """
        Calculates initial total, then applies volume discount on it and returns the final total
        :args: None
        :return: None
        """

        # Load data from inventory.json
        self.load_inventory()

        # Processes both DataFrame and barcode before handing them over for calculation
        self.preprocessor()

        # Validates barcode
        self.validate_code(self.barcode)

        # Iterate through the barcode and start calculating initial total
        for code in self.barcode:
            self.initial_total += self.df.loc[code]['Cost']

        # Apply volume discount if applicable
        self._apply_volume_discount()
        return round(self.total, 2)
