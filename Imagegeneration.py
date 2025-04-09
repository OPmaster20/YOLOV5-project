import qrcode,os

data = "Test 100"
imgsname = "top.jpg"
print(os.getcwd())

if os.path.isfile(str(os.getcwd()) + imgsname):
    os.remove(str(os.getcwd()) + imgsname)
imgs = qrcode.make(data)
print(type(imgs))
imgs.save(imgsname)
