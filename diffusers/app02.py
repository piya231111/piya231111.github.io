import diffusers
from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, diffuser_model):
    diffusers = diffusers.load_diffuser(diffuser_model)
    image_data = diffuser.generate(text)
    image = image.fromarray(image_data)
    image.show()

if __name__ == "__main__":
    input_text = "Hello, Wold!"
    diffuser_model = "example_diffuser_model"
    