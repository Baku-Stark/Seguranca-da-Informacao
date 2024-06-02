from exif import Image

img_path = 'alvo.jpg'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

if img.has_exif:
    # Inserir um metadado na imagem
    img.copyright = 'Wallace Stay here'

    # Apagar Metadados
    img.delete('flash')

    # lista de metadados
    img_exif_list = img.list_all()
    #print(img_exif_list)

    for exif in img_exif_list:
        print(f"[-] {exif.title()} : {img[exif]}")

    # print(img['copyright'])

    with open("./sem_meta.jpg", "wb") as n_image:
        n_image.write(img.get_file())
        print("Nova Imagem sem metadados geradas")

print("=" *50)
