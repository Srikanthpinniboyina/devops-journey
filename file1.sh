echo "enter a number"
read num
count=1
while [ $count -le $num ]; do 
	echo "$count"
	count=$((count + 1))
done	
