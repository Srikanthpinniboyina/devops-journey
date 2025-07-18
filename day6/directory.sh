#!/bin/bash
read -p "enter folder name" folder
mkdir -p "$folder"
for i in {1..3}
do 
	echo "This is file$i" > "$folder/file$i.txt"
done
echo "Folder '$folder' with 3 files created."
