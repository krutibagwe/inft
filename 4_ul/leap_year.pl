#!/usr/bin/perl
print "Enter a year: ";
$year = <STDIN>;
if ($year % 4 == 0) {
	if ($year % 100 == 0) {
    	if ($year % 400 == 0) {
        	print "$year is a leap year.\n";
    	} else {
        	print "$year is not a leap year.\n";
    	}
	} else {
    	print "$year is a leap year.\n";
	}
} else {
	print "$year is not a leap year.\n";
}
