"""
parsing.py

This file provides parsing services
"""

import re

def find_tags(text):
    tag_regex = re.compile("#\w+")
    hashtags = tag_regex.findall(text)
    tag_names = [tag.strip("#").lower() for tag in hashtags]
    return tag_names
