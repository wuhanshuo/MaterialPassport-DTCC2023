import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage

def generate_qr_code(project_id, item_id):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=50,
        border=4,
        image_factory=PyPNGImage
    )
    project_id = str(project_id)
    item_id = str(item_id)
    qr.add_data("https://dtcc2023.pythonanywhere.com/?db=" + project_id + "&id=" + item_id)

    print('https://dtcc2023.pythonanywhere.com/?db=' + project_id + '&id=' + item_id)
    qr.make(fit=True)

    img = qr.make_image().to_string(encoding='unicode')
    img = img.replace("fill=\"#000000\"", "fill=\"#0000ff\"")
    f = open("qrcodes/" + str(item_id) + ".svg", "w")
    f.write(img)
    f.close()
    print(type(img))


for i in range(1012, 1015):
    generate_qr_code(project_id=2, item_id=i)
