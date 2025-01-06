# CSV and TopoJSON Comparison Tool

Hi!👋
This Python script is designed to help you compare data from a CSV file with a TopoJSON file. It identifies matching and non-matching elements between specified fields in both files and provides detailed results for analysis.

## Features 👌
- Compare fields in the CSV file with properties in the TopoJSON file.
- Generate insights about matching and non-matching values.
- Outputs a summary of unique values and matches for easier analysis.

## Requirements ✅
- Python 3.6 or higher.
- Libraries:
	- pandas
	- json (standard Python library)

## How to use 🤔
### 1. Edit the Script

##### File Paths: 
Update the csv_file and json_file variables to the paths of your CSV and TopoJSON files (Line 119 and 120:

    csv_file = r"path_to_your_csv_file.csv"
    json_file = r"path_to_your_topojson_file.json"

##### CSV Columns:
Replace the placeholder names in the script (column_1, column_2, etc.) with the actual column names in your CSV file that you wish to compare (Line 30):

    # Extract the corresponding columns from the CSV (Replace 'column_1', 'column_2', 'column_3', 'column_4' by your the columns you need to work with)
    
        csv_field_1 = csv_data['column_1'].unique()
        csv_field_2 = csv_data['column_2'].unique()
        csv_field_3 = csv_data['column_3'].unique()
        csv_field_4 = csv_data['column_4'].unique()
    

##### JSON Properties: 
Update json_prop1 and json_prop2 with the property names in the TopoJSON file you wish to compare (Line 24):

        # Iterate over the geometries within the 'objects' field of the JSON
       
    for geometry in topojson_data['objects']['world.geo']['geometries']:
            if 'properties' in geometry:
                json_ids.append(geometry['properties'].get('json_prop1', None))
                json_names.append(geometry['properties'].get('json_prop2', None))

You may also need to modify the values under ['objects']['world.geo']['geometries'] depending on how they are named in your topoJson file.

### 2. Run the Script ⚙️
Save your changes to the script and run it in a Python environment:

The script will display:

Count of unique values in each column.
Number of matches and non-matches between fields.
Lists of non-matching values for deeper analysis.

## Use example 💡
You can find an example of this code implementation in /example. 

There, you will find the CSV file, the TopoJSON file, and the adapted script.


------------


#### 👐 I hope this script helps you save time when working with maps and data.

------------

