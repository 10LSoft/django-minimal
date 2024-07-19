import sys

from django.core.management import execute_from_command_line

from project.config.settings import settings

if __name__ == "__main__":
    print("Running in DEBUG mode") if settings.DEBUG else None

    execute_from_command_line(sys.argv)
