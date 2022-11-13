

<!--
 * @Author: Innary
 * @Date: 2022-11-11 12:26:10
 * @LastEditors: Innary
 * @LastEditTime: 2022-11-13 17:32:37
-->


## Summary
This is a quick text file transfom script.


you can transfom
`html,md,json,tex,md,ipynb,rst,csv,docx`
to
`html,md,json, tex,ipynb,rst,pptx,docx,txt`

这是一个用来转换文本文件的脚本。
目前支持从
`html,md,json,tex,md,ipynb,rst,csv,docx`
转换为
`html,md,json, tex,ipynb,rst,pptx,docx,txt`



`TextTransfor lastest version 0.0.1`

## Setup
## install
1. clone repository
    ```
    git clone https://github.com/Innary/texttransfor.git
    ```
2. Switch to the root directory of TextTransfor



3. use conda virtual environment
`conda actvate {env_name}`
or install `python>=3.8` first,
then install
    ```
    python setup.py develop
    ```

## uninstall

```
python setup.py develop --uninstall
```


# Usage

You can enter the following commands： 

```
tt -s {source_file_path} -o {output_dir} -of {output_format}
```
or
```
tt -s {source_file_dir} -o {output_dir} -of {output_format}
```

As an example:
```
tt -s README.md -o .\out -of docx
```
or

```
tt -s .\in -o .\out -of docx
```
### Args
```
'--source_path', '-s':  the relative path of the file or the path of the folder where the file is located


'--output_path', '-o':  Output folder path, required
'--source_format', '-sf':  The format of the file, which is automatically recognized by default
'--output_format', '-of':   Format of output file, required
'--input_encoding', '-e':   The encoding format of the file,defult is utf-8
```

