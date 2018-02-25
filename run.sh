# echo "cleaning up temp folder"
# rm temp/*
echo "preparing to take screeshot"
python screenshot.py
echo "preparing to pixelate"
python pixelate.py
echo "moving image to out/ folder"
mv in/screenshot_pixelated.png out/
# echo "graying final output"
# python gray.py
echo "graying and inverting"
python invert.py
echo "done"