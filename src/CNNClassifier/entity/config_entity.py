from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # frozen = true makes the class immutable
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_data_flie:Path
    unzip_dir:Path
    

