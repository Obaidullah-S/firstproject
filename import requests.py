import requests
from bs4 import BeautifulSoup
import re


def decode_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text("\n")

    points = []

    for line in text.splitlines():
        line = line.strip()
        parts = re.split(r"\s+", line)

        if len(parts) >= 3:
            try:
                x = int(parts[0])
                char = parts[1]
                y = int(parts[2])
                points.append((x, y, char))
            except ValueError:
                continue

    if not points:
        return

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))