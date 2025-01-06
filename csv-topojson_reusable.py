import pandas as pd
import json

def load_and_compare_data(csv_file, json_file):
    """
    Function to load and compare data between a CSV file and a TopoJSON file.
    
    :param csv_file: Path to the CSV file
    :param json_file: Path to the TopoJSON file
    :return: A dictionary with the comparison results
    """

    # Load the CSV data
    csv_data = pd.read_csv(csv_file)

    # Load the TopoJSON file as a JSON object
    with open(json_file, 'r') as f:
        topojson_data = json.load(f)

    # Extract values from the JSON properties ('json_id' and 'json_name')
    json_ids = []
    json_names = []

    # Iterate over the geometries within the 'objects' field of the JSON
    for geometry in topojson_data['objects']['world.geo']['geometries']:
        if 'properties' in geometry:
            json_ids.append(geometry['properties'].get('json_prop1', None))
            json_names.append(geometry['properties'].get('json_prop2', None))

    # Extract the corresponding columns from the CSV (Replace 'column_1', 'column_2', 'column_3', 'column_4' by your the columns you need to work with)
    csv_field_1 = csv_data['column_1'].unique()
    csv_field_2 = csv_data['column_2'].unique()
    csv_field_3 = csv_data['column_3'].unique()
    csv_field_4 = csv_data['column_4'].unique()

    # Count unique values
    unique_json_ids = len(set(json_ids))
    unique_json_names = len(set(json_names))

    unique_csv_field_1 = len(csv_field_1)
    unique_csv_field_2 = len(csv_field_2)
    unique_csv_field_3 = len(csv_field_3)
    unique_csv_field_4 = len(csv_field_4)

    # Compare values between JSON and CSV
    matching_ids = set(json_ids).intersection(set(csv_field_1).union(set(csv_field_2)))
    matching_names = set(json_names).intersection(set(csv_field_3).union(set(csv_field_4)))

    # List non-matching values
    non_matching_ids = list(set(json_ids) - matching_ids)
    non_matching_names = list(set(json_names) - matching_names)

    # Compare the values between CSV and JSON for csv_field_1, csv_field_2 vs json_id
    matching_field_1 = set(csv_field_1).intersection(set(json_ids))
    matching_field_2 = set(csv_field_2).intersection(set(json_ids))

    # List non-matching values in csv_field_1 and csv_field_2
    non_matching_field_1 = list(set(csv_field_1) - matching_field_1)
    non_matching_field_2 = list(set(csv_field_2) - matching_field_2)

    # Compare the values between CSV and JSON for csv_field_3, csv_field_4 vs json_name
    matching_field_3 = set(csv_field_3).intersection(set(json_names))
    matching_field_4 = set(csv_field_4).intersection(set(json_names))

    # List non-matching values in csv_field_3 and csv_field_4
    non_matching_field_3 = list(set(csv_field_3) - matching_field_3)
    non_matching_field_4 = list(set(csv_field_4) - matching_field_4)

    # Results
    results = {
        'unique_json_ids': unique_json_ids,
        'unique_json_names': unique_json_names,
        'unique_csv_field_1': unique_csv_field_1,
        'unique_csv_field_2': unique_csv_field_2,
        'unique_csv_field_3': unique_csv_field_3,
        'unique_csv_field_4': unique_csv_field_4,
        'matching_ids': len(matching_ids),
        'matching_names': len(matching_names),
        'matching_field_1': len(matching_field_1),
        'matching_field_2': len(matching_field_2),
        'matching_field_3': len(matching_field_3),
        'matching_field_4': len(matching_field_4),
        'non_matching_ids': non_matching_ids,
        'non_matching_names': non_matching_names,
        'non_matching_field_1': non_matching_field_1,
        'non_matching_field_2': non_matching_field_2,
        'non_matching_field_3': non_matching_field_3,
        'non_matching_field_4': non_matching_field_4
    }

    return results

def display_results(results):
    """
    Function to display the comparison results in a more readable format.
    
    :param results: Dictionary with the comparison results
    """
    # Matches and unique counts
    print(f"\n{results['matching_field_1']} of {results['unique_csv_field_1']} values of 'csv_field_1' match with 'json_id'.")
    print(f"The 'csv_field_1' values that do not match with 'json_id' are: {results['non_matching_field_1']}")
    
    print(f"\n{results['matching_field_2']} of {results['unique_csv_field_2']} values of 'csv_field_2' match with 'json_id'.")
    print(f"The 'csv_field_2' values that do not match with 'json_id' are: {results['non_matching_field_2']}")
    
    print(f"\n{results['matching_field_3']} of {results['unique_csv_field_3']} values of 'csv_field_3' match with 'json_name'.")
    print(f"The 'csv_field_3' values that do not match with 'json_name' are: {results['non_matching_field_3']}")
    
    print(f"\n{results['matching_field_4']} of {results['unique_csv_field_4']} values of 'csv_field_4' match with 'json_name'.")
    print(f"The 'csv_field_4' values that do not match with 'json_name' are: {results['non_matching_field_4']}")

    print(f"\n{results['matching_ids']} of {results['unique_json_ids']} values of 'json_id' match with 'csv_field_1' or 'csv_field_2'.")
    print(f"The 'json_id' values that do not match with 'csv_field_1' or 'csv_field_2' are: {results['non_matching_ids']}")
    
    print(f"\n{results['matching_names']} of {results['unique_json_names']} values of 'json_name' match with 'csv_field_3' or 'csv_field_4'.")
    print(f"The 'json_name' values that do not match with 'csv_field_3' or 'csv_field_4' are: {results['non_matching_names']}")

# Example of usage
csv_file = r"path.csv"  # Replace with you csv path
json_file = r"path.json"  # Replace with you topojson path
# Load and compare data
results = load_and_compare_data(csv_file, json_file)

# Display results
display_results(results)
