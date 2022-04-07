import os

def clear():
    os.system("clear")

def archive(default=True):
    if not(default):
        return
    archive_name=input("Enter the name of the archive[Ex: xyz (or) path/of/the/archive/xyz]:")
    archive_file=input("Enter the file to be compressed(for multiple files, separate with space):")
    compression_level=input("Enter the compression level(1 to 9, higher number means higher compression):") or "9"
    os.system("7z -mmt=on -mx="+compression_level+" "+archive_name+" "+archive_file)


def delete(default=True):
    if not(default):
        return


def extract(default=True):
    if not(default):
        return


def list_files(default=True):
    if not(default):
        return


def test(default=True):
    if not(default):
        return

def update(default=True):
    if not(default):
        return

def main():
    print("[7z archive program]\n")
    value=False
    archive_options=   [["1","a","Create a new archive or add files to existing archive",archive(value)],
                        ["2","d","Delete files from an archive",delete(value)],
                        ["3","e","Extract files from archive",extract(value)],
                        ["4","l","List contents of an archive",list_files(value)],
                        ["5","t","Test archive integrity",test(value)],
                        ["6","u","Update files in archive",update(value)]]
    value=True
    print("Listing available options:")
    for x in archive_options:
        print("   "+x[0]+")"+x[1]+"("+x[2]+")")
    ans = input("Enter the option number or name(Leave blank to exit)[Ex:1 (or) a]:")
    if not(ans):
        exit()
    for x in archive_options:
        if ans.lower() in x:
            x[3]
            return
    print("\nInvalid option! Try again")
    return main()

clear()
main()