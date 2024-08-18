import qrcode
from PIL import Image


def create_qr_code(data, logo_path, qr_name="qrcode.png", logo_size=(50, 50)):

    # Créer le QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Ouvrir l'image du logo
    logo = Image.open(logo_path)
    logo.thumbnail(logo_size)

    # Calculer les dimensions pour ajuster le logo
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)

    # Enregistrer le QR code final
    img.save(qr_name)


# Exemple d'utilisation
data = "NAME=ASASAGARE SANA;\nDLNo=PNC0125420;\ncat=A,B;\nDOB=07-01-2000 12:00:00 AM;"
logo_path = "/home/me/Pictures/astro.png"  # Remplacez par le chemin de votre logo

create_qr_code(data, logo_path)
