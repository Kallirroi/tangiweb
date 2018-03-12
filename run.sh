echo "preparing to take screeshot of $1" 
python screenshot.py $1
echo "preparing to pixelate $1"
python pixelate.py $1
echo "graying and inverting $1"
python invert.py $1
echo "sending $1 to socket"
python ocamyGo.py $1