#!/usr/bin/perl
print "Enter the number: ";
$num = <STDIN>;
$is_prime = 1;

for ($i = 2; $i <= sqrt($num); $i++) {
	if ($num % $i == 0) {
    	$is_prime = 0;
	}
}
if ($is_prime) {
  print "$num is prime\n";
} else {
  print "$num is not prime\n";
}
