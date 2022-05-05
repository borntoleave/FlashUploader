cp ../languages.py .
cp ../SerialCommunication.py .
cp ../Flash_Uploader.py .
cp ../defaultpath.txt .
cp -r ../release .
#
python3 setup.py py2app -A
#
./dist/FlashUploader.app/Contents/MacOS/FlashUploader
rm -rf build
rm -rf dist

python3 setup.py py2app
cp avrdude ./dist/FlashUploader.app/Contents/Resources/

rm -f languages.py
rm -f SerialCommunication.py
rm -f Flash_Uploader.py
rm -f defaultpath.txt
rm -rf release


