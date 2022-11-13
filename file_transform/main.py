#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-12 23:22:20
@ LastEditors: Innary
@ LastEditTime: 2022-11-13 16:51:12
'''
import argparse
from tqdm import tqdm
from typing import Union, Generator
from pathlib import Path
import os
from glob import glob
def get_args_parser():
    parser = argparse.ArgumentParser('file format transform', add_help=False)
    parser.add_argument('--source_path', '-s', type=str, required=True)
    parser.add_argument('--output_path', '-o', type=str, required=True)
    parser.add_argument('--source_format', '-sf', type=Union[str, None] ,default=None,
                        choices=['html','md','json', 'tex','md','ipynb','rst','csv','docx'])
    parser.add_argument('--output_format', '-of', type=str, required=True,
                        choices=['html','md','json', 'tex','ipynb','rst','pptx','docx','txt'])
    parser.add_argument('--input_encoding', '-e', type=str, default='utf-8')
    return parser 


def file_transform(sourcefile:Union[list, str, Path, Generator],
                    output_format:str,
                    outputfile:Union[None, str, Path]=None,
                    source_format:Union[str, None]=None,
                    encoding:str='utf-8'
                    ) -> str:
    try:
        import pypandoc
        return pypandoc.convert_file(source_file=sourcefile, to=output_format, format=source_format, outputfile=outputfile, encoding=encoding)
    except (IOError, ImportError):
        with open('Error.txt',"a") as f:
            f.write('IOError')
        return


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    root = os.getcwd()
    print('root dir:{}\n'.format(root))

    source_is_file = os.path.isfile(os.path.join(root, args.source_path))
    source_is_dir = os.path.isdir(os.path.join(root, args.source_path))
    output_is_dir = os.path.isdir(os.path.join(root, args.output_path))



    if source_is_file and  not source_is_dir:
        file = os.path.basename(args.source_path)
    elif  not source_is_file and source_is_dir:
        dirs = [_ for _ in glob(args.source_path)]
    else:
        raise IOError('The entered source_path:{} is invalid'.format(args.source_path))
    

    if output_is_dir:
        args.output_path = args.output_path
    else:
        raise IOError('The entered output_path:{} is invalid'.format(args.output_path))

    if source_is_dir and output_is_dir:
        for dir in tqdm(dirs ,colour = 'blue'):
            file_list = Path(dir).glob('*.*')
            for file in tqdm(file_list, leave=False, desc=dir):
        
                op_file_name = os.path.join(args.output_path ,os.path.basename(file).split('.')[0] + '.' + args.output_format)
                if args.output_format == 'txt':
                    args.output_format = 'plain'

                sp = os.path.join(root, file)
                op = os.path.join(root, op_file_name)
                file_transform(sp, args.output_format, op, args.source_format, args.input_encoding)
                print('output file name:{}\n'.format(op))

        sp = os.path.join(root, file)
        op = os.path.join(root, op_file_name)
        file_transform(sp, args.output_format, op, args.source_format, args.input_encoding)
        print('output file name:{}\n'.format(op))


    elif source_is_file and output_is_dir:
        for _ in tqdm(range(1) ,colour = 'blue',desc=file):
            op_file_name = os.path.join(args.output_path ,file.split('.')[0] + '.' + args.output_format)
            if args.output_format == 'txt':
                args.output_format = 'plain'
            sp = os.path.join(root, args.source_path)
            op = os.path.join(root, op_file_name)
            file_transform(sp, args.output_format, op, args.source_format, args.input_encoding)
            print('output file name:{}\n'.format(op))
    else:
        raise ValueError('no support')
    

if __name__ == "__main__":         
    main()