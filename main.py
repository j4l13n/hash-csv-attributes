import argparse
import pandas as pd
import hashlib

def hash_columns(input_file, output_file, columns_to_hash):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Hash the specified columns
    for column in columns_to_hash:
        df[column] = df[column].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Hash specified columns in a CSV file.")
    
    # Add command-line arguments for input and output file paths
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output hashed CSV file")
    
    # Add a command-line argument for columns to hash
    parser.add_argument("columns_to_hash", nargs="+", help="Columns to hash in the CSV file")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to hash specified columns
    hash_columns(args.input_file, args.output_file, args.columns_to_hash)

    print("Hashing completed. Check the output file:", args.output_file)
