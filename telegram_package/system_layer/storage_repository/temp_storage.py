import tempfile
from PIL import Image
import requests
from io import BytesIO

def store_file_to_temp_folder(image_url, file_ext=".png"):
    """
    Downloads an image from the given URL and stores it in a temporary folder.
    Returns the path to the saved image file.

    :param image_url: URL of the image to download.
    :param file_ext: File extension for the saved image.
    :return: Path to the temporary image file.
    """
    # Download the image from the URL
    response = requests.get(image_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Open the downloaded image as a PIL Image
    image = Image.open(BytesIO(response.content))

    # Save the image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext, mode="w+b") as temp_file:
        image.save(temp_file, format=image.format)
        temp_file.flush()
        temp_file.close()

    return temp_file.name