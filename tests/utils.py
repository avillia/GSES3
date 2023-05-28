import random
import string


def generate_sample_string(length: int = 8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
