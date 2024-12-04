import qrcode

# 创建QRCode对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加数据到二维码
qr.add_data('https://github.com/DU1999')
qr.make(fit=True)

# 创建二维码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图片
img.save("link.png")
