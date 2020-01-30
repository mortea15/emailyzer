from emailyzer.helpers.save_attachments import save_all
def print_body(email):
    print(email.html_as_text)

def print_html(email):
    print(email.html)

def print_attachments(email):
    for attachment in email.attachments:
        print(f'{"=" * 4} {attachment.get("filename")} {"=" * 4}')
        print(f'Filetype: {attachment.get("filetype")}')
        print(f'Encoding: {attachment.get("encoding")}\n')

def print_headers(email):
    for header, value in email.headers.items():
        print(f'{header}: {value}')

def print_to(email):
    print(email.headers.get('To'))

def print_from(email):
    print(email.sender)

def print_subject(email):
    print(email.subject)

def save_attachments(email):
    fnames = save_all(email.attachments)
    return fnames