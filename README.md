# OpenEye - Dark Web OSINT Scraper tool

OpenEye is an OSINT (Open Source Intelligence) tool that allows you to fetch data from websites, perform keyword searches, analyze onion URLs, and more.

## Usage

To use OpenEye, you can run the `openeye.py` script with various command line flags to perform different tasks

### Flags

- `-k`: Fetch data from sites by entering keywords.
- `-k -r <file>`: Fetch data from keywords from a file.
- `-u`: Fetch data from the URL entered.
- `-u -r <file>`: Fetch data from URLs from a file.
- `-s -r <file>`: Run OnionScan on a file containing URLs.
- `-s <url>`: Run OnionScan on a URL.
- `-d`: Show data.
- `-h`: Show help.

## Examples

- #### Fetch data using keywords.
  - `python openeye.py -k`

- #### Fetch data from keywords in a file
  - `python openeye.py -k -r keywords.txt`

- #### Fetch data from a specific URL
  - `python openeye.py -u https://example.com`

- #### Fetch data from URLs in a file
  - `python openeye.py -u -r urls.txt`
 
- #### Run OnionScan on a file containing URLs
  - `python openeye.py -s -r urls.txt`

- #### Run OnionScan on a specific URL
  - `python openeye.py -s https://example.onion`

- #### Show data
  - `python openeye.py -d`

- #### Show help
  - `python openeye.py -h`
