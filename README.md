# NYC 311 Service Requests Analysis

## How to Run

1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:

python3 analysis.py

Output will be saved to `output.txt`. The console will confirm when the file has been written.

## What This Script Does

Part 1:
My script finds the total number of open request in the csv file by adding to a variable whenever it encounters the key of open_request's value of open. It then also adds all the complaint types in the csv file and puts them in a dict with the value of how many times that complaint shows up in the csv file. I then find the complaint with the highest value and display that. I then added the boroughs to a dict counted how many times the borough shows up in the requests.

## Dependencies

This script uses only Python's built-in libraries: `csv`.

## Notes

[Optional: anything you want to flag about your approach or assumptions.]
