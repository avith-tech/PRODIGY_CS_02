import numpy as np
from PIL import Image

def encrypt(input_image_path, output_image_path):
    #open the imagen using pil
    image = Image.open(input_image_path)
    print(f"image format is:{image.mode}")
    if image.mode == 'L':
        # grayscale image, skip RGB channel swapping and just copy the image
        print("Image is grayscale. Encryption will not modify color channels.")
        encrypted_pixels = np.array(image)
        print(f"image array shape is:{encrypted_pixels.shape}")
    else:
        # Convert image to RGB if it's not already
        if image.mode != 'RGB':
            image = image.convert('RGB')

        pixels = np.array(image)
        print(f" image array shape:{pixels.shape}")

        # Swap pixel values-rgb
        encrypted_pixels = np.copy(pixels)
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                # Swap the red and blue channels for encryption
                encrypted_pixels[i, j, 0], encrypted_pixels[i, j, 2] = pixels[i, j, 2], pixels[i, j, 0]

    #save encrypted values
    encrypted_image=Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt(input_image_path, output_image_path):
    encrypt_image=Image.open(input_image_path)
    print(f"Image format is:{encrypt_image}")
    if encrypt_image.mode == 'L':
        # grayscale image, skip decryption and just copy the image
        print("Image is grayscale. Decryption will not modify color channels.")
        decrypted_pixels = np.array(encrypt_image)
        print(f"image array shape is:{decrypted_pixels}")
    else:
        # Convert image to RGB if it's not already
        if encrypt_image.mode != 'RGB':
            encrypted_image = encrypt_image.convert('RGB')

        encrypted_pixels = np.array(encrypt_image)
        print(f"image array shape is:{encrypted_pixels}")
        # Swap pixel values back to decrypt (for RGB images)
        decrypted_pixels = np.copy(encrypted_pixels)
        for i in range(encrypted_pixels.shape[0]):
            for j in range(encrypted_pixels.shape[1]):
                # Swap back the red and blue channels for decryption
                decrypted_pixels[i, j, 0], decrypted_pixels[i, j, 2] = encrypted_pixels[i, j, 2], encrypted_pixels[
                    i, j, 0]

    #saving decrypted image
    decrypted_image=Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)
    print(f"print the decrypted image is saved as:{output_image_path}")

if __name__== "__main__":
    action=input("Do you want to encrypt or decrypt?(e/d):").lower()
    if action=='e':
        input_path= input("Enter the path of the image to encrypt:")
        output_path=input("Enter the path to save encrypted image:")
        encrypt(input_path,output_path)
    elif action=='d':
        input_path=input("Enter the path of the image to decrypt:")
        output_path=input("Enter the path to store decrypted image:")
        decrypt(input_path,output_path)
    else:
        print("Invalid input value. Please choose 'e' for encrypt and 'd' for decrypt")