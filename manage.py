#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "glowstick.settings")

    from django.core.management import execute_from_command_line
    import dotenv

    dotenv.read_dotenv(os.environ.get("ENV_FILE"))
    execute_from_command_line(sys.argv)
