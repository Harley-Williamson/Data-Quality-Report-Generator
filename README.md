# Data Quality Report Generator

## Overview
This script checks CSV files for common data quality issues, including:
- Empty Fields
- Improper data in last_service_date field

## Requirements
- Python 3.12.3+
- Standard Libraries only (csv, argparse, datetime)

## Features
- CSV input/output
- CLI interface using argparse
- Clean modular design

## Usage
bash
python3 main.py input.csv output.csv