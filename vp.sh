#!/bin/bash
for file in `ls vpype/input/*.svg | sort`; do
    echo $file
    vpype read $file name -l 1 "%lid%"
done
vpype write vpype/output/output.svg