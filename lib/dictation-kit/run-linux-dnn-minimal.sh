#! /bin/sh
./bin/linux/julius -C main.jconf -C am-dnn.jconf -quiet -nolog -nolattice -noconfnet -1pass -charconv utf-8 utf-8 -dnnconf julius.dnnconf $*