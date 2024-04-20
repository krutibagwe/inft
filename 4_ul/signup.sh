#!/bin/bash

# Prompt user to enter username and password
read -p "Enter username: " username
read -sp "Enter password: " password
echo

# Check if the file exists and is writable
if [ ! -w "users.txt" ]; then
	echo "Error: Unable to write to users.txt"
	exit 1
fi

# Save username and password (plaintext for demonstration)
echo "$username:$password" >> users.txt

# Provide feedback to the user
if [ $? -eq 0 ]; then
	echo "User '$username' signed up successfully!"
else
	echo "Error: Unable to sign up user '$username'"
fi
