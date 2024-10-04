import os
import sys

# Using tutorial from https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure/24266885#24266885
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)