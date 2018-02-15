from setuptools import setup, find_packages


setup(
    name="BatchImageResize",
    version='0.3.6',
    description="Batch resize and compress images with Qt5 GUI.",
    long_description="Batch resize and compress JPG and PNG images.",
    author="Ramil Minnigaliev",
    author_email="minnigaliev-r@yandex.ru",
    url="https://github.com/thunderamur/batch-image-resize",
    license='MIT',
    keywords=['batch image resize', 'resize image'],
    packages=find_packages('src'),
    package_dir={
        'batch_image_resize': 'src/batch_image_resize',
    },
    python_requires='>=3.5',
    install_requires=[
        "pillow>=5.0",
        "PyQt5>=5.9",
    ],
    entry_points={
        'console_scripts': [
            'batch-image-resize = batch_image_resize.resize_console:main',
        ],
        'gui_scripts': [
            'batch-image-resize-qt5 = batch_image_resize.resize_qt5:main',
        ]
    },
)