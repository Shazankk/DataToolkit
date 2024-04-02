import json
from datetime import datetime
from data_toolkit import retrieve_dataset, load_dataset

def load_config(config_path: str) -> dict:
    """
    Loads database connection configuration from a JSON file.
    """
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config['database']

def main():
    # Load database connection configuration
    config_path = 'path/to/your/config.json'  # Adjust to your actual config.json path
    conn_params = load_config(config_path)

    # SQL query template with placeholders for start and end times
    query_template = """
    SELECT * FROM your_table
    WHERE time >= '{start}' AND time < '{end}'
    """

    # Define parameters for data retrieval
    start_time = datetime(2023, 1, 1)
    end_time = datetime(2023, 1, 31)
    fetch_frequency = '1H'
    aggregation_frequency = 'daily'
    save_location = 'data_output'  # Directory to save data files (optional for direct DataFrame loading)
    file_extension = 'csv'

    print("Retrieving and saving dataset...")
    # Retrieve and save dataset
    retrieve_dataset(
        conn_params=conn_params,
        query_template=query_template,
        start_time=start_time,
        end_time=end_time,
        fetch_frequency=fetch_frequency,
        aggregation_frequency=aggregation_frequency,
        save_location=save_location,
        file_extension=file_extension
    )

    print("Loading saved dataset...")
    # Load the saved dataset into a pandas DataFrame
    loaded_data = load_dataset(save_location)
    print("Loaded Data (from saved files):")
    print(loaded_data.head())

    print("\nRetrieving dataset directly into a DataFrame (without saving)...")
    # Retrieve dataset directly into a DataFrame without saving
    direct_data = retrieve_dataset(
        conn_params=conn_params,
        query_template=query_template,
        start_time=start_time,
        end_time=end_time,
        fetch_frequency=fetch_frequency,
        aggregation_frequency=aggregation_frequency,
        save_location=None,  # No save location provided for direct DataFrame loading
        file_extension=file_extension
    )
    if direct_data is not None:
        print("Directly Loaded Data:")
        print(direct_data.head())
    else:
        print("No data retrieved for direct loading.")

if __name__ == "__main__":
    main()
