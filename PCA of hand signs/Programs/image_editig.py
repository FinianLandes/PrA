import os
from PIL import Image, ImageFilter

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
image_dir: str = "PCA of hand signs\Images"
image_dest: str = "PCA of hand signs\Processed Images"

order_names: list = ["high_five", "metal", "peace"]
n_per_cat: int = 5
resolution: int = 256 #resulting image in format resolution x resolution
file_names: list = sorted(os.listdir(image_dir))

for i in range(len(file_names) // n_per_cat):
    image_num: list = [(i * 5), (i * 5) + 5] #Images [0,5)
    images: list = file_names[image_num[0]:image_num[1]]
    image_name: str = order_names[i]
    for i,name in enumerate(images):
        img_name: str = image_name + "_" + f"{i:02}"
        if _debug:
            print("Processing Image: " + img_name)
        img: Image = Image.open(image_dir + "//" + name)
        img = rotate(img, 180)
        img = downscale(img, resolution)
        img = black_white(img)
        img = rename_save_img(img, img_name , image_dest)


