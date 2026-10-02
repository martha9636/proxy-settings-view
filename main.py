"""Proxy Settings View — Print WinHTTP and user proxy settings. It does not hide a proxy."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='proxy_settings_view',
        description='Print WinHTTP and user proxy settings. It does not hide a proxy.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Proxy Settings View')
    print('What proxy this user actually has.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
