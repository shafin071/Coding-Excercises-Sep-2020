import json

from cash_register_app import CashRegister
from config import data_file, output_file, object_columns

shopping_codes = ["ABCD", "DCCBAABB"]


def run_cash_register(barcodes, data_file_path, object_cols, output_file_path):
    """
    - Calls the Cash Register Handler and passes required params to it:
    - Writes calculated total to a json file

    :param barcodes: [type: list of str]: Each element is a string of item IDs
    :param data_file_path: [type: string]:  path to the local data file
    :param object_cols: [type: list of str]: object data type columns that need to be converted to numerical
    :param output_file_path: [type: string]:  path to the output data file
    :return: None
    """
    output_dict = {}

    order_num = 0
    for barcode in barcodes:
        cr = CashRegister(barcode=barcode, data=data_file_path, object_cols=object_cols)
        cr.calculate_total()

        print(f"\n********* Order: {cr.barcode} *********")
        print(f"Your total after applying applicable volume discount is: ${round(cr.total, 2)}\n")

        # Adding an order number to output in case there are multiple orders with the same barcode
        order_num += 1
        output_dict[order_num] = {'order_code': cr.barcode, 'order_total': round(cr.total, 2)}

    # Create new output file in the output_file_path and stores the result in that file in JSON format
    # If the file is present, it'll be overwritten with updated results
    with open(output_file_path, 'w') as f:
        json.dump(output_dict, f)


if __name__ == '__main__':
    run_cash_register(barcodes=shopping_codes,
                      data_file_path=data_file,
                      object_cols=object_columns,
                      output_file_path=output_file)
