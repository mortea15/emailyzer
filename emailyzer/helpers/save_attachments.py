from datetime import datetime


def save(attachment):
    now = datetime.now().timestamp()
    fname = attachment.get('filename')
    fname = f'{now}-{fname}'
    if isinstance(attachment.get('content'), bytes):
        wt = 'wb'
    elif isinstance(attachment.get('content'), str):
        wt = 'w'
    with open(fname, wt) as f:
        f.write(attachment.get('content'))
        return f.name


def save_all(attachments):
    filenames = []
    for attachment in attachments:
        fname = save(attachment)
        filenames.append(fname)
    return filenames
