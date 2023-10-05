from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("2_Intermediate_Project/app4_pdf_invoice/invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)


# pdf = FPDF(orientation="P", unit="mm", format="A4")
