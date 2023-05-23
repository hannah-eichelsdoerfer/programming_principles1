# Problem: 
# Write a program that 
#   - prompts for the names of a source file to read 
#   - and a target file to write, and copy the content of the source file to the target file, but with all empty lines removed, 
#   - then output the number of empty lines removed.

# Example:
# Source file name: string_doc.txt
# Target file name: string_doc_nonempty.txt
# Lines removed: 16


empty_lines_count = 0

path1 = input("What file to copy from: ")
f1 = open(path1)

path2 = input("What file to copy to: ")
f2 = open(path2, mode ='w')

line = f1.readline()

while line != "":
  if line.isspace():
    empty_lines_count += 1
  f2.write(line)
  line = f1.readline()
f1.close()
f2.close()

print(f"Lines removed: {empty_lines_count}")