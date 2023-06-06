#!/usr/bin/env python3

import io
import sys
import zipfile
from pathlib import Path

try:
    import httpx
except ImportError:
    print(
        """
Please create the virtual environment and install the dependencies before
running the script.  If you have already done it, make sure the virtual
environment is activated when running this script.
""",
        file=sys.stderr,
    )
    raise


def check_exists():
    data_dir = Path.cwd() / "data"
    indoor_dir = data_dir / "indoor"
    outdoor_dir = data_dir / "outdoor"
    num_files = 200
    if (
        data_dir.exists()
        and data_dir.is_dir()
        and indoor_dir.exists()
        and indoor_dir.is_dir()
        and outdoor_dir.exists()
        and outdoor_dir.is_dir()
        and len(list(indoor_dir.iterdir())) == num_files
        and len(list(outdoor_dir.iterdir())) == num_files
    ):
        return True

    return False


def main(url: str) -> int:
    if check_exists():
        print("Data already downloaded.")
        return 0

    print("Downloading data...")

    res = httpx.get(url)
    res.raise_for_status()

    print("Extracting data...")

    with zipfile.ZipFile(io.BytesIO(res.content)) as zf:
        zf.extractall()

    print("Done.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
