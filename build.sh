#!/bin/bash

mkdir -p mnt0
mkdir -p mnt2
mkdir -p mnt3
rm hello_ll_2.bin
rm hello_ll_3.bin
gcc -Wall hello_ll_2.c `pkg-config fuse --cflags --libs` -o hello_ll_2.bin
gcc -Wall hello_ll_3.c `pkg-config fuse3 --cflags --libs` -o hello_ll_3.bin
