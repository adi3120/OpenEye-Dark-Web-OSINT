# OpenEye - Dark Web OSINT Scraper tool

OpenEye is an OSINT (Open Source Intelligence) tool that allows you to fetch data from websites, perform keyword searches, analyze onion URLs, and more.

## Setup

To setup OpenEye on your system follow these steps
- `git clone https://github.com/adi3120/OpenEye-Dark-Web-OSINT` : clone this git repository
- `pip install -r requirements.txt` : Install PIP dependencies
- `Enable tor service` : Enable tor service from terminal or by running tor browser in background
- `install go lang` : Install Go Lang from the offical site( Needed for OnionScan )
- `install OnionScan tool` : Visit and follow the instructions given there - https://github.com/s-rah/onionscan


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
