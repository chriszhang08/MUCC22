import cmath
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def decrypt_aes_ecb(ciphertext, key_bytes):
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data.decode('utf-8')


def find_exponent(g, p, A):
    current_value = 1

    for a in range(1, p):
        current_value = (current_value * g) % p
        if current_value == A:
            return a

    return None  # If no exponent is found

if __name__ == '__main__':
    # Example usage:
    base_g = 627
    modulus_p = 941
    result_A = 760

    # exponent_a = find_exponent(base_g, modulus_p, result_A)
    #
    # if exponent_a is not None:
    #     print(f"The exponent a is: {exponent_a}")
    # else:
    #     print("No exponent found.")

    # Example usage:
    ciphertext = "ba1a3f56cff5c56b0e355f944c0f3fe7a1a8878fac48b6163cd4f94b1401ea9342ddb7a928b90ada25ebf8751ed00eb769774f4c16a718427967729323901ca7"
    ciphertext = bytes.fromhex(ciphertext)
    key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x67'

    decrypted_text = decrypt_aes_ecb(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
