import qrcode


# Funktion zum Erstellen eines QR-Codes mit strukturierten Daten
def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qr_code.png")


# Funktion zum Lesen des QR-Codes und Extrahieren der Daten
def read_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    return data


# Beispielstrukturierte Daten im JSON-Format
data = '{"PID": "3644875", "FallID": "789124549", "Name": "TEXT", "Surname": "Test}'

# Erstelle einen QR-Code mit den strukturierten Daten
create_qr_code(data)

# Lese den erstellten QR-Code und extrahiere die Daten
extracted_data = read_qr_code("qr_code.png")

# Drucke die extrahierten Daten
print(extracted_data)
