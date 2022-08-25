# DesktopNotification
Has it ever happened to you to sit at the computer or laptop and forget that you have something to do. With this application made with python, requests and plyer you can receive at certain intervals data about the COVID situation in your country.
This app will provide a way to create a customized desktop notifier application for your PC in a few simple steps using python.

We will use request library to get information about coronavirus cases from an website and plyer library to push notification to the desktop

Datetime library will help us push the today data to the bar

We will use JSON libray to transform the data (which is initially in a byte format) to a dict 

P.s This was tested only for Windows 10

If you want to keep running your file so you don't have to execute it again and again, just insert this in your command prompt terminal

pythonw.exe .\<your-file-name-here>
example 
pythonw.exe .\desktopNotifier.py

If you want to close the app just enter in task manager and close it from the processes bar.
