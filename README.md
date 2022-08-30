# HDB_Dataset
Quiz for one of my universities' modules.

## Quiz

Given `HDB Dataset - Feb` and `HDB Dataset - Jan`, figure out the best way to merge both files using Python.

Using the merged dataset, create at least 3 visualization charts. Each chart must be different in either the chart type of data representation.

## Usage

Run `main.py`.

### Merging

Append the corresponding file-paths to `EXCEL_FILE_LOCATIONS` array.

> `EXCEL_FILE_LOCATIONS` array should be a variable at the top of the file.

Code may not work as intended if the respective excel files do not have the same headers.

> Headers do not need to be in the same exact column, and are non-case sensitive.<p>As long as every excel file contains the same headers, the code will work.

Finally, assign the output file path into `MERGED_FILE_PATH` variable.

**Note:** *Output excel file is not sorted by anything, it just merged all the input excel files.*