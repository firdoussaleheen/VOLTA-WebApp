import cgi
import sys

form = cgi.FieldStorage()

seachterm =  form.getvalue('searchbox')

f=open('speech.txt', 'w')
f.write(searchterm)
f.close()
