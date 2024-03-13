#!/bin/bash
echo "enter 1st number: "
read n1
echo "enter 2nd number: "
read n2
echo "Addition is: `expr $((n1+n2))`"
echo "Subtraction is: `expr $((n1-n2))`"
echo "Multiplication is: `expr $((n1*n2))`"
echo "Division is: `expr $((n1/n2))`"
