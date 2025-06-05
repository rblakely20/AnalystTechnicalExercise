# import packages
import pandas as pd
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

# import the csv file to a pandas dataframe
df = pd.read_csv('patient_id_month_year.csv')

# convert the month_year field to a datetime and rename
# must do before sorting or dates won't sort correctly
df['enrollment_start_date'] = pd.to_datetime(df['month_year'], format='%m/%d/%Y')
del df['month_year']

# sort the data
df=df.sort_values(by=['patient_id','enrollment_start_date'])

# create a function that takes in a list of months and condenses them based on consecutive months
def condense_months(months):
    condensed_months = []
    start = months[0]
    prev = start

    # for each month in the list, loop through and check if it is consecutive with the previous month in the list
    for curr in months[1:]: 
        if curr != prev + relativedelta(months=1): 
            # if current month is not one greater than prior month, then prior is the end of a pair and a new span is defined
            condensed_months.append((start, prev))
            start = curr # current month is now the new start month for the next span until a new end is found
        prev = curr
    condensed_months.append((start, prev)) # add each span found to the condensed months list
    return condensed_months 

results = []

# for each patient id, get the list of months and apply condensed months logic defined above
for patient_id, months in df.groupby('patient_id'):
    condensed_months = condense_months(months['enrollment_start_date'].tolist())
    # for each condensed months pairing define a record with patient id, start, and end, updating the end date to be the end of the month
    for start, end in condensed_months:
        results.append({
            'patient_id': patient_id,
            'enrollment_start_date': start,
            'enrollment_end_date': (end + relativedelta(months=1) - timedelta(days=1))
        })

# create final dataframe
final_df = pd.DataFrame(results)

# create csv output
final_df.to_csv('patient_enrollment_span.csv', index=False)

print(len(final_df))