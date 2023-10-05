from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("2_Intermediate_Project/app4_pdf_invoice/invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    file_name = Path(filepath).stem
    invoice_nr = file_name.split("-")[0]
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Inovice nr {invoice_nr}")

    pdf.output(f"2_Intermediate_Project/app4_pdf_invoice/invoices/{invoice_nr}.pdf")
