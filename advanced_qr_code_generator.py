import qrcode as qr
from PIL import Image #if i want to add special opertions(fill color,back color etc) on saved images by qrcode lib 
gen=qr.QRCode(version=1,
                error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=10,border=4)
gen.add_data("https://jsl.savvyhrms.in/savvyhrms/")
gen.make(fit=True)
img=gen.make_image(fill_color='black',back_color='white') #here make_images is taken instead of make bcs in order to get more control of image like fill coolor,back color
img.save("JSL HRMS Login.jpeg")
