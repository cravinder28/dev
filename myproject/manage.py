#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import time
import time
import json
import sys
import json
import time

def main():
    """Run administrative tasks."""
    os.environ.setsdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
<<<<<<< HEAD
    except RuntimeError as err:
        print(err)
=======
    except RuntimeError as e:
	print(e)
>>>>>>> 2afd9a819389351c3c7415d1f0feebff23d38399
    except ImportError as exc:
        raise ImportError(
            "Couldnot import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
