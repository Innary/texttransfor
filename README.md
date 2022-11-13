

<!--
 * @Author: Innary
 * @Date: 2022-11-11 12:26:10
 * @LastEditors: Innary
 * @LastEditTime: 2022-11-11 23:56:58
-->


## Summary
This is a quick copy of PDF text and remove line breaks, while you can cut the copied content  to sentence by sentence.


这是一个用来复制PDF并且可以按照句子切分段落的脚本。


**WARNING**


This script can only work on windows , no support for linux for now.






`PDFcopy lastest version 0.0.2`

## Setup
## install
1. clone repository
    ```
    git clone https://github.com/Innary/pdfcopy.git
    ```
2. Switch to the root directory of PDFcopy



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
## Enter

type： 

```
pcp
```
in cmd.exe, then you can use `ctrl + c` and `ctrl + v` to copy&paste content in PDF
### Args
You can also use:
```
pcp -s
```
to split sentence.

## Exit
type：
```
ctrl + c
```
in cmd.exe