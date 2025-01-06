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

    # Extract values from the JSON properties ('id' and 'name')
    json_ids = []
    json_names = []

    # Iterate over the geometries within the 'objects' field of the JSON
    for geometry in topojson_data['objects']['world.geo']['geometries']:
        if 'properties' in geometry:
            json_ids.append(geometry['properties'].get('id', None))
            json_names.append(geometry['properties'].get('name', None))

    # Extract the corresponding columns from the CSV ('coo_iso', 'coa_iso', 'coo_name', 'coa_name')
    csv_coo_iso = csv_data['coo_iso'].unique()
    csv_coa_iso = csv_data['coa_iso'].unique()
    csv_coo_name = csv_data['coo_name'].unique()
    csv_coa_name = csv_data['coa_name'].unique()

    # Count unique values
    unique_json_ids = len(set(json_ids))
    unique_json_names = len(set(json_names))

    unique_csv_coo_iso = len(csv_coo_iso)
    unique_csv_coa_iso = len(csv_coa_iso)
    unique_csv_coo_name = len(csv_coo_name)
    unique_csv_coa_name = len(csv_coa_name)

    # Compare values between JSON and CSV
    matching_ids = set(json_ids).intersection(set(csv_coo_iso).union(set(csv_coa_iso)))
    matching_names = set(json_names).intersection(set(csv_coo_name).union(set(csv_coa_name)))

    # List non-matching values
    non_matching_ids = list(set(json_ids) - matching_ids)
    non_matching_names = list(set(json_names) - matching_names)

    # Compare the values between CSV and JSON for coo_iso, coa_iso vs id
    matching_coo_iso = set(csv_coo_iso).intersection(set(json_ids))
    matching_coa_iso = set(csv_coa_iso).intersection(set(json_ids))

    # List non-matching values in coo_iso and coa_iso
    non_matching_coo_iso = list(set(csv_coo_iso) - matching_coo_iso)
    non_matching_coa_iso = list(set(csv_coa_iso) - matching_coa_iso)

    # Compare the values between CSV and JSON for coo_name, coa_name vs name
    matching_coo_name = set(csv_coo_name).intersection(set(json_names))
    matching_coa_name = set(csv_coa_name).intersection(set(json_names))

    # List non-matching values in coo_name and coa_name
    non_matching_coo_name = list(set(csv_coo_name) - matching_coo_name)
    non_matching_coa_name = list(set(csv_coa_name) - matching_coa_name)

    # Results
    results = {
        'unique_json_ids': unique_json_ids,
        'unique_json_names': unique_json_names,
        'unique_csv_coo_iso': unique_csv_coo_iso,
        'unique_csv_coa_iso': unique_csv_coa_iso,
        'unique_csv_coo_name': unique_csv_coo_name,
        'unique_csv_coa_name': unique_csv_coa_name,
        'matching_ids': len(matching_ids),
        'matching_names': len(matching_names),
        'matching_coo_iso': len(matching_coo_iso),
        'matching_coa_iso': len(matching_coa_iso),
        'matching_coo_name': len(matching_coo_name),
        'matching_coa_name': len(matching_coa_name),
        'non_matching_ids': non_matching_ids,
        'non_matching_names': non_matching_names,
        'non_matching_coo_iso': non_matching_coo_iso,
        'non_matching_coa_iso': non_matching_coa_iso,
        'non_matching_coo_name': non_matching_coo_name,
        'non_matching_coa_name': non_matching_coa_name
    }

    return results

def display_results(results):
    """
    Function to display the comparison results in a more readable format.
    
    :param results: Dictionary with the comparison results
    """
    # Matches and unique counts
    print(f"\n{results['matching_coo_iso']} of {results['unique_csv_coo_iso']} values of 'coo_iso' match with 'id'.")
    print(f"The 'coo_iso' values that do not match with 'id' are: {results['non_matching_coo_iso']}")
    
    print(f"\n{results['matching_coa_iso']} of {results['unique_csv_coa_iso']} values of 'coa_iso' match with 'id'.")
    print(f"The 'coa_iso' values that do not match with 'id' are: {results['non_matching_coa_iso']}")
    
    print(f"\n{results['matching_coo_name']} of {results['unique_csv_coo_name']} values of 'coo_name' match with 'name'.")
    print(f"The 'coo_name' values that do not match with 'name' are: {results['non_matching_coo_name']}")
    
    print(f"\n{results['matching_coa_name']} of {results['unique_csv_coa_name']} values of 'coa_name' match with 'name'.")
    print(f"The 'coa_name' values that do not match with 'name' are: {results['non_matching_coa_name']}")

    print(f"\n{results['matching_ids']} of {results['unique_json_ids']} values of 'id' match with 'coo_iso' or 'coa_iso'.")
    print(f"The 'id' values that do not match with 'coo_iso' or 'coa_iso' are: {results['non_matching_ids']}")
    
    print(f"\n{results['matching_names']} of {results['unique_json_names']} values of 'name' match with 'coo_name' or 'coa_name'.")
    print(f"The 'name' values that do not match with 'coo_name' or 'coa_name' are: {results['non_matching_names']}")

# Example of usage
csv_file = r"path.csv"  # Sustituye con la ruta del archivo CSV
json_file = r"path.json"  # Sustituye con la ruta del archivo TopoJSON
# Load and compare data
results = load_and_compare_data(csv_file, json_file)

# Display results
display_results(results)

