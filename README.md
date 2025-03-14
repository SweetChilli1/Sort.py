# Sort.py
Python Script: Sorts files in the directory by creating folders either by name or type of files and then moving the files to the appropriate folders.
#

##  Why this script:
I am a beginner programmer and this is my first script that I publish on Github. 
It's a small project for myself and others.
I think I will develop the script further.
Feel free to give me feedback and suggestions for improvement.
Thanks :)

#


## How to Install:



#### Linux(Bash):


#### Step 1: Clone the repository:
```bash
git clone https://github.com/SweetChilli1/Sort.py.git
cd Sort.py
```


#### Step 2: Move Sort.py to'~/.local/bin/': 
```bash
mv Sort.py ~/.local/bin/ && cd ~/.local/bin
```

#### Step 3: Make the file executable:
```bash
chmod +x Sort.py
mv Sort.py Sort
```

#### Step 4: Refresh terminal/ Clear the cache:
```bash
hash -r
```

#### Finished:
Type the command 'Sort', (capital letter at the beginning) and the script will be executed in the current directory
#


#### Examples:
Help list:
```bash
Sort -h
```

Basic use:
```bash
Sort
```

Sort files by name:
```bash
Sort -n
```

Sort files in another directory:
```bash
Sort -d <~/example/directory>
```
#







