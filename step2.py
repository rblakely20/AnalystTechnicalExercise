# import packages
import pandas as pd
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

# import the csv files to a pandas dataframes
df_enroll = pd.read_csv('patient_enrollment_span.csv')
df_opvisits = pd.read_csv('outpatient_visits_file.csv')

# convert to datetimes
df_enroll['enrollment_start_date'] = pd.to_datetime(df_enroll['enrollment_start_date'], format='%Y-%m-%d')
df_enroll['enrollment_end_date'] = pd.to_datetime(df_enroll['enrollment_end_date'], format='%Y-%m-%d')
df_opvisits['date'] = pd.to_datetime(df_opvisits['date'], format='%m/%d/%Y')

results = []

# for each enrollment span in the enrollment data
for _, row in df_enroll.iterrows():
    patid = row['patient_id']
    start = row['enrollment_start_date']
    end = row['enrollment_end_date']

    # get corresponding visit data
    enrolled_visits = df_opvisits[
        (df_opvisits['patient_id'] == patid) &
        (df_opvisits['date'] >= start) &
        (df_opvisits['date'] <= end)
    ]

    # aggregate visit data that is within the enrollment span
    ct_outpatient_visits = enrolled_visits['outpatient_visit_count'].sum()
    ct_days_with_outpatient_visit = enrolled_visits['date'].nunique()

    # output aggregated data into result
    results.append({
        'patient_id': patid,
        'enrollment_start_date': start,
        'enrollment_end_date': end,
        'ct_outpatient_visits': ct_outpatient_visits,
        'ct_days_with_outpatient_visit': ct_days_with_outpatient_visit
    })

# create final dataframe
final_df = pd.DataFrame(results)

# create csv output
final_df.to_csv('result.csv', index=False)

print(final_df['ct_days_with_outpatient_visit'].nunique())