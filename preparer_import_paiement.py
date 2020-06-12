#!/usr/local/bin/python
# coding: latin-1

import csv
import sys
from decimal import *

def convert_file(input_filename):

    csv_in  = open(input_filename, "r")
    csv_reader = csv.reader(csv_in, delimiter=',', quotechar='"')

    output_filename = input_filename.replace('.csv', '_for_import.csv')
    csv_out = open(output_filename, "w")
    #write header
    csv_out.write("from;to;type;amount;description;field.MoyenPaiementEuroPart;field.DateTransactionSource;field.cle_unique_credit_particulier")
    for field_list in csv_reader:
        #strip 
        description = str(field_list[8]).replace('/','-')
        #format amount to 2 digits fixed width, deal with comma as decimal separator
        amount = str(Decimal(field_list[2].replace(",",".")).quantize(Decimal('.01'))).replace(".",",")
        date_transaction_source = str(field_list[0])
        bank_account_source = str(field_list[3])    
        unique_key_seq = (date_transaction_source, bank_account_source,description, amount)
        unique_key = '|'.join(unique_key_seq)
        seq = ('\nsystem',
    				description,   # rejoin with commas, new order
            'Emission.CreditParticulier',
            amount,
            'Crédit Particulier',
            'Virement Bancaire',
            date_transaction_source,
            unique_key)
        output_line = ';'.join(seq)
        csv_out.write(output_line)

    csv_in.close()
    csv_out.close()

if __name__ == "__main__":
    cmdargs = str(sys.argv)
    convert_file(str(sys.argv[1]))  