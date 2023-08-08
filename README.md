# yolo2labelme

Tool to convert yolo format dataset to labelme json format.

## Installation
```bash
pip install yolo2labelme
```
## Usage
Arguments:

`data` : path to dataset directory

Keyword arguments:

`out` : path to output directory. Default dataset is created at same path as data_dir with name labelmeDataset.

`skip` : action to take if `.txt` file corresponding to image is not found.
- `False` (default) raises `FileNotFoundError`.
- `print` prints missing file path to stdout.
- `True` or any other value skips file silently.
### CLI Usage:

Following command creates labelme json dataset directory at `path/to/yolo/labelmeDataset` from `path/to/yolo/dataset` dataset directory.
```bash
yolo2labelme path/to/yolo/dataset
```

Specify output directory, skip.

```bash
yolo2labelme path/to/yoloDataset --out path/to/labelmeJsonDir --skip print
```

### Python Usage:
```python
from yolo2lableme import yolo2labelme
yolo2labelme('path/to/yolo/dataset')
```
With output directory and skip action
```python
yolo2labelme('path/to/yolo/dataset','path/to/labelme/dataset',skip=True)
```
Or simply
```python
from yolo2labelme import y2l
y2l('path/to/dataset')
```
## Useful links
https://github.com/kadapallaNithin/yolo2labelme

https://pypi.org/project/yolo2labelme/

Lableme to yolo : https://pypi.org/project/labelme2yolo/