New-Item -Path .\FlashUploader -ItemType Directory
Copy-Item ..\languages.py .
Copy-Item ..\SerialCommunication.py .
Copy-Item ..\Flash_Uploader.py .
Copy-Item ..\defaultConfig.txt .
Copy-Item ..\release -Recurse .

pyinstaller -F -i .\Petoi.ico .\Flash_Uploader.py

Copy-Item .\dist\Flash_Uploader.exe .\FlashUploader
Copy-Item .\Petoi.ico .\FlashUploader
Copy-Item .\avrdude.exe .\FlashUploader
Copy-Item .\avrdude.conf .\FlashUploader
Copy-Item .\libusb0.dll .\FlashUploader
Move-Item .\defaultConfig.txt .\FlashUploader
Move-Item .\release .\FlashUploader

Remove-Item .\languages.py
Remove-Item .\SerialCommunication.py
Remove-Item .\Flash_Uploader.py