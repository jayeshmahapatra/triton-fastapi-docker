import base64
import cv2
import numpy as np


def decode_img(img: str) -> np.ndarray:
    """
    Decode a base64 encoded image and return it as a NumPy array.

    Args:
        img (str): Base64 encoded image.

    Returns:
        np.ndarray: Decoded image as a NumPy array.
    """
    decoded_img = base64.urlsafe_b64decode(img)
    np_arr = np.fromstring(decoded_img, dtype=np.uint8)
    img_decoded = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
    is_encoded = img_decoded is not None
    return img_decoded if is_encoded else np_arr


def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize an image using per-channel normalization (in-place).

    Args:
        image (np.ndarray): Input image as a NumPy array with shape (1, 3, height, width).

    Returns:
        np.ndarray: Normalized image as a NumPy array.
    """

    means = np.mean(image, axis=(2, 3), keepdims=True)
    stds = np.std(image, axis=(2, 3), keepdims=True)

    epsilon = 1e-8  # Small epsilon value for safety

    # Normalize each channel in-place, avoiding division by zero
    image[:, :, :, :] = (image[:, :, :, :] - means) / (stds + epsilon)
    
    return image



def decode_img_to_numpy(base64_img: str, height: int, width: int):

    img = decode_img(base64_img)

    #Change dtype to float32
    img = img.astype(np.float32)

    #Model expects channels first. Changing image to be in format [N,C,H,W]
    img = img.reshape(1, 3, height, width)

    #Normalizing. The per channel mean and std are derived from train set
    # in actual production setting, should be derived from the test set dynamically
    img = normalize_image(img)

    return img