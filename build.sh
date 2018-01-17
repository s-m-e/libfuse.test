#!/bin/bash

mkdir -p mnt

rm hello_ll_2.bin
rm hello_ll_3.bin
rm hello_hl_2.bin
rm hello_hl_3.bin

gcc -Wall hello_ll_2.c `pkg-config fuse --cflags --libs` -o hello_ll_2.bin
gcc -Wall hello_ll_3.c `pkg-config fuse3 --cflags --libs` -o hello_ll_3.bin
gcc -Wall hello_hl_2.c `pkg-config fuse --cflags --libs` -o hello_hl_2.bin
gcc -Wall hello_hl_3.c `pkg-config fuse3 --cflags --libs` -o hello_hl_3.bin
