# Saved Password Stealer

Steal Saved Password On Browser On All Profile

## Disclamer
This tool is for educational purposes only; Any actions and or activities related to this tool are solely your responsibility. The used of this tool can result in criminal charges brought against the persons in question. 
I'll not be held responsible in the event any criminal charges be brought against any individuals misusing this tool to break the law.

## Usage

### Install Module

```python
  pip install selenium
```
### Run Tool

```python
  python find_location.py
```

### Convert To EXE

- Use Script In File Organizer EXE Folder
```python
  # Using Pyinstaller
  Pyinstaller --noconfirm --onefile find_location.py

  # Using Nuitka
  py -m nuitka --mingw64 .\find_location.py --standalone --onefile 
 ```


## Tutorial

You need to use chromedriver.exe to make this tool work and put into same directory with script/exe. chromedriver must have the same version with Chrome. 
Also findlocation can't work in headless mode but i set the chrome location to "window-position=-2000,0" so there's nothing shows on the screen. Only on taskbar.

## Download chromedriver.exe

 - [chromedriver.exe](https://chromedriver.chromium.org/downloads)
 
## Demo
<img src="https://github.com/katakkentut/LocationFinderPython/blob/master/Tutorial/Tutorial.gif" width="700" height="600">
 
 
