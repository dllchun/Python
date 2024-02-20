import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob(
    "2_Intermediate_Project/app4_pdf_invoice/additional/text_files/*.txt"
)

pdf = FPDF(orientation="P", unit="mm", format="A4")


for filepath in filepaths:
    pdf.add_page()
    # header
    file_name = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=25)
    pdf.cell(w=350, h=30, txt=f"{file_name}", align="l", ln=1)

    # content
    with open(filepath) as f:
        content = f.read()
    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=0, h=6, txt=f"{content}", align="l")


pdf.output("2_Intermediate_Project/app4_pdf_invoice/additional/text.pdf")
