#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VLA_project.settings")

    from django.core.management import execute_from_command_line
    # Force IP for testing server
    if ('test' in sys.argv):
	sys.argv = ['manage.py','runserver','162.243.224.139:6666']
    execute_from_command_line(sys.argv)
