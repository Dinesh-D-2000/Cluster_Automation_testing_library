import os


def insert_image(name, image_path):
    with open(image_path, "rb") as image:
        blob_data = image.read()
        print(blob_data.hex())


curr_dir = os.path.dirname(os.path.abspath(__file__))

insert_image("icn_tpms_image", curr_dir + r"\icons\icn_tpms.png")






