from reportlab.pdfgen import canvas

def hello(c):
    c.drawString(100, 100, "hello world")

c = canvas.Canvas("hello.pdf")
hello(c)

c.showPage()
c.save()