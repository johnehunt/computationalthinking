from pathlib import Path

print('Create Path object for current directory')
p = Path('info.dat')
print('p:', p)
print('p.exists():', p.exists())
print('p.is_dir():', p.is_dir())
print('p.is_file():', p.is_file())
print('p.absolute():', p.absolute())

if p.exists():
    print('yes the file exists')
    for l in open(str(p.absolute())):
        print(l)


home = str(Path.home())
print(home)
