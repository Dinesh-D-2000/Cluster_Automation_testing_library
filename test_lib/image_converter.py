

def insert_image(name, image_path):
    with open(image_path, "rb") as image:
        blob_data = image.read()
        print(blob_data.hex())

   

#insert_image("icn_abs_image", r"D:\Automation_testing\abs_yellow.png" )
insert_image("icn_tpms_image", r"D:\Automation_testing\icons\icn_tpms.png")



    
    

