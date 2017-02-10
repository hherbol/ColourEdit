from PIL import Image
from PIL import ImageFilter

COLORS = {"Snow": [255, 250, 250],
          "Snow2": [238, 233, 233],
          "Snow3": [205, 201, 201],
          "Snow4": [139, 137, 137],
          "GhostWhite": [248, 248, 255],
          "WhiteSmoke": [245, 245, 245],
          "Gainsboro": [220, 220, 220],
          "FloralWhite": [255, 250, 240],
          "OldLace": [253, 245, 230],
          "Linen": [240, 240, 230],
          "AntiqueWhite": [250, 235, 215],
          "AntiqueWhite2": [238, 223, 204],
          "AntiqueWhite3": [205, 192, 176],
          "AntiqueWhite4": [139, 131, 120],
          "PapayaWhip": [255, 239, 213],
          "BlanchedAlmond": [255, 235, 205],
          "Bisque": [255, 228, 196],
          "Bisque2": [238, 213, 183],
          "Bisque3": [205, 183, 158],
          "Bisque4": [139, 125, 107],
          "PeachPuff": [255, 218, 185],
          "PeachPuff2": [238, 203, 173],
          "PeachPuff3": [205, 175, 149],
          "PeachPuff4": [139, 119, 101],
          "NavajoWhite": [255, 222, 173],
          "Moccasin": [255, 228, 181],
          "Cornsilk": [255, 248, 220],
          "Cornsilk2": [238, 232, 205],
          "Cornsilk3": [205, 200, 177],
          "Cornsilk4": [139, 136, 120],
          "Ivory": [255, 255, 240],
          "Ivory2": [238, 238, 224],
          "Ivory3": [205, 205, 193],
          "Ivory4": [139, 139, 131],
          "LemonChiffon": [255, 250, 205],
          "Seashell": [255, 245, 238],
          "Seashell2": [238, 229, 222],
          "Seashell3": [205, 197, 191],
          "Seashell4": [139, 134, 130],
          "Honeydew": [240, 255, 240],
          "Honeydew2": [244, 238, 224],
          "Honeydew3": [193, 205, 193],
          "Honeydew4": [131, 139, 131],
          "MintCream": [245, 255, 250],
          "Azure": [240, 255, 255],
          "AliceBlue": [240, 248, 255],
          "Lavender": [230, 230, 250],
          "LavenderBlush": [255, 240, 245],
          "MistyRose": [255, 228, 225],
          "White": [255, 255, 255],
          "Black": [0, 0, 0],
          "DarkSlateGray": [49, 79, 79],
          "DimGray": [105, 105, 105],
          "SlateGray": [112, 138, 144],
          "LightSlateGray": [119, 136, 153],
          "Gray": [190, 190, 190],
          "LightGray": [211, 211, 211],
          "MidnightBlue": [25, 25, 112],
          "Navy": [0, 0, 128],
          "CornflowerBlue": [100, 149, 237],
          "DarkSlateBlue": [72, 61, 139],
          "SlateBlue": [106, 90, 205],
          "MediumSlateBlue": [123, 104, 238],
          "LightSlateBlue": [132, 112, 255],
          "MediumBlue": [0, 0, 205],
          "RoyalBlue": [65, 105, 225],
          "Blue": [0, 0, 255],
          "DodgerBlue": [30, 144, 255],
          "DeepSkyBlue": [0, 191, 255],
          "SkyBlue": [135, 206, 250],
          "LightSkyBlue": [135, 206, 250],
          "SteelBlue": [70, 130, 180],
          "LightSteelBlue": [176, 196, 222],
          "LightBlue": [173, 216, 230],
          "PowderBlue": [176, 224, 230],
          "PaleTurquoise": [175, 238, 238],
          "DarkTurquoise": [0, 206, 209],
          "MediumTurquoise": [72, 209, 204],
          "Turquoise": [64, 224, 208],
          "Cyan": [0, 255, 255],
          "LightCyan": [224, 255, 255],
          "CadetBlue": [95, 158, 160],
          "MediumAquamarine": [102, 205, 170],
          "Aquamarine": [127, 255, 212],
          "DarkGreen": [0, 100, 0],
          "DarkOliveGreen": [85, 107, 47],
          "DarkSeaGreen": [143, 188, 143],
          "SeaGreen": [46, 139, 87],
          "MediumSeaGreen": [60, 179, 113],
          "LightSeaGreen": [32, 178, 170],
          "PaleGreen": [152, 251, 152],
          "SpringGreen": [0, 255, 127],
          "LawnGreen": [124, 252, 0],
          "Chartreuse": [127, 255, 0],
          "MediumSpringGreen": [0, 250, 154],
          "GreenYellow": [173, 255, 47],
          "LimeGreen": [50, 205, 50],
          "YellowGreen": [154, 205, 50],
          "ForestGreen": [34, 139, 34],
          "OliveDrab": [107, 142, 35],
          "DarkKhaki": [189, 183, 107],
          "Khaki": [240, 230, 140],
          "PaleGoldenrod": [238, 232, 170],
          "LightGoldenrodYellow": [250, 250, 210],
          "LightYellow": [255, 255, 224],
          "Yellow": [255, 255, 0],
          "Gold": [255, 215, 0],
          "LightGoldenrod": [238, 221, 130],
          "Goldenrod": [218, 165, 32],
          "DarkGoldenrod": [184, 134, 11],
          "RosyBrown": [188, 143, 143],
          "IndianRed": [205, 92, 92],
          "SaddleBrown": [139, 69, 19],
          "Sienna": [160, 82, 45],
          "Peru": [205, 133, 63],
          "Burlywood": [222, 184, 135],
          "Beige": [245, 245, 220],
          "Wheat": [245, 222, 179],
          "SandyBrown": [244, 164, 96],
          "Tan": [210, 180, 140],
          "Chocolate": [210, 105, 30],
          "Firebrick": [178, 34, 34],
          "Brown": [165, 42, 42],
          "DarkSalmon": [233, 150, 122],
          "Salmon": [250, 128, 114],
          "LightSalmon": [255, 160, 122],
          "Orange": [255, 165, 0],
          "DarkOrange": [255, 140, 0],
          "Coral": [255, 127, 80],
          "LightCoral": [240, 128, 128],
          "Tomato": [255, 99, 71],
          "OrangeRed": [255, 69, 0],
          "Red": [255, 0, 0],
          "HotPink": [255, 105, 180],
          "DeepPink": [255, 20, 147],
          "Pink": [255, 192, 203],
          "LightPink": [255, 182, 193],
          "PaleVioletRed": [219, 112, 147],
          "Maroon": [176, 48, 96],
          "MediumVioletRed": [199, 21, 133],
          "VioletRed": [208, 32, 144],
          "Violet": [238, 130, 238],
          "Plum": [221, 160, 221],
          "Orchid": [218, 112, 214],
          "MediumOrchid": [186, 85, 211],
          "DarkOrchid": [153, 50, 204],
          "DarkViolet": [148, 0, 211],
          "BlueViolet": [138, 43, 226],
          "Purple": [160, 32, 240],
          "MediumPurple": [147, 112, 219],
          "Thistle": [216, 191, 216]}


# Completely different color
def diff_color(image):
    width, height = img.size

    # Process every pixel
    for x in range(width):
        for y in range(height):
            new_color = (0, 100, 100)
            image.putpixel((x, y), new_color)
    return image


def get_pixel_luminance(rgb):
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]


def get_image_luminance(image):
    '''
    Loop through image and calculate a total luminance value for it.
    Luminance is calculated as the total pixel luminance divided by the number
    of pixels.

    Pixel Luminance = 0.299 * R + 0.587 * G + 0.114 * B

    **References**

        * http://stackoverflow.com/a/596243
    '''
    width, height = img.size

    reds = sum([c[0]
                for x in range(width)
                for y in range(height)
                for c in img.getpixel((x, y))
                ]
               )
    greens = sum([c[0]
                  for x in range(width)
                  for y in range(height)
                  for c in img.getpixel((x, y))
                  ]
                 )
    blues = sum([c[0]
                 for x in range(width)
                 for y in range(height)
                 for c in img.getpixel((x, y))
                 ]
                )
    total_luminance = 0.299 * reds + 0.587 * greens + 0.114 * blues

    return total_luminance / (width * height)


# Remove color
def remove_color(image, operator, color="RED", scale=0.2, keep_brightness=True):

    if color not in COLORS:
        raise Exception("You chose a bad color >:(")
    if operator not in ["ADD", "SUBTRACT"]:
        raise Exception("Opterator must be ADD or SUBTRACT")

    width, height = img.size

    edit_colour = [int(c * scale) for c in COLORS[color]]

    # Process every pixel
    for x in range(width):
        for y in range(height):
            current_color = img.getpixel((x, y))
            luminance = 0.299 * current_color[0] +\
                0.587 * current_color[1] +\
                0.114 * current_color[2]

            new_colour = [a - b for a, b in zip(current_color, edit_colour)]
            new_color = tuple([max(val, 0.1) for val in new_colour])
            luminance2 = 0.299 * new_color[0] +\
                 0.587 * new_color[1] +\
                 0.114 * new_color[2]
            if keep_brightness:
                new_color = tuple([int(c * luminance / luminance2) for c in new_color])

            new_color = tuple([int(c) for c in new_color])
            image.putpixel((x, y), new_color)
    return image


# Add color
def add_color(image, color="RED", scale=0.2):

    if color not in COLORS:
        raise Exception("You chose a bad color >:(")

    width, height = img.size

    edit_colour = [int(c * scale) for c in COLORS[color]]

    # Process every pixel
    for x in range(width):
        for y in range(height):
            current_color = img.getpixel((x, y))
            new_colour = [a + b for a, b in zip(current_color, edit_colour)]
            new_color = tuple([min(val, 255) for val in new_colour])
            image.putpixel((x, y), new_color)
    return image


# Get color of specified pixel
def get_pixel(image, x, y):
    pix = image.load()
    print pix[x, y]
    return pix[x, y]


# Resize image
def resize(image, size1, size2):
    new_img = image.resize((size1, size2))
    return new_img


# Convert to grayscale (using 'grayscale' function on Wikipedia)
def rgb2gray(image):
    width, height = img.size

    # Process every pixel
    for x in range(width):
        for y in range(height):
            current_color = img.getpixel((x, y))
            scaling_function = (0.299, 0.587, 0.114)
            new_color = tuple([int(a * b) for a, b in zip(current_color, scaling_function)])
            image.putpixel((x, y), new_color)
    return image


def blur(image):
    blurred_image = image.filter(ImageFilter.BLUR)

    return blurred_image


def blur_alg(image):

    # You need a graphic file in the working directory, specify it here:
    width, height = image.size

    # The higher the kernel value, the more intense the blur
    blur_amount = 6
    blur_range = blur_amount / 2

    # The blur algorithm
    # ------------------
    # The algorithm works like this:
    # For every pixel in 'img', add the red, green and blue values of it's
    # neighbouring pixels and divide each total red, green and blue value by
    # the total number of colours scanned. This then gives you the average pixel
    # colour for the pixel in 'img' being scanned. The neighbouring pixels positions
    # are calculated using a kernel value.

    # The 20 x 3 dots below represented pixels, and the X represents the
    # pixel currently being checked.
    # ...................
    # .............x.....
    # ...................

    # If the kernel size has been set to three then the pixel colour checks
    # would be done
    # like this ('c' represents a colour check):
    # ............ccc....
    # ............cxc....
    # ............ccc....

    for x in range(0, int(height)):
        for y in range(0, int(width)):
            r, g, b, colour, count = 0, 0, 0, (0, 0, 0), 0

            for blur_x in range(0 - blur_range, 0 + blur_range):
                for blur_y in range(0 - blur_range, 0 + blur_range):
                    # Don't check outside screen edges...
                    if (x + blur_x > 0 and x + blur_x < height and y + blur_y > 0 and y + blur_y < width):
                        colour = image.getpixel((y + blur_y, x + blur_x,))
                        r += colour[0]
                        g += colour[1]
                        b += colour[2]
                        count += 1

            if (r > 0):
                r = r / count
            if (g > 0):
                g = g / count
            if (b > 0):
                b = b / count

            blur = (r, g, b)
            image.putpixel((y, x), blur)

    return image

############################
# Start actual Python Script
############################
img = Image.open('spring.jpg')

img.show()

img = remove_color(img, "Purple", scale=1)

img.show()

img = remove_color(img, "Purple", scale=1, keep_brightness=False)

# Displaying
img.show()
