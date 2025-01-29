from pathlib import Path
path = Path('vs_python_pi_text.1415926535')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
path.write_text('Pie tastes very good. I have eaten 3.14 pies.')
contents = path.read_text()
print(contents)