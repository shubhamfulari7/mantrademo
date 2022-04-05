#!/bin/bash

echo "Enter 3 bash variables - 2 input video files and output video file location"  
read vfile1 vfile2 flocation  
echo "$vfile1, $vfile2, $flocation are the input."  

cat vfile1 vfile2 > flocation
