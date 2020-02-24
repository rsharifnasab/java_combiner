#!/usr/bin/python3

from os import listdir,mkdir
from os.path import isfile
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import abspath
from shutil import rmtree


imports = []

source_folder = ""
out_folder = ""
out_file = ""

main_class_name = ""


def greet():
    greet_text = """this script will combine all java files
and make one compilable java file for you\n"""
    print(greet_text)

def find_java_files(mypath):
    ans = []
    for f in listdir(mypath):
        new_path = join(mypath, f)
        if isfile(new_path) and f.endswith(".java"):
            ans += [new_path]
        if isdir(new_path):
            ans += find_java_files(new_path) #recursive
    return ans

def clean_packages_from_java_class(class_text):
    lines = class_text.split("\n")
    no_package_lines = [ l for l in lines if not l.startswith("package") ]
    return "\n".join(no_package_lines)

def extract_imports_from_java_class(class_text):
    global imports
    lines = class_text.split("\n")
    no_import_lines = [ l for l in lines if not l.startswith("import") ]

    imports += [ l for l in lines if l.startswith("import") and "java" in l ]
    #dont care about internal imports

    return "\n".join(no_import_lines)

def convert_publics_to_normal(class_text):
    to_replace = {
        "public class" : "class",
        "public enum" : "enum",
        "public abstract class" : "abstract class",
        "public interface" : "interface",
        "public enum" : "enum"
    }

    for original,neww in to_replace.items():
        class_text = class_text.replace(original,neww)

    return class_text


def clean_java_class(file_add):
    class_text = open(file_add).read()

    class_text = clean_packages_from_java_class(class_text)
    class_text = extract_imports_from_java_class(class_text)
    class_text = convert_publics_to_normal(class_text)

    return class_text


def clean_folder(mypath):
    command = input(f"do you want to delete {mypath}?")
    if command not in ["y","Y",""]:
        print("ok so i cant do anything")
        exit(1)

    try:
        if exists(mypath) and isdir(mypath):
            rmtree(mypath)
        mkdir(mypath)
    except Exception as e:
            print(e)
            exit(1)

def write_file(file_add,text):
    print(f"writing to {file_add}")
    f = open(file_add, "w") #write mode
    f.write(text)
    f.close()



def get_info_from_user():
    global source_folder
    global out_folder
    global out_file
    global main_class_name

    source_folder = abspath( input("enter path of your src folder: ") )
    print(f"src folder is: {source_folder}")

    default_out = abspath( (source_folder+"/../out/").replace(r"//","/") )
    print(f"default out folder is: {default_out}")

    out_folder = input("enter out folder (nothing to use default): ")
    out_folder = default_out if out_folder == '' else abspath(out_folder)
    print(f"out folder is : {out_folder}\n")

    main_class_name = input("enter your main class name: ")
    main_class_name = main_class_name.split(".")[0]

    out_file = out_folder+"/"+main_class_name+".java"
    print(f"out file is : {out_file}\n")


def combine_javas(cleaned_javas):
        global imports
        imports = set(imports)
        imports_text = "\n".join(imports)

        classes_text = "\n/************ next file **********/\n".join(cleaned_javas)

        all_text = imports_text + "\n" + classes_text
        all_text = all_text.replace(f"class {main_class_name}", f"public class {main_class_name}")
        return all_text


greet()
get_info_from_user()

file_list = find_java_files(source_folder)
cleaned_javas = [ clean_java_class(java_file) for java_file in file_list ]
combined_text = combine_javas(cleaned_javas)
clean_folder(out_folder)
write_file(out_file,combined_text)
print("done")
