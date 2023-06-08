from setuptools import setup

setup(
    name='yolo2labelme',
    version='0.0.2',
    py_modules=['yolo2labelme'],
    entry_points={
        'console_scripts': [
            'yolo2labelme = yolo2labelme:main',
        ],
    },
)