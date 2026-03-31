import string
from pwn import *

charset = string.ascii_letters + string.digits
enc_flag = bytes.fromhex("your hash")
part_flag = b'THM{'

part_key = xor(enc_flag, part_flag)[:4]
#print(part_key)

for c in charset:
    key = part_key + c.encode()
    dec_flag = xor(enc_flag, key).decode()

    if dec_flag[-1] == '}':
         print(f"Key: {key.decode()}")
         print(f"Flag: {dec_flag}")
