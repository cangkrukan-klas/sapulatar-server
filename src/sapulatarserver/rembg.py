import numpy as np
import io
import os
from PIL import Image
from rembg.bg import remove


# TODO prepare rembg interface


def remove_background(filename, filepath):
    """
    Remove background from image with rembg
    @type filename: str
    @type filepath: str
    @param filename: A name of file to process
    @param filepath: A path of the file without filename
    @return: output_filename
    """

    # insert "_result" in the filename for result image
    extension_index = filename.index('.')
    output_filename = filename[:extension_index] + "_result" + ".png"

    # load image
    image = np.fromfile(os.path.join(filepath, filename))

    # remove the background and save it
    image_result = remove(image)
    image_result = Image.open(io.BytesIO(image_result)).convert("RGBA")
    image_result.save(os.path.join(filepath, output_filename))

    return output_filename


# if __name__ == "__main__":
#     print(remove_background("a.jpeg", "/home/fadhilyori"))
