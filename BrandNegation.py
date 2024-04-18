import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime
import random
import string

def random_alphanumeric(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def process_file(uploaded_file, all_asins, asin_list, brand_ids):
    # Read the Excel file into a Pandas DataFrame
    xlsx = pd.ExcelFile(uploaded_file)
    sheets = [sheet for sheet in xlsx.sheet_names if "Sponsored Products Campaigns" in sheet]
    df_list = [pd.read_excel(xlsx, sheet_name=s) for s in sheets]
    df = pd.concat(df_list, ignore_index=True)

    # Filter campaigns starting with "OP_"
    df = df[df['Campaign Name (Informational only)'].str.startswith("OP_")]

    # Filter non-empty ad group names
    df = df[df['Ad Group Name'].notna()]

    # This constructs a regex pattern to match any ASINs as substrings within the Ad Group Names
    pattern = '|'.join(asin_list)  # Joins all ASINs with '|' which acts as an OR in regex
    df = df[df['Ad Group Name'].str.contains(pattern, na=False)]

    # Prepare output DataFrame
    rows = []
    for _, row in df.iterrows():
        for brand_id in brand_ids:
            new_row = {
                "Product": "Sponsored Products",
                "Entity": "Negative Product Targeting",
                "Operation": "create",
                "State": "enabled",
                "Campaign ID": row["Campaign ID"],
                "Ad Group ID": row["Ad Group ID"],
                "Product Targeting ID": random_alphanumeric(),
                "Product Targeting Expression": brand_id,
                "Campaign Name (Informational only)": row["Campaign Name (Informational only)"]
            }
            rows.append(new_row)

    result = pd.DataFrame(rows)
    return result

def main():
    st.title("Brand Negatives in OPs tool")

    uploaded_file = st.file_uploader("Choose an XLSX file", type="xlsx")
    if uploaded_file is not None:
        all_asins = st.checkbox("Process all ASINs")
        asin_list = st.text_area("Enter ASINs (one per line)").split() if not all_asins else []
        brand_ids = st.text_area("Enter Brand IDs (one per line)").split()

        if st.button("Generate Negative Product Targetings"):
            result_df = process_file(uploaded_file, all_asins, asin_list, brand_ids)
            result_file = f"brand_negative_bulksheet_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
            result_df.to_excel(result_file, index=False)
            with open(result_file, "rb") as file:
                btn = st.download_button(
                    label="Download Excel file",
                    data=file,
                    file_name=result_file,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                # Display the image below the download button
                st.image("https://thrassvent.de/wp-content/uploads/2024/04/homerOPmeme.png", caption='The reality about OPs')

if __name__ == "__main__":
    main()
