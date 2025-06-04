Objective: Create a single CSV file containing the following 5 fields:
1. patient_id (Primary Key)
2. enrollment_start_date (Primary Key)
3. enrollment_end_date (Primary Key)
4. ct_outpatient_visits
5. ct_days_with_outpatient_visit

Step 1: Data Transformation
1. Access the patient_id_month_year.csv file: https://docs.google.com/spreadsheets/d/1nry5xBNR45TsrHKt0u1wBj7LFtrS7aN9M2O_Jb5tSvw
2. This CSV file contains two fields: patient_id and month_year.
3. Transform this dataset from patient_id x month_year level to patient_id x enrollment_start_date x enrollment_end_date level using Python.
4. Save the result as patient_enrollment_span.csv.

Step 2: Data Aggregation
1. Access the outpatient_visits_file.csv file: https://docs.google.com/spreadsheets/d/1OVLFbEYaPlw0wqY01NBlLg9TneuImg6y0VLESvGQSNc
2. This file includes three fields: patient_id, date, and outpatient_visit_count.
2. Using patient_enrollment_span.csv and outpatient_visits_file.csv, create a single CSV file with the 5 fields mentioned in the objective. Implement this using Python.
3. Save the result as result.csv.
