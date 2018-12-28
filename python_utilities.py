# -*- coding: utf-8 -*-Q
# provide utility method for path lib operation
from pathlib import Path
from typing import List
import datetime
import re

def list_files(parentfolders:List[str],suffixes:List[str]):
    """
    Generator method for path object based on the specified multiple parent folders and mutliple suffixes
    ---------
    Parameters
        parentfolders:List[str]
        suffixes:List[str]
    Returns
        List of Path object
    """
    reg_suffixes = '.(' + '|'.join(suffixes) + ')'
    for folder in parentfolders:
        p = Path(folder)
        for f in p.glob('**/*'):
            if re.search(reg_suffixes, str(f)):
                yield f

def delta_list_files(parentfolders: str, suffixes: List[str],dhours:int):
    """
    Generator method for path object based on the specified multiple parent folders 
    and mutliple suffixes with conditon (delta hours specified)
    ---------
    Parameters
        parentfolders:List[str]
        suffixes:List[str]
    Returns
        List of Path object
    """
    thetime = int((datetime.datetime.now() - datetime.timedelta(hours=dhours)).strftime('%s'))
    for f in list_files(parentfolders=parentfolders,suffixes=suffixes):
        ctime = int(f.stat().st_ctime)
        if ctime > thetime: #指定時間以降に作成されたファイルのみ
            yield f
 