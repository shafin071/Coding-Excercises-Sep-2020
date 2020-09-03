import json

from cash_register import CashRegisterHandler
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
    for barcode in barcodes:
        print(f"\n********* Order: {barcode} *********")
        cr = CashRegisterHandler(barcode=barcode, data=data_file_path, object_cols=object_cols)
        cr.call_cash_register()
        print(f"Your total after applying applicable volume discount is: ${round(cr.total, 2)}\n")
        output_dict[cr.barcode] = round(cr.total, 2)

    # Create new output file in the output_file_path and stores the result in that file in JSON format
    # If the file is present, it'll be overwritten with updated results
    with open(output_file_path, 'w') as f:
        json.dump(output_dict, f)


if __name__ == '__main__':
    run_cash_register(barcodes=shopping_codes,
                      data_file_path=data_file,
                      object_cols=object_columns,
                      output_file_path=output_file)
