import csv
from collections import defaultdict

for year in range(2021, 2022):
    input_file = f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/district_keystone_data/district_keystone_{year}.csv"
    output_file = f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/district_keystone_data/{year}.csv"

    # A helper function to convert percentages to absolute counts
    def percentage_to_abs(percentage, student_count):
        if percentage is None:
            return None
        return (percentage / 100.0) * student_count


    # A defaultdict for aggregation
    # Key: (District, Subject, Demographic)
    # Value: dictionary storing summed data
    aggregated_data = defaultdict(lambda: {
        'total_students': 0,
        'abs_col4': 0.0,
        'abs_col5': 0.0,
        'abs_col6': 0.0,
        'abs_col7': 0.0,
        'count_col4': 0,  # to track how many rows had a non-NULL value in p4
        'count_col5': 0,
        'count_col6': 0,
        'count_col7': 0
    })

    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        # We expect columns: District, Subject, Demographic, Student_Count, p4, p5, p6, p7, Year
        # Let's define indices for clarity:
        DISTRICT_IDX = 0
        SUBJECT_IDX = 1
        DEMO_IDX = 2
        COUNT_IDX = 3
        P4_IDX = 4
        P5_IDX = 5
        P6_IDX = 6
        P7_IDX = 7
        # Year is at index 8, but we will ignore it.

        for row in reader:
            district = row[DISTRICT_IDX].strip()
            subject = row[SUBJECT_IDX].strip()
            demographic = row[DEMO_IDX].strip()

            try:
                student_count = int(row[COUNT_IDX])
            except ValueError:
                # If can't parse student count, skip row
                continue

            # null or empty strings are treated as None
            def parse_percent(val):
                val = val.strip()
                return float(val) if val and val.upper() != 'NULL' else None


            p4 = parse_percent(row[P4_IDX])
            p5 = parse_percent(row[P5_IDX])
            p6 = parse_percent(row[P6_IDX])
            p7 = parse_percent(row[P7_IDX])

            # Convert percentages to absolute counts
            abs_p4 = percentage_to_abs(p4, student_count) if p4 is not None else None
            abs_p5 = percentage_to_abs(p5, student_count) if p5 is not None else None
            abs_p6 = percentage_to_abs(p6, student_count) if p6 is not None else None
            abs_p7 = percentage_to_abs(p7, student_count) if p7 is not None else None

            # Aggregate data
            key = (district, subject, demographic)
            data = aggregated_data[key]
            data['total_students'] += student_count

            # Add absolute counts and count non-NULL values
            if abs_p4 is not None:
                data['abs_col4'] += abs_p4
                data['count_col4'] += student_count
            if abs_p5 is not None:
                data['abs_col5'] += abs_p5
                data['count_col5'] += student_count
            if abs_p6 is not None:
                data['abs_col6'] += abs_p6
                data['count_col6'] += student_count
            if abs_p7 is not None:
                data['abs_col7'] += abs_p7
                data['count_col7'] += student_count

    # Now compute final percentages
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # Write header (excluding year since we're ignoring it)
        writer.writerow(["District", "Subject", "Demographic", "Total_Students", "p4", "p5", "p6", "p7"])

        for (district, subject, demographic), vals in aggregated_data.items():
            total_students = vals['total_students']

            # To find the final percentage: (sum of absolute counts / total_students) * 100
            # If a column had no non-NULL values, leave it as None.
            def final_percentage(abs_val, count_col):
                if total_students == 0 or count_col == 0:
                    return None
                return (abs_val / total_students) * 100


            final_p4 = final_percentage(vals['abs_col4'], vals['count_col4'])
            final_p5 = final_percentage(vals['abs_col5'], vals['count_col5'])
            final_p6 = final_percentage(vals['abs_col6'], vals['count_col6'])
            final_p7 = final_percentage(vals['abs_col7'], vals['count_col7'])


            # Prepare row for output
            # Convert None back to "NULL" or leave as empty string
            def val_or_null(v):
                return v if v is not None else "NULL"

            writer.writerow([
                district,
                subject,
                demographic,
                total_students,
                val_or_null(final_p4),
                val_or_null(final_p5),
                val_or_null(final_p6),
                val_or_null(final_p7)
            ])
