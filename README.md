# emailyzer

*emailyzer* is a Python package and CLI tool to analyze .eml and .msg email files, extracting the data to a common interface.

## Installation
**Optional: Create a virtual environment**
```bash
$ virtualenv .env
$ source .env/bin/activate    # *nix
$ .\.env\Scripts\activate     # win
```
**Install**
```bash
$ git clone git@github.com:mortea15/emailyzer.git
$ cd emailyzer && pip3 install .
```
```bash
$ pip3 install git+ssh://git@github.com/mortea15/emailyzer.git
```
## Usage
### CLI
```bash
$ emailyzer --help
usage: emailyzer (-e .EML FILE | -m .MSG FILE | -f FILE) [-b] [-h] [-a] [-r] [-t] [-o] [-u] [-sa] [-v] [-l]

      -e, --eml                   Parse a .eml file
      -m, --msg                   Parse a .msg file
      -f, --file                  Parse a file (must be either .msg or .eml format)

      -b, --body                  Print the body of the email
      -h, --html                  Print the HTML content of the email
      -a, --attachments           Print the attachments of the email
      -r, --headers               Print the headers of the email
      -t, --to                    Print the to of the email
      -o, --from                  Print the from of the email
      -u, --subject               Print the subject of the email

      -sa, --save-attachments     Save the attachments to disk

      -v, --verbose               Increase verbosity (can be used several times, e.g. -vvv)
      -l, --log-file              Write log events to the file `emailyzer.log`
      --help                      Print this message
```
```bash
// Print the HTML part of the email as plain text (parsed and cleaned)
$ emailyzer -f some_eml.eml -b
// Print the HTML
$ emailyzer -f some_eml.eml -h
```

### Using the module
```python
$ python3
# Import the module
>>> import emailyzer
# Create an object from .msg
>>> email = emailyzer.from_msg(PATH_TO_MSG)
# Create an object from .eml
>>> email = emailyzer.from_eml(PATH_TO_EML)
# Or simply
>>> email = emailyzer.from_file(PATH_TO_FILE)

# Get all IPs and hosts found in the email
>>> print(email.hosts)
['IPaddr1', 'IPaddr2', 'domain.tld', 'IPaddr3']
# Get sender
>>> print(email.sender)
First Last <address>
# Get HTML
print(email.html)
# Get the HTML as plain text (parsed and cleaned)
print(email.html_as_text)
```

## Resources
