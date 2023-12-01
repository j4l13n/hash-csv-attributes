# CSV Hashing Script

This Python script allows you to hash specified columns in a CSV file using the SHA-256 algorithm.

## Requirements

- Python 3
- pandas library

Install the required library using:

```bash
pip install pandas
```

Usage

```bash
python main.py input_file.csv output_file.csv column1 column2 column3 ...
```

- `input_file.csv:` Path to the input CSV file.
- `output_file.csv:` Path to the output hashed CSV file.
- `column1 column2 column3 ...:` Columns to hash in the CSV file.

Example

```bash
python main.py input_data.csv output_data_hashed.csv AMAZINA JANVIER FEVRIER MARS AVRIL MAIE JUIN JUILLET AOUT SEPTAMBRE OCTOBRE NOVEMBRE DECEMBRE TOTAL
```


The hashed CSV file will be saved with the specified columns hashed.

Note: Keep the original CSV file secure, as hashing is irreversible.

For any issues or questions, please create an issue.

Enjoy hashing your CSV data!
