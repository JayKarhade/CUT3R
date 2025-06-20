"""
Setup script for installing SEA-RAFT as a package
"""

from setuptools import setup, find_packages

setup(
    name="cut3r",
    version="0.1.0",
    description="CUT3R",
    author="CUT3R Team",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.0",
        "numpy",
        "opencv-python",
        "matplotlib",
        "open3d",
        "pyyaml",
    ],
    python_requires=">=3.7",
)