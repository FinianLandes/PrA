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
image_dir: str = "PCA of hand signs//Images//5_HF_M_P"
image_dest: str = "PCA of hand signs//Processed Images"

order_names: list = ["high_five", "metal", "peace"]#Abbr. High Five: HF, Metal: M, Peace: P
n_per_cat: int = 5
replace: bool = True # if False checks whether name already exists, if it does it increments the number and adds the new image
resolution: int = 256 #resulting image in format resolution x resolution
file_names: list = sorted(os.listdir(image_dir))

for i in range(len(file_names) // n_per_cat):
    image_num: list = [(i * 5), (i * 5) + 5] #Images [0,5)
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
            print("Saved Image as: " + img_name)
        img = rename_save_img(img, img_name , image_dest)


