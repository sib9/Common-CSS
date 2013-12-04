#!/bin/bash
# Tanky Woo @ 2013-11-28 21:20:26

html_name=index.html

markdown_py -x fenced_code -x 'codehilite(guess_lang=False)' index.md -f $html_name

python ConvertToRealHtmlFormat.py $html_name
