import json
from fpdf import FPDF

with open("SD9fEIozIK5lgLne2l5K1_conversations_2023-12-27~2024-01-26.json") as f:
    data = json.load(f)
    conversations = data["conversations"]

# Create PDF instance
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_font(
    "NotoSansTC",
    style="",
    fname="/Users/vincentcheung/Desktop/font/NotoSansTC-Regular.ttf",
)
pdf.add_font(
    "NotoSansTC",
    style="b",
    fname="/Users/vincentcheung/Desktop/font/NotoSansTC-Bold.ttf",
)


# List out all conservations in this chatbot
for i, item in enumerate(conversations):
    pdf.add_page()
    createdTime = item["created_at"]
    messages = item["messages"]

    # Create Time
    pdf.set_font(family="NotoSansTC", size=14, style="B")
    pdf.cell(w=50, h=8, text="Date Created")

    pdf.set_font(family="NotoSansTC", size=14)
    pdf.cell(w=50, h=8, text=createdTime)

    pdf.line(10, 24, 200, 24)

    for message in messages:
        content = message["content"]
        pdf.set_font(family="NotoSansTC", size=14)
        pdf.cell(w=50, h=8, text=content, ln=1)


# Output PDF
pdf.output("test.pdf")
