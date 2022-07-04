# raw2parquet

This directory defines a command-line-tool to convert 1minute resolution raw signal from the Vivent PhytlSigns devices,
into a parquet dataset.

## Running the tool
Complete the following steps in order to convert the raw data into a parquet dataset:
1. Make sure you create and activate a new python virtual environment.
2. Run `pip install -r requirements.txt`
3. Install `vivraw` by running `pip install vivraw`
4. Run `python raw2parquet.py`