#! /bin/bash
echo "Enter source file: "
read src
echo "Enter target file: "
read targ
if [ ! -f $src ]
then
echo "File $src does not exist"
exit 1
elif [ -f $targ ]
then 
echo "File $targ already exists, cannot overwrite"
exit 2
fi
cp $src $targ
status=$?
if [ $status -eq 0 ]
then
echo "File copied successfully"
else
echo "Problem with copying"
fi
