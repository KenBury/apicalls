import json
from data_handler import PickleDataHandler
from excel_exporter import ExcelExporter

def main(family_file_path, individual_file_path, output_path, json_text):
    # Parse the JSON input
    config = json.loads(json_text)
    family_names = config.get("family_names", [])

    # Initialize handlers
    data_handler = PickleDataHandler(family_file_path, individual_file_path)
    excel_exporter = ExcelExporter(output_path)

    # Load data
    families, individuals = data_handler.load_data()

    # Filter data based on JSON input
    filtered_families, filtered_individuals = data_handler.filter_data(families, individuals, family_names)

    # Merge data
    final_df = data_handler.merge_data(filtered_families, filtered_individuals)

    # Export to Excel
    excel_exporter.export(final_df)

if __name__ == "__main__":
    # File paths
    family_file_path = 'data/families.pkl'
    individual_file_path = 'data/individuals.pkl'
    output_path = 'family_members.xlsx'

    # Example JSON input
    json_text = '''
    {
        "family_names": ["Smith", "Johnson"]
    }
    '''

    # Execute main function
    main(family_file_path, individual_file_path, output_path, json_text)
