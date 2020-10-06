from PIL import Image
file = Image.open("*file location*").convert("RGB")
file.save("file name.jpg","jpeg")
