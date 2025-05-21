import csv
import requests
import sys


def is_valid_url(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        # Acceptable codes: 200 OK, maybe 3xx redirects
        return response.status_code < 400
    except requests.RequestException as e:
        return False


file_name = "sprayfilm.fr-Top sites linking to this page-2025-05-21.csv"
with open(file_name, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip first line
    for row in reader:
        url = row[0]

        is_valid = is_valid_url("https://" + url)
        if not is_valid:

            print(
                is_valid,
                url,
            )
        # sys.exit(0)
