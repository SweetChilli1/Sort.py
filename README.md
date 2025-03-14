# Sort.py
Python Script: Sorts files in the directory by creating folders either by name or type of files and then moving the files to the appropriate folders.
#



### How to Install:

#### Linux(Bash):

##### Step 1: Clone the repository:
```bash
git clone https://github.com/SweetChilli1/Sort.py.git
cd Sort.py
```

##### Step 2: If not already present: Create the directory '~/bin/': 
```bash
mkdir ~/bin
```

##### And move Sort.py to ~/bin/:
```bash
mv Sort.py ~/bin/
```

##### Step 3: Make the file executable:
```bash
chmod +x Sort.py
mv Sort.py Sort
```

##### Step 4: Add the path from ~/bin/ to the .bashrc file, if not already present
Open '.bashrc'
```bash
nano ~/.bashrc
```
Add this line at the end of the file (if ~/bin is not already included in the PATH):
```bash
export PATH="$HOME/bin:$PATH"
```

##### Step 5: Refresh terminal/ Clear the cache:
```bash
hash -r
```

##### Finished:
Type the command 'Sort', (capital letter at the beginning) and the script will be executed in the current directory

###### Examples:
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








