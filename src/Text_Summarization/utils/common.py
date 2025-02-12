import os
from box.exceptions import BoxValueError
import yaml
from Text_Summarization.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and return a ConfigBox object
    
    Args:
        path_to_yaml (Path): path to yaml file
        
        Raises:
            BoxValueError: if the yaml file is not found
            e:empty yaml file or file is not found
            
        Returns:
            ConfigBox: a ConfigBox object
            """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"empty yaml file or file is not found")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """create directories if they don't exist
    
    Args:
        path_to_directories (list): list of directories to create
        verbose (bool, optional): whether to print out the directories created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory created at {path}")
            
            
@ensure_annotations
def get_size(path:Path) -> str:
    """get the size of a file or directory in KB or MB
        Returns:
            str: size of the file or directory
            """
    size_in_kb = round(os.path.getsize(path) / (1024))
    return f"{size_in_kb} KB" if size_in_kb < 1024 else f"{round(size_in_kb / 1024, 2)} MB"