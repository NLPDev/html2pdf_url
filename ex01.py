import pdfkit

pdfkit.from_file("canvas.html", "out.pdf")
pdfkit.from_url("https://demo.waiver.dizio.app/kapowsin/pages/page1.html", "out.pdf")