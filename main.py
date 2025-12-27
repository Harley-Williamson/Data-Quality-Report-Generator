"""
Name: Data Quality Report Generator
Author: Harley Williamson
Description: A script which takes CSV files, and outputs a new file with an "issues" column, listing missing fields, and issues with 
the last_service_date field
"""
import argparse
import file_utils as fu



def main():
    """
    The entry point for the function, it collects arguments from the command line, and directs logic to produce the desired report.

    """
    parser = argparse.ArgumentParser(description="Data mistake repor generator.")
    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()

    data_read_from_file, fieldnames = fu.read_data(args.input_file)

    parsed_data = fu.check_for_errors(data_read_from_file, fieldnames)

    fu.write_rows_with_bad_data(parsed_data, args.output_file)

    
   # print(error_count_from_file)



if __name__ == "__main__":
    main()