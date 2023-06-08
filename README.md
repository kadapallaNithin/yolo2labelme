# yolo2labelme

Tool to convert yolo format dataset to labelme json format.

## Installation
```bash
pip install yolo2labelme
```
## Usage
### CLI Usage:

Following command creates labelme json dataset directory at `path/to/yolo/labelmeDataset` from `path/to/yolo/dataset` dataset directory.
```bash
yolo2labelme path/to/yolo/dataset
```

Specify output directory

```bash
yolo2labelme path/to/yoloDataset --out path/to/labelmeJsonDir
```

### Python Usage:
```python
from yolo2lableme import yolo2labelme
yolo2labelme('path/to/yolo/dataset')
```
With output directory
```python
yolo2labelme('path/to/yolo/dataset','path/to/labelme/dataset')
```
Or simply
```python
from yolo2labelme import y2l
y2l('path/to/dataset')
```
## Useful links
https://github.com/kadapallaNithin/yolo2labelme

https://pypi.org/project/yolo2labelme/