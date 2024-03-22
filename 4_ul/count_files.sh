#! /bin/bash
ls
echo "Enter directory name: "
read dir
if [ -d $dir ]
then
    echo "Number of files are: $(find $dir -type f | wc -l)"
    echo "Number of sub directories are: $(find $dir -type d | wc -l)"
else
    echo "Error"
    exit 1
fi
