echo "enter a file name"
read filename
if [ -f "$filename" ]; then
	echo "file exists"
else 
	echo "file does not exists"
fi
