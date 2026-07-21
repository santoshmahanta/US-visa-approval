import os
import sys
import yaml
import dill
import numpy as np

from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging


# ---------------------------------------------------------
# Read YAML File
# ---------------------------------------------------------

def read_yaml_file(file_path: str) -> dict:
    """
    Read a YAML file and return its content as a dictionary.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Write YAML File
# ---------------------------------------------------------

def write_yaml_file(
    file_path: str,
    content: object,
    replace: bool = False
) -> None:
    """
    Write content into a YAML file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Load Object
# ---------------------------------------------------------

def load_object(file_path: str) -> object:
    """
    Load a Python object from a file.
    """

    logging.info("Entered the load_object method of utils")

    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Save NumPy Array
# ---------------------------------------------------------

def save_numpy_array_data(
    file_path: str,
    array: np.array
):
    """
    Save NumPy array data to file.

    file_path: location of file to save
    array: NumPy array data to save
    """

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(
            dir_path,
            exist_ok=True
        )

        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Load NumPy Array
# ---------------------------------------------------------

def load_numpy_array_data(
    file_path: str
) -> np.array:
    """
    Load NumPy array data from file.

    file_path: location of file to load
    return: NumPy array data
    """

    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Save Object
# ---------------------------------------------------------

def save_object(
    file_path: str,
    obj: object
) -> None:
    """
    Save a Python object using dill.
    """

    logging.info("Entered the save_object method of utils")

    try:
        os.makedirs(
            os.path.dirname(file_path),
            exist_ok=True
        )

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        logging.info("Exited the save_object method of utils")

    except Exception as e:
        raise USvisaException(e, sys) from e


# ---------------------------------------------------------
# Drop Columns
# ---------------------------------------------------------

def drop_columns(
    df: DataFrame,
    cols: list
) -> DataFrame:
    """
    Drop columns from a pandas DataFrame.

    df: pandas DataFrame
    cols: list of columns to be dropped
    """

    logging.info("Entered drop_columns method of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")

        return df

    except Exception as e:
        raise USvisaException(e, sys) from e