import os

with open("com.py", "w") as f:
  
  dif_same = input("Are you going to be using the same file? (true/false)\n")
  if dif_same == "true":
    file = input("Enter file name\n")
    f.write(f"f = '{file}'\n")
  elif dif_same == "false":
    f.write(f"f = input('Enter file name.\n')\n")
  else:
    exit(f"Invalid input! ({dif_same})\n")
    
  comment_char = input("Enter character you want\n")
  my_char = input("Enter the character you used\n")
  
  new_file = (f"fc = '{comment_char}'.join(((open(f, 'r')).read()).split('{my_char}'))", "(open(f, 'w')).write(fc)")

  f.write('\n'.join(new_file))

if dif_same == "true":
    os.system("python com.py")
