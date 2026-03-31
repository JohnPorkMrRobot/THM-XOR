import string
from pwn import *

charset = string.ascii_letters + string.digits
enc_flag = bytes.fromhex("393e351a1e5c17140f1a280e0c201a19421b0a0d2c180a520f013a01093b1f0201511b1f0e371313")
part_flag = b'THM{'

part_key = xor(enc_flag, part_flag)[:4]
#print(part_key)

for c in charset:
    key = part_key + c.encode()
    dec_flag = xor(enc_flag, key).decode()

    if dec_flag[-1] == '}':
         print(f"Key: {key.decode()}")
         print(f"Flag: {dec_flag}")