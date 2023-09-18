# raw2parquet

This directory defines a command-line-tool to convert 1minute resolution raw signal from the Vivent PhytlSigns devices,
into a parquet dataset.

## Running the tool
Complete the following steps in order to convert the raw data into a parquet dataset:
1. Make sure you create and activate a new python virtual environment.
2. Run `pip install -r requirements.txt`
3. Install `vivraw` by running `pip install vivraw`
4. [Bug in requirement!] if you are running a version of python greater than 3.10, please do the following:
   1. As per the bug report [here](https://github.com/CITGuru/PyInquirer/issues/198), navigate to
   `prompt_toolkit/styles/from_dict.py` in your virtual environment site packages. 
   2. Change the import from `from collections import Mapping` to `from collections.abc import Mapping`.
5. Run `python raw2parquet.py`
