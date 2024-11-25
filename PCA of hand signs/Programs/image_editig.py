import os
from PIL import Image, ImageOps

#Saves an image with a provided name at a given location
def rename_save_img(img: Image, name: str, path: str) -> None:
    img.save(path + "//" + name + ".jpg")

#Rotates an image with a given angle
#Returns the rotated image
def rotate(img: Image, alpha: int) -> Image:
    img = img.rotate(angle=alpha)
    return img

#Scales down the image to a given width and height, only works on square pictures (Warning shown with LANCZOS method is irrelevant)
#Returns new image
def downscale(img: Image, size: int) -> Image:
    new_size: list = (size, size)
    return img.resize(new_size, Image.LANCZOS)

#Converts image to Grayscale
#Returns new image
def black_white(img: Image) -> Image:
    return img.convert('L')

#Mirrors an image
#Returns mirrored Image
def mirror(img: Image) -> Image:
    return ImageOps.mirror(img)

_debug: bool = True
image_dir: str = "PCA of hand signs//Images//10_T_E_P_Pi_M_Remy"
image_dest: str = "PCA of hand signs//Processed Images//Train"

order_names: list = ["thumbs_up", "easy", "peace", "pistol","metal"]#Abbr. High Five: HF, Metal: M, Peace: P, Crossed: C, Pistol: Pi, Easy: E, Thumbs up: T, Fist: F, Index: I, Okay: O
n_per_cat: int = 10
replace: bool = False # if False checks whether name already exists, if it does it increments the number and adds the new image
size: int = 256 #resulting image in format size x size
file_names: list = sorted(os.listdir(image_dir))

for i in range(len(file_names) // n_per_cat):
    image_num: list = [(i * n_per_cat), (i * n_per_cat) + n_per_cat] #Images [0,5)
    images: list = file_names[image_num[0]:image_num[1]]
    image_name: str = order_names[i]
    for j, name in enumerate(images):
        img_name: str = image_name + "_" + f"{j:02}"
        img: Image = Image.open(image_dir + "//" + name)
        img = rotate(img, 180)
        img = downscale(img, size)
        img = black_white(img)
        if not replace:
            n: int = j
            while True:
                if os.path.isfile(image_dest + "//" + img_name + ".jpg"):
                    n += 1
                    img_name = image_name + "_" + f"{n:02}"
                else: break
        if _debug:
            print(str((i * n_per_cat) + j + 1) + "/" + str(len(file_names)) +" Saved Image as: " + img_name)
        img = rename_save_img(img, img_name , image_dest)

