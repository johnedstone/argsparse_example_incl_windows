### Simple example to explain the argsparse module
Here is the `-h` or `--help`:

```
usage: example_argsparse.py [-h] -i INPUT_FILENAME --input-path INPUT_PATH -o OUTPUT_FILENAME [--output-path OUTPUT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input-filename INPUT_FILENAME
                         REQUIRED
  --input-path INPUT_PATH
                        REQUIRED
  -o OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        REQUIRED
  --output-path OUTPUT_PATH
                        Default is current directory

Examples
--------
Windows:
    -i input_file.txt
    --input-path c:\users\username\desktop\
    or
    --input-path c:/users/username/desktop/
Linux:
    -i input_file.txt
    --input-path /home/username/

```
