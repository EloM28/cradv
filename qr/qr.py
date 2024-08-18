import qrcode
import qrcode.image.svg

# Le texte que vous souhaitez encoder dans le QR code
data = (
    "NAME=ASASAGARE SANA;\n"
    + "DLNo=PNC0125420;\n"
    + "cat=A,B;\n"
    + "DOB=07-01-2000 12:00:00 AM;"
)

# Créer un objet QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
factory = qrcode.image.svg.SvgImage
img = qrcode.make("Mon super QR code", image_factory=factory)
qr.add_data(data)
# qr.make(fit=True)

# Créer une image à partir du QR code
img = qr.make_image(fill_color="black", back_color="white")

# Enregistrer l'image
img.save("qrcode.png")

