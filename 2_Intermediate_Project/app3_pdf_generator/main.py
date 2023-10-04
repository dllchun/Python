import pandas as pd
from fpdf import FPDF

df = pd.read_csv("2_Intermediate_Project/app3_pdf_generator/topics.csv")
pdf = FPDF("P", "mm", "A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="l", ln=1)
    pdf.line(10, 22, 200, 22)

    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)

    # footer
    pdf.ln(255)
    pdf.set_font(family="Times", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(255)
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="R", ln=1)

        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output(
    "/Users/vincentcheung/Desktop/Coding/Python-1/2_Intermediate_Project/app3_pdf_generator/test.pdf"
)
