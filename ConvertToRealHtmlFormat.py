#!/usr/bin/env python

import sys

def get_html_header():
    header = '''<html xmlns="http://www.w3.org/1999/xhtml">\n'''
    header += "<head>\n"
    header += ''' <link rel="stylesheet"
     href="style.css" type="text/css">\n'''
    header += "</head>\n"
    header += "<body>\n"
    
    return header

def get_html_footer():
    footer = "</body>\n</html>\n"
    return footer

html_name = 'index.html'
if len(sys.argv) > 2:
    html_name = sys.argv[1]

print html_name

# read
file_in = open(html_name, 'r')
content = file_in.read()
file_in.close()

# fill
full_content = get_html_header()
full_content += content
full_content += get_html_footer()

# write
file_out = open(html_name, 'w')
file_out.write(full_content)
file_out.close()
