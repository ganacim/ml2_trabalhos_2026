import importlib.resources as res
from pathlib import Path

def data_path(dataset_name=None, create_if_missing=False) -> Path:
    """Returns the path to the data directory. If dataset_name is provided, returns the path to the dataset directory.
    If create_if_missing is True, creates the directory if it does not exist."""
    # get package name
    pkg_name = __name__.split(".")[0]
    # get package path
    with res.path(pkg_name, ".") as path:
        data_path = "/".join(str(path).split("/")[:-1])
    # return data path
    if dataset_name:
        path = Path(data_path) / "data" / dataset_name
    else:
        path = Path(data_path) / "data"
    
    if create_if_missing and not path.exists():
        path.mkdir(parents=True, exist_ok=True)

    return path
