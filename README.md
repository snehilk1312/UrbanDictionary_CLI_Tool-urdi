# UrbanDictionary_CLI_Tool  - urdi
Use urban dictionary from your command line

#### Without Piping into "less" : 
command ran : ***$  urdi "Schrödinger's Douchebag"***

![without pipeing](https://github.com/snehilk1312/UrbanDictionary_CLI_Tool-urdi/blob/main/output_screenshots/without_less.png?raw=true)

#### With Piping into "less"  :
command ran : ***$  urdi "Schrödinger's Douchebag" | less***


![with piping](https://github.com/snehilk1312/UrbanDictionary_CLI_Tool-urdi/blob/main/output_screenshots/with_less.png?raw=true)



## For \*nix systems: 
### To run this code from anywhere in terminal, do as follows:

#### 1. git clone https://github.com/snehilk1312/UrbanDictionary_CLI_Tool-urdi.git
#### 2. cd UrbanDictionary_CLI_Tool-urdi/urdi/
#### 3  pip3 install -r requirements.txt
#### 4. In home directory : mkdir myPythonScripts
#### 5. In .bashrc(if you are in bash) file, add : export PATH="$PATH:/home/user/myPythonScripts"
#### 6. source ~/.bashrc
#### 7. cd myPythonScripts
#### 8. move urdi.py to myPythonScripts: mv ~/UrbanDictionary_CLI_Tool-urdi/urdi/urdi.py ~/myPythonScripts/urdi
#### 9. chmod +x urdi

Upon doing ablove steps we can run "todo" as any similar Linux command line commands(as "cd" , "pwd" , "ls"), with or without arguments.

## For best formatting of text, sometime it maybe required to pipe the output into "less"
