#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import base64


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parlorpal.settings")
    if "GOOGLE_CREDENTIALS_B64" in os.environ:
        cred_path = "/tmp/google-credentials.json"
        with open(cred_path, "wb") as f:
            f.write(base64.b64decode(os.environ["GOOGLE_CREDENTIALS_B64"]))
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

