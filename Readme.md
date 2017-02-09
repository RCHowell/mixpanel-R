## Introduction
These two scripts make it super easy to export your Mixpanel data and load it into R. I've run everything on OSX 10.12.3, but these scripts have very little to do with your operating system. The only step that changes based upon OS is creating your secret.txt file which can be done without a command.


## Requirements
**R	> 3.0.0**

**Python 2.7.x**

## Usage
### 1. Create `secret.txt` in the Root Directory
```bash
# Run this in your terminal
echo "YOUR SECRET" >> ./secret.txt
```

### 2.a From Terminal
```bash
# Run this in your terminal
./python export.py 'event1,event2,...' from_date to_date
```

### 2.b From R
The script `main.r` contains instructions. It is highly likely that you will only run `export.py` from within the R script. Within the R script, be sure to set the proper working directory to the directory containing export.py.
