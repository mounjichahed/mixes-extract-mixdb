
# MixesDB Extractor

## Introduction

The `final_extractor.py` script is designed to extract mix information based on an artist's name from the MixesDB website. Optionally, users can also specify a mix number to further narrow down the results.

## Requirements

To run the script, ensure you have the following libraries installed:

- `requests`
- `re`
- `bs4` (BeautifulSoup)
- `urllib3`

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4 urllib3
```

## Usage

To use the script, navigate to its directory and run:

```bash
python final_extractor.py "Artist Name" --mix_number 123
```

Replace "Artist Name" with the desired artist's name and `123` with the desired mix number (if any).

## Functionality

The script works as follows:

1. Takes the artist's name as input and constructs a URL to search on MixesDB.
2. Sends a request to MixesDB with the constructed URL to retrieve mix data.
3. Parses the returned HTML using BeautifulSoup to extract relevant mix information.
4. Optionally, if a mix number is provided, the script will filter results to match the specified mix number.

---

Created by Mounji CHAHED
