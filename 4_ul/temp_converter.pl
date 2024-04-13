#!/usr/bin/perl
print "Enter temperature in Centigrade: ";
$cent = <STDIN>;
$fah = (9 * $cent/5) +32;
print "corresponding temperature in Fahrenheit is $fah degree Fahrenheit\n";
