import os 
import csv

# Get the directory of the currently running script (Main.py)
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the CSV file using the relative path from the script's directory
mybudget_csv = os.path.join(script_dir, 'Resources', 'budget_data.csv')

print("+++++++++++++ This is the script's directory ++++++++++++++")
print(script_dir)
print("+++++++++++++ This is the file's location ++++++++++++++")
print(mybudget_csv)
print("*************** This is the Current Working Directory ****************")
print (os.getcwd())

# Check if the file exists and read it
if os.path.exists(mybudget_csv):
    print("File exists.")

    # Read the CSV file if it exists
    with open(mybudget_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')
        
        print(csvreader)

        csv_header = next(csvreader)
        print(f"CSV Header:")
        print(csv_header)

        months = 0
        
        cum_changes = 0
        changes = []
        first_row = next(csvreader) #positioning in the first row 
        cum_profits = int(first_row[1])
        initial_pl = int(first_row[1])#captures the first profit and loss value
        #print (initial_pl)  # wanted to verify if the value was properly captured

        # Process the CSV data
        for row in csvreader:
            final_pl = int(row[1])
            #print (f"here {final_pl} minus {initial_pl}") # used this as a control line to verify the loop
            months = months + 1
            cum_profits = cum_profits + int(row[1])
            change = final_pl - initial_pl
            #print (f"change: {change}") # used this as a control line to verify the stored value in the list
            changes.append(change)
            cum_changes = cum_changes + change
            initial_pl = final_pl # initial value of next month is the end value of current month

        length_ch = len(changes)
        average = round(cum_changes / length_ch,2)
        max_change = max(changes)
        min_change = min(changes)
    
        
        #print (f"length_ch {length_ch} and sum of changes {cum_changes} and the average is {average} ") # used to validate the sum of changes and the correct average

    results = (

        f"TOTAL MONTHS: {months}\n"
        f"TOTAL REVENUE: ${cum_profits:,}\n"
        f"AVERAGE CHANGE: ${average:,}\n"
        f"GREATEST INCREASE IN PROFITS: ${max_change:,}\n"
        f"GREATEST DECREASE IN PROFITS: ${min_change:,}"
    )

    print(results)

    # Export the results to a text file
    output_file = os.path.join(script_dir, 'analysis', 'analysis.txt')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as file:
        file.write(results)

else:
    print("File does not exist.")
