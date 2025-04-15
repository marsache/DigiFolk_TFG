import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_file, train_ratio=0.8, output_train_file='train.csv', output_test_file='test.csv'):
    """
    Splits the input CSV data into train and test sets based on the specified ratio.
    
    Parameters:
        input_file (str): Path to the input CSV file.
        train_ratio (float): Ratio of data to use for training (between 0 and 1).
        output_train_file (str): Path to save the training data.
        output_test_file (str): Path to save the testing data.
    """
    # Load the dataset
    df = pd.read_csv(input_file)
    
    # Split the data into train and test sets
    train_data, test_data = train_test_split(df, train_size=train_ratio, random_state=42)

    # Save the datasets to CSV files
    train_data.to_csv(output_train_file, index=False)
    test_data.to_csv(output_test_file, index=False)

    print(f"Data has been split: {len(train_data)} rows for training, {len(test_data)} rows for testing.")
    print(f"Training data saved to: {output_train_file}")
    print(f"Testing data saved to: {output_test_file}")


if __name__ == "__main__":
    # Input file (replace with your CSV file path)
    input_csv = input("Enter the path to your input CSV file: ")

    # User defines the train-test ratio (default 80% train, 20% test)
    train_ratio = float(input("Enter the training data ratio (e.g., 0.8 for 80% train): "))

    # Output files for train and test data (you can customize these)
    output_train = 'train.csv'
    output_test = 'test.csv'

    # Run the split function
    split_data(input_csv, train_ratio, output_train, output_test)
