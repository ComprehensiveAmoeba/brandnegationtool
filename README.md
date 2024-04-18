# Brand Negatives in OPs Tool

## Overview
The "Brand Negatives in OPs" tool is a Streamlit app designed to process Excel files and create campaigns for negative product targeting in sponsored product campaigns on platforms like Amazon. It is particularly useful for filtering campaigns based on specific criteria and automatically generating product targeting IDs.

## Features
- **OP Campaign Filtering**: Automatically filters campaigns that start with "OP_" in the campaign names.
- **Ad Group Filtering**: Filters out ad groups based on provided ASINs.
- **Automatic ID Generation**: Generates random alphanumeric IDs for product targeting.
- **Excel Output**: Produces a new Excel file with prepared negative product targeting data, ready for upload.

## How to Use
1. **Open the App**: Navigate to the Streamlit app's URL in your web browser.
2. **Upload an Excel File**: Use the file uploader to select and upload your campaign data in `.xlsx` format.
3. **Input ASINs and Brand IDs**: Enter the ASINs and Brand IDs relevant to your campaigns in the provided text areas.
4. **Generate Negative Product Targetings**: Click the "Generate Negative Product Targetings" button to process your uploaded file.
5. **Download the Results**: Once processed, a button will appear allowing you to download the newly created Excel file, which is named with a timestamp indicating the creation time.

## Input Details
- **Excel File**: Ensure the file is in `.xlsx` format and contains the necessary campaign data.
- **ASINs**: Enter the ASINs you are targeting, one per line.
- **Brand IDs**: Enter the Brand IDs for negative targeting, one per line.

## Output Format
The output Excel file contains columns such as Product, Entity, Operation, State, Campaign ID, Ad Group ID, Product Targeting ID, Product Targeting Expression, and Campaign Name.

## Dependencies
- Streamlit
- Pandas
- Openpyxl
- Random
- String
- Datetime

## App Code Structure
- `process_file`: Reads the Excel file, filters, and processes data based on specified conditions.
- `random_alphanumeric`: Generates a random alphanumeric string used as Product Targeting ID.
- `Streamlit App Layout`: Defines the interactive user interface for file upload and data entry.

## Troubleshooting
- **Upload Errors**: Check that the file is in `.xlsx` format and is not corrupted.
- **Data Mismatch**: Ensure that ASINs and Brand IDs are correctly listed as required.
- **Output Issues**: Verify the correct execution of the app if the output file does not meet expectations.

## Support
For support or to report any issues, please contact ComprehensiveAmoeba.
