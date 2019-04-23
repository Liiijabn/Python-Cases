#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class FileEncrypt:

    __key = 0xa

    def encrypt(self, in_file, out_file):
        with open(in_file, 'rb') as f:
            byte_array = bytearray(f.read())
        with open(out_file, 'wb') as out:
            for i, j in enumerate(byte_array):
                byte_array[i] = j ^ self.__key

            out.write(bytes(byte_array))

    def decrypt(self, in_file, out_file):
        self.encrypt(in_file, out_file)

    # def set_encrypt_key(self, key: int):
    #     self.__key = key
    #
    # def get_encrypt_key(self):
    #     return self.__key


file = '/Users/neo/Pictures/网络图片/最孤独的人.jpg'
e_file = '/Users/neo/Pictures/网络图片/最孤独的人_en.jpg'
de_file = '/Users/neo/Pictures/网络图片/最孤独的人_de.jpg'

enc = FileEncrypt()
# enc.set_encrypt_key(25)
enc.encrypt(file, e_file)
enc.decrypt(e_file, de_file)
# print(enc.get_encrypt_key())

