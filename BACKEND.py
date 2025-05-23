from flask import Flask, render_template, request, Response
from fpdf import FPDF
from datetime import datetime

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.get_json()
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Header
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "FICHE DE CONTRÔLE HSE", 0, 1, 'C')
        pdf.ln(10)
        
        # Inspection info
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 10, "Date de l'inspection :", 0, 0)
        pdf.cell(0, 10, data['inspection_date'], 0, 1)
        pdf.cell(40, 10, "Lieu / Site :", 0, 0)
        pdf.cell(0, 10, data['site'], 0, 1)
        pdf.cell(40, 10, "Installation :", 0, 0)
        pdf.cell(0, 10, data['installation'], 0, 1)
        pdf.cell(40, 10, "Inspecteur(s) :", 0, 0)
        pdf.cell(0, 10, data['inspectors'], 0, 1)
        pdf.cell(40, 10, "Département concerné :", 0, 0)
        pdf.cell(0, 10, data['department'], 0, 1)
        pdf.ln(10)
        
        # Section 1: General Safety Control
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "1. CONTRÔLE GÉNÉRAL DE LA SÉCURITÉ", 0, 1)
        pdf.set_font("Arial", size=10)
        
        # Table header
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(80, 10, "Éléments à vérifier", 1, 0, 'L', 1)
        pdf.cell(20, 10, "Conforme", 1, 0, 'C', 1)
        pdf.cell(20, 10, "Non conforme", 1, 0, 'C', 1)
        pdf.cell(70, 10, "Observations / Actions correctives", 1, 1, 'C', 1)
        
        # Table rows (sample data - you would add all items)
        pdf.cell(80, 10, "Port des EPI (casque, gants, lunettes, chaussures, etc.)", 1)
        pdf.cell(20, 10, "☐", 1, 0, 'C')
        pdf.cell(20, 10, "☐", 1, 0, 'C')
        pdf.cell(70, 10, "", 1, 1)
        
        # Add all other sections similarly
        
        # General comments
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Commentaires généraux :", 0, 1)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, data['comments'])
        
        # Signatures
        pdf.ln(15)
        pdf.cell(95, 10, "Signature de l'inspecteur : ________________________", 0, 0)
        pdf.cell(0, 10, "Signature du responsable de site : ________________________", 0, 1)
        
        # Generate PDF
        pdf_output = pdf.output(dest='S').encode('latin1')
        
        return Response(
            pdf_output,
            mimetype='application/pdf',
            headers={'Content-Disposition': 'attachment; filename=fiche_controle_HSE.pdf'}
        )
        
    except Exception as e:
        return str(e), 500

if _name_ == '_main_':
    app.run(debug=True)