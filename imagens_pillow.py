from PIL import Image, ImageFilter

imagem = Image.open("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1.png")

# EXIBIR
# imagem.show()

# CONVERTER FORMATO DA IMAGEM

imagem_rgb = imagem.convert("RGB")
imagem_rgb.save("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1.jpg")

#   CONVERTER O TAMANHO
tamanho = (300, 300)
imagem.thumbnail(tamanho)
imagem.save("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1 300.png")

# EDITAR IMAGENS

# ROTACIONAR 
imagem.rotate(90).save("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1 rotacionado.png")

# EDITAR CORES
imagem.convert("L").save("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1 300.png")

# FILTROS
imagem.filter(ImageFilter.GaussianBlur(2)).save("C:\\Users\\caiqu\\Desktop\\AULAS_PYTHON\\PYTHON NTT\\IMAGEM\\imagem1 birrado.png")