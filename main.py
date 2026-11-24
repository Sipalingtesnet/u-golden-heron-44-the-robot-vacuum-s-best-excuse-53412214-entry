#!/usr/bin/env python3
"""Write the robot vacuum's excuse to /output/entry.txt"""

import os

EXCUSE = "My bumper hit something warm — logged 'cat', aborted. I don't vacuum court."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()