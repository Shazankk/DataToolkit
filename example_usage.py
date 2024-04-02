import json
from datetime import datetime
from DataToolkit.data_toolkit import retrieve_dataset, load_dataset
from DataToolkit.performance_stats import PerformanceStats

def load_config(config_path: str) -> dict:
    """
    Loads database connection configuration from a JSON file.
    """
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config['database']

def main():
    # Load database connection configuration
    config_path = 'path/to/your/config.json'  # Ensure this points to your actual configuration file
    conn_params = load_config(config_path)

    # SQL query template with placeholders for start and end times
    query_template = "SELECT * FROM your_table WHERE your_time_column BETWEEN '{start}' AND '{end}'"

    # Define the time range for data retrieval
    start_time = datetime(2023, 1, 1)
    end_time = datetime(2023, 1, 31)

    # Initialize the PerformanceStats object to track performance metrics
    stats = PerformanceStats()

    print("Retrieving dataset and returning as DataFrame...")
    # Retrieve dataset and return it as a DataFrame (without saving)
    df = retrieve_dataset(
        conn_params=conn_params,
        query_template=query_template,
        start_time=start_time,
        end_time=end_time,
        fetch_frequency='1H',  # Adjust based on your needs
        stats=stats  # Pass the PerformanceStats object
        # Note: Not specifying save_location or file_extension, so data is returned directly
    )
    print(df.head())  # Display the first few rows of the returned DataFrame

    # To demonstrate saving data, specify save_location and file_extension
    print("Retrieving dataset and saving to files...")
    retrieve_dataset(
        conn_params=conn_params,
        query_template=query_template,
        start_time=start_time,
        end_time=end_time,
        fetch_frequency='1H',
        stats=stats,
        save_location='data_output',  # Specifying save location
        file_extension='csv'  # Specifying file extension for saving
        # Note: aggregation_frequency is optional and can be specified if needed
    )

    # Optionally, load dataset from saved files for demonstration
    print("Loading saved dataset...")
    loaded_data = load_dataset(
        path='data_output',  # Path to where data was saved
        stats=stats  # Continue tracking performance during loading
    )
    print(loaded_data.head())  # Display the first few rows of the loaded DataFrame

    # Log the performance statistics after completing all operations
    stats.log_stats()

if __name__ == "__main__":
    main()