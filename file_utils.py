"""
Name: Data Quality Report Generator file_util.py
Author: Harley Williamson
Description: File utilities to read files, check for errors, and output a new file with original data,
and a list of errors found.
"""
import csv
import datetime

def check_for_errors(data, fieldnames):
    """
    Description: Checks data from input file for missing fields, and date format issues.
    
    :param data: The data read from the input file.
    :param fieldnames: Field names which were pulled from the data read from the input file.

    Output: Returns a new list of dictionaries which includes a new field which lists issues.
    """
    
    new_field = 'issue'
    return_data = []
    missing_error= {}
    required_date_format = "%Y-%m-%d"

    if not fieldnames:
        print("File is empty, or contains no fieldnames.")
        return
    for row in data:
        for name in fieldnames:
            #print(row, name)
            if row[name] == '' or row[name] is None:
                if new_field not in row:
                    row[new_field] = r"missing data in "+name
                else:
                    row[new_field] += r", missing data in "+ name
                if row[name] not in missing_error:
                    missing_error[name] = 0
                missing_error[name] += 1
                            
                
            if name == 'last_service_date' and row[name] != '':
                date_str = row[name]
                try:
                    if not datetime.datetime.strptime(date_str, required_date_format):
                        if new_field not in row:
                            row[new_field] = r"Incorrect date format"
                        else:
                            row[new_field] = ", Incorrect date format"
                except ValueError:
                    if new_field not in row:
                        row[new_field] = r"Invalid date (not a number)"
                    else:
                        row[new_field] = ", Invalid date (not a number)"
        return_data.append(row)
    return return_data

def read_data(input_file):
    """
    Description: Takes an input file from argparse, reads it, and returns it as a list of dictionaries, along with a second list of field names.
    
    :param input_file: input file collected from argParse argument from the command line.

    Output: Returns the data from the input file, and a list of fieldnames collecte from the input file data.
    """
    return_data = []
    missing_error = {}
   
    incorrect_email_format = {}
    with open(input_file, "r") as f:
        data = csv.DictReader(f)
        fieldnames = data.fieldnames
        for row in data:
            return_data.append(row)

    return return_data, fieldnames


def write_rows_with_bad_data(data_read_from_file, output_file):
    """
    Description: Writes data out to a CSV file. The data has been checked for errors, and issues are included in a new field
    
    :param data_read_from_file: This is the data that has been read from the input file, checked for errors, and had any issues added to a new field.
    :param output_file: File name which was included in CLI, gathered from argPars arguments.
    """
    fieldnames = data_read_from_file[0].keys()
    with open(output_file, "w") as of:
        writer = csv.DictWriter(of, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_read_from_file)