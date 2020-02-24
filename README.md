# java compiner 

a simple python script to combine all your java sources in different packages 
to only one file!

is it as simple as copy pastiing all content one after other?
no! of course not, but i wih=sh it was :)))

## this program :
+ handle imports from java util and .., it collect all imports to beginning of destinantion source file 
+ remove all packaging inside project
+ search for classes recusively to find nested packges
+ convert all public classes and public enums and public everything to normal(package access) 
+ ask for main class of project and set that class to **public** 

## this progeam do not:
+ handle imports of inner classes well, it is almost ok but it may cause compile errors of destination file 
+ guanrantee that the destination file compile well, but i did my best
+ handle importing libraries out of your project and java (for exmaple javafx) well


### the best usage for this script is to remove packaging and make a single source file to upload in quera or other online judges

 

## FAQ:
+ why i wrote in python? java isn't better? maybe but i prefer python!
+ is it work on windows? absoloutely not (actually it should be with minor changes but i can't test it because i don't have windows)
+ is it safe? yeah, why not, it just ask for your permission to clean output folder
+ do i need java installed? not for this script, but for compile? yes 
+ do i need python installed? for sure! i tested it with python3

## how to run? 
+ simply run script with: `python3 java_combiner.py` 
+ or run: `chmod +x java_combiner.py` and then `./java_combiner.py'
` 


