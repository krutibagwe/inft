#!/bin/bash
echo "Enter the number: "
read n
echo "Enter the limit: "
read l
echo " "
echo "Table of $n (till limit $l): "
i=1
while [ $i -le $l ]
do
mult=`expr $i \* $n`
echo "$n * $i = $mult"
((++i))
done
