# Brand Negatives in OPs Tool

## Overview
The Brand Negatives in OPs Tool is a Streamlit app designed to streamline the process of generating negative product targeting in Amazon advertising campaigns. It specifically targets campaigns prefixed with "OP_" and filters ad groups based on provided ASINs and Brand IDs. This app helps advertisers optimize their campaigns by excluding unwanted brand crossovers, thereby focusing ad spend more efficiently.

## Features
- **Ad Group Filtering**: Filters ad groups within campaigns starting with "OP_" to target specific operational campaigns.
- **ASIN Matching**: Uses ASINs as part of the filtering criteria to refine the ad groups further.
- **Brand ID Inclusion**: Includes functionality to apply negative product targeting based on specified Brand IDs.
- **Excel Output**: Generates an Excel report which allows users to download the resultant configurations for negative product targeting directly from the tool.

## How to Use
1. **Access the App**: Open the [Brand Negatives in OPs Tool](https://brandnegationtool.streamlit.app/) in your web browser.
2. **Upload a File**: Use the file uploader to select and upload your Excel file in `.xlsx` format.
3. **Specify ASINs and Brand IDs**: Enter the ASINs and Brand IDs to be used for filtering. ASINs should be entered one per line, and Brand IDs should also be listed one per line.
4. **Generate Report**: Click the "Generate Negative Product Targetings" button to process your data.
5. **Download the Results**: After processing, a link to download the Excel file will be provided. This file includes the details of your negative product targeting setup, named with a timestamp to denote the creation time.

## Input Details
- **Excel File**: Ensure the file is in `.xlsx` format.
- **ASINs**: List the ASINs you're targeting with your campaigns, separated by newlines.
- **Brand IDs**: List Brand IDs as discovered by your research, formatted as "brand=000000000", separated by newlines.

## Output Format
The output Excel file is organized with the following columns:
- **Product**
- **Entity**
- **Operation**
- **State**
- **Campaign ID**
- **Ad Group ID**
- **Product Targeting ID**
- **Product Targeting Expression**
- **Campaign Name (Informational only)**

## Discovering Brand IDs
Brand IDs can be discovered by manually adding brand negatives to any OP target and then downloading a bulk sheet to spot them under the column 'Product Targeting Expression'. Users should add the full string "brand=000000000".

## Dependencies
- Streamlit
- Pandas
- Openpyxl
- Random
- String

## App Code Structure
- `process_file`: Reads the uploaded Excel file, filters, and processes data based on user input.
- `random_alphanumeric`: Generates random alphanumeric strings for product targeting IDs.
- `Streamlit App Layout`: Defines the interactive user interface for file upload, input entry, and file download.

## Troubleshooting
- **Upload Errors**: Ensure the file is in the correct `.xlsx` format and not corrupted.
- **Data Mismatch**: Check if the ASINs and Brand IDs are correctly listed as per your operational needs.

## Support
For support or to report any issues, please contact ComprehensiveAmoeba ;)

