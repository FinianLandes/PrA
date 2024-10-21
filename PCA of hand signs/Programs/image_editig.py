import os
from PIL import Image

def rename_save_img(img: Image, name: str, path: str) -> None:
    img.save(path + "//" + name + ".jpg")
def rotate(img: Image, alpha: int) -> Image:
    img = img.rotate(angle=alpha)
    return img
def downscale(img: Image, resolution: int) -> Image:
    new_size: list = (resolution, resolution)
    return img.resize(new_size, Image.LANCZOS)
def black_white(img) -> Image:
    return img.convert('L')

_debug: bool = True
image_dir: str = "PCA of hand signs//Images//3_O_P_C_Pi_HF_E_M_T_F_I"
image_dest: str = "PCA of hand signs//Processed Images//Test"

order_names: list = ["okay", "peace", "crossed", "pistol", "high_five", "easy", "metal", "thumbs_up", "fist", "index"]#Abbr. High Five: HF, Metal: M, Peace: P, Crossed: C, Pistol: Pi, Easy: E, Thumbs up: T, Fist: F, Index: I, Okay: O
n_per_cat: int = 3
replace: bool = True # if False checks whether name already exists, if it does it increments the number and adds the new image
resolution: int = 256 #resulting image in format resolution x resolution
file_names: list = sorted(os.listdir(image_dir))

for i in range(len(file_names) // n_per_cat):
    image_num: list = [(i * n_per_cat), (i * n_per_cat) + n_per_cat] #Images [0,5)
    images: list = file_names[image_num[0]:image_num[1]]
    image_name: str = order_names[i]
    for j, name in enumerate(images):
        img_name: str = image_name + "_" + f"{j:02}"
        img: Image = Image.open(image_dir + "//" + name)
        img = rotate(img, 180)
        img = downscale(img, resolution)
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
#hi:) 

