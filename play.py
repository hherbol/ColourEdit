from PIL import Image
import ColourEdit as CE


img = Image.open('google_image.png')
img.show()

img = CE.rg_color_blind(img, "Red", "Green", delta=50)
img.show()
