echo "enter a file or directory"
read name
if [ -f "$name" ]; then 
	echo "It's a file"
elif [ -d "$name" ]; then
	echo "It's a directory"
else
	echo "does not exists"
fi
