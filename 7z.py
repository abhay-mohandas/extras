import os

def clear():
    os.system("clear")

def archive():
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    archive_file=input("Enter the file to be compressed(for multiple files, separate with space):")
    types=["7z","zip","tar","gzip","iso"]
    print("List of archive formats:")
    for x in types:
        print("   ) ."+x)
    archive_type=input("Enter the compression format(Leave blank to default to .7z):") or "7z"
    if not(archive_type in types):
        archive_type = "7z"
    compression_level=input("Enter the compression level(1 to 9, higher number means higher compression):") or "9"
    output_add=input("Enter the output location(Leave blank to place the archive in the current directory):") or ""
    if output_add:
        output = "&& mv "+archive_name+" "+output_add
    else:
        output = " "
    os.system("7z a -y -mmt=on -mx="+compression_level+" -t"+archive_type+" "+archive_name+" "+archive_file+" "+output)


def delete():
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    archive_file=input("Optionally enter file names to be deleted from within the archive(Leave space to skip):") or " "
    output_add=input("Enter the output location(Leave blank to place the archive in the current directory):") or ""
    if output_add:
        output = "&& mv "+archive_name+" "+output_add
    else:
        output = " "
    os.system("7z d -y -mmt=on "+archive_name+" "+archive_file+" "+output)
    

def extract():
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    output_add=input("Enter the output location(Leave blank to place the archive in the current directory):") or ""
    if output_add:
        output = "&& mv "+archive_name+" "+output_add
    else:
        output = " "
    os.system("7z e -y -mmt=on "+archive_name+" "+output)


def list_files():
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    os.system("7z l -y "+archive_name)

def test():
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    os.system("7z t -y "+archive_name)


def main():
    print("[7z archive program]\n")
    archive_options=   [["1","a","Create a new archive or add files to existing archive",archive],
                        ["2","d","Delete files from an archive",delete],
                        ["3","e","Extract files from archive",extract],
                        ["4","l","List contents of an archive",list_files],
                        ["5","t","Test archive integrity",test]]
    print("Listing available options:")
    for x in archive_options:
        print("   "+x[0]+")"+x[1]+"("+x[2]+")")
    ans = input("Enter the option number or name(Leave blank to exit)[Ex:1 (or) a]:")
    if not(ans):
        exit()
    for x in archive_options:
        if ans.lower() in x:
            clear()
            x[3]()
            return
    print("\nInvalid option! Try again")
    return main()

clear()
main()
