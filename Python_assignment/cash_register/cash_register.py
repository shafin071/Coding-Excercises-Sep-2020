import pandas as pd


class CashRegister:
    def __init__(self, barcode):
        """
        Performs basic functions of cash register.
        - Calculates total from a shopping list presents as string of item IDs
        - Applies volume discount if applicable

        :args: barcode [type: string]: A string of item IDs
        :args: data_file [type: string]:  path to the local data file
        :return: total [type: float]: calculated total of shopping list
        """
        self.barcode = barcode
        self.df = None
        self.initial_total = 0.0
        self.total = 0.0

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

        # Iterate through the barcode and start calculating initial total
        for code in self.barcode:
            self.initial_total += self.df.loc[code]['Cost']

        # Apply volume discount if applicable
        self._apply_volume_discount()
        return round(self.total, 2)
