import barcode
from barcode.writer import ImageWriter

# Données à encoder
data = "1234567890123"

# Créer un objet code-barres EAN-13
# et on peut le si on veut le changer code-barres de type  code128 ou UPC-A
ean = barcode.EAN13(data, writer=ImageWriter())

# Personnalisation
ean.options.module_height = 20  # Hauteur des modules
ean.options.font_size = 10  # Taille de la police pour le texte
ean.options.text_distance = 5  # Distance entre le code-barres et le texte

# Enregistrer l'image du code-barres
ean.save("my_ean13_barcode")
