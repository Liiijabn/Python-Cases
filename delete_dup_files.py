#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import shutil


deleted_files = []


def delete_dup_files(root_directory):
    # names = [x for x in os.listdir(root_directory)]
    for name in os.listdir(root_directory):
        file = os.path.join(root_directory, name)
        if os.path.isdir(file):
            delete_dup_files(file)
        if os.path.isfile(file):
            delete_file(name, file)


def delete_file(name, file):
    if re.match(r'^[0-9a-zA-Z\_\-]+\s\(\d+\).[a-zA-Z]+$', name):
        deleted_files.append(file)
        move_to_trash(name, file)


def move_to_trash(name, file):
    trash = '/Users/neo/.Trash';
    destination = os.path.join(trash, name)
    if os.path.isfile(destination):
        os.remove(file)
    else:
        shutil.move(file, trash)


# delete_dup_files('/Users/neo/Pictures/iPhone/000000')
for deleted in deleted_files:
    print('deleted_files: ' + deleted)
