# a shell script to display greatest among three numbers.

#!/bin/bash
find_greatest() {
if [ $1 -gt $2 ] && [ $1 -gt $3 ]; then
echo "Greatest number is: $1"
elif [ $2 -gt $1 ] && [ $2 -gt $3 ]; then
echo "Greatest number is: $2"
else
echo "Greatest number is: $3"
fi
}
echo "Enter three numbers: "
read num1 num2 num3
find_greatest $num1 $num2 $num3
