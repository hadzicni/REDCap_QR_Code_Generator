import qrcode
from PIL import Image
import json

data = {
    'pat_id': '1111111',
    'fname' : 'Nikola',
    'lname' : 'Hadzic',
    'dateob' : '01-08-2007',
}

data_string = json.dumps(data)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=60,
    border=4,
)

qr.add_data(data_string)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

logo = Image.open('logo.png') 

logo_size = min(img.size) // 3

logo = logo.resize((logo_size, logo_size))

pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

img.save('qrcode/redcap_qrcode.pdf')
