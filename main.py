import cv2

image= cv2.imread("galaxy.jpeg")
print(image.shape)

def calculate_size (sclae_percentage, width, height):
    new_width= int(width * sclae_percentage / 100)
    new_height= int(height * sclae_percentage/ 100)
    return (new_width, new_height)

def resize(image_path, scale_percentage, resized_path):
    image= cv2.imread(image_path)
    new_dim= calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image= cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)

resize("galaxy.jpeg",50, "resized_galaxy.jpeg")