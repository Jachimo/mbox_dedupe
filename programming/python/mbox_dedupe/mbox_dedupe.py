#!/usr/bin/env python3

''' Unix MBOX Message Deduplicator

MAKE A BACKUP BEFORE USING!

Usage: ./mbox_dedupe.py targetmbox
'''

import sys
import os
import mailbox

# Set to True to do a "dry run" without actually removing messages
dryrun = False

def main(args):
    mbox_name = args[1]
    mbox = mailbox.mbox(mbox_name, create=False)  # do not create new file
    
    mbox.lock() # lock the mbox file
    
    dedupe_by_messageid(mbox)
    
    mbox.flush()
    mbox.close()
    
    return 0


def dedupe_by_messageid(mbox):
    messageids = []
    deletekeys = []
    for key, msg in mbox.iteritems():  # see https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox
        if msg['Message-ID'] not in messageids:
            messageids.append(msg['Message-ID'])
        elif msg['Message-ID'] in messageids:
            if dryrun:
                print('DRY RUN: Delete ' + msg['Message-ID'])
            else:
                deletekeys.append(key)
    for key in deletekeys:  # Avoids "RuntimeError: dictionary changed size during iteration" issue
        mbox.remove(key)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Specify target mbox file for deduplication.\n")
        sys.exit(1)
    sys.exit( main( sys.argv ) )
