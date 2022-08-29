import mylib

CURRENT_PATH = "cotton"
DESTINATION_PATH = "cotton_224x224"
IMAGE_SIZE = (224, 224)


# mylib.copy_folders(CURRENT_PATH, DESTINATION_PATH)
#mylib.resize_images(CURRENT_PATH, DESTINATION_PATH, IMAGE_SIZE)
mylib.split_to("cotton_224x224", "cotton_224x224_split", 0.8, 0.1, 0.1)
#mylib.split_to(CURRENT_PATH,
               #DESTINATION_PATH, 0.15, 0.8, 0.05)


# mylib.get_folders(CURRENT_PATH)
