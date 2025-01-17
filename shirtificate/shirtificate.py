from fpdf import FPDF

name=input("Name: ")


pdf = FPDF()
pdf.add_page()
pdf.set_y(10)
pdf.set_font("Arial", style='B', size=37.5)
pdf.cell(pdf.w - 2 * pdf.l_margin, 10, f'CS50 Shirtificate', align='C', ln=True)
pdf.set_y(70)

image_path = "shirtificate.png"
image_width = 200  # Largeur de l'image souhaitée en mm
image_height = 200  # Hauteur de l'image souhaitée en mm
x_position = (pdf.w - image_width) / 2  # Calcul pour centrer horizontalement

pdf.image(image_path, x=x_position, y=50, w=image_width, h=image_height)
pdf.set_text_color(255, 255, 255)
pdf.cell(pdf.w - 2 * pdf.l_margin, 100, f'{name} took CS50', align='C')

pdf.output("shirtificate.pdf")
