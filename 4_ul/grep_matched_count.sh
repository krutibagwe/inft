echo "Number of matched characters in file: "
grep -o S file_name.txt |wc -l
echo "Number of matched words in file: "
grep -o "word" file_name.txt |wc -l
echo "Number of matched lines in file: "
grep -o "line" file_name.txt |wc -l
