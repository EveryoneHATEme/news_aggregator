import os
from pathlib import Path
import csv
from common.categories import Categories

base = Path(__file__).parent / "out"
print(base)

if not os.path.exists(base):
    os.mkdir(base)


def write_data(texts: list[str], category: Categories):
    print(texts, category)
    with open(
        base / f"{category.name.lower()}.csv", "w", encoding="utf-8", newline=""
    ) as f:
        print(category)
        writer = csv.writer(f)
        categories = [0 for c in list(Categories)]
        categories[category.value] = 1
        writer.writerows([[text] + categories for text in texts])


def category_exists(category: Categories) -> bool:
    return os.path.exists(base / f"{category.name.lower()}.csv")
