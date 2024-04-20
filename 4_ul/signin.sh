#!/bin/bash

# Prompt user to enter username and password
read -p "Enter username: " username
read -sp "Enter password: " password
echo

# Validate credentials against the stored data
if grep -q "^$username:$password$" users.txt; then
	echo "Welcome, $username! Sign-in successful."
else
	echo "Invalid username or password. Please try again."
fi
