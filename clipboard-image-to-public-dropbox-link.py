import uuid
import os
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()


DROPBOX_PUBLIC_IMAGE_FOLDER = "/Users/stevenvo/Dropbox\ \(Personal\)/Public/screenshots/"
DROPBOX_USER_ID = "24437878"
PNGPASTE_CMD = "/usr/local/bin/pngpaste"

DROPBOX_PUBLIC_URL = "https://dl.dropboxusercontent.com/u/{}/screenshots/".format(DROPBOX_USER_ID)

# Extract image file from clipboard
unique_filename = str(uuid.uuid4()) + ".png"
file_path = DROPBOX_PUBLIC_IMAGE_FOLDER + "/" + unique_filename
# os.system("{cmd} {filename}".format(cmd=PNGPASTE_CMD, filename=file_path))

out, error = cmdline("{cmd} {filename}".format(cmd=PNGPASTE_CMD, filename=file_path))

# Generate Dropbox URL
direct_link = DROPBOX_PUBLIC_URL + unique_filename
os.system("echo '![]({url})' | pbcopy".format(url=direct_link.strip()))

cmdline("terminal-notifier -title \"Clipboard Image 2 Dropbox\"  -message \"{msg}\"".format(msg = direct_link))
