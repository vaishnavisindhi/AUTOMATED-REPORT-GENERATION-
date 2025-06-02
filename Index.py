# Auto-installing reportlab
import subprocess
import sys

try:
    from reportlab.lib.pagesizes import letter
except ImportError:
    print("Installing required library: reportlab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    print("Installation complete.\n")
    from reportlab.lib.pagesizes import letter

import pandas as pd
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


data = pd.DataFrame({
    'Sales': [1000, 1500, 1200],
    'Cost': [400, 500, 450],
    'Profit': [600, 1000, 750]
})


summary = data.describe().reset_index()


pdf_file = 'sample_report.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

styles = getSampleStyleSheet()
story = []

title = Paragraph("Internship Report – Data Analysis", styles['Title'])
name = Paragraph("Prepared by: Sindhi Vaishnavi", styles['Normal'])
org = Paragraph("Organization: COD TECH IT SOLUTIONS", styles['Normal'])
report_date = Paragraph("Date: 01/06/2025", styles['Normal'])

story.extend([title, Spacer(1, 12), name, org, report_date, Spacer(1, 24)])


intro_text = (
    "This report presents a basic analysis of Sales, Cost, and Profit data "
    "as part of the internship project at COD TECH IT SOLUTIONS. "
    "The dataset used here is simulated and created directly in the script."
)
story.append(Paragraph(intro_text, styles['Normal']))
story.append(Spacer(1, 12))

table_data = [summary.columns.tolist()] + summary.values.tolist()

for i in range(1, len(table_data)):
    for j in range(1, len(table_data[i])):
        if isinstance(table_data[i][j], float):
            table_data[i][j] = f"{table_data[i][j]:.2f}"

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
]))

story.append(table)
story.append(Spacer(1, 12))

conclusion = (
    "This concludes the data summary. In future stages of the project, real-time data can be analyzed, "
    "visualized, and automatically compiled into detailed reports."
)
story.append(Paragraph(conclusion, styles['Normal']))

doc.build(story)

print(f"✅ Report generated successfully: {pdf_file}")
