# Simple mbox de-duplicator

A simple utility program to remove duplicate messages in a Unix mbox
file, using Message-IDs.

## Usage

The script takes one argument, which is the name of the mbox file to
be deduplicated.  E.g.:

    ./mbox_dedupe.py targetmbox

The script assumes that a valid path to Python 3 can be found via
`/usr/bin/env python3`; if this is not the case, you can specify the
Python interpreter explicitly:

    python3 mbox_dedupe.py targetmbox

The `targetmbox` file must be a valid Unix mbox, containing messages
with valid and meaningful `Message-ID` headers.  This is the case for
nearly all mbox files produced by modern MTAs and MUAs, but may not be
true for extremely old mail archives, or if message headers were
stripped from the file for some reason.

**Make sure to create a backup first, since the utility is potentially
destructive!**

## Notes

There are many other ways to dedupe mailbox files, including more
sophisticated approaches that analyze the message content, timestamps,
hashes, etc.  This program doesn't do any of that.  It looks purely at
the `Message-ID` and assumes that if the ID is the same, that the rest
of the message probably is, too.

As a result, this might not be a good fit for cases where messages
might have been copied, modified, and re-added to the mbox (but
without changing the Message-ID).  In particular, using it on "Drafts"
mailboxes may go poorly, as many (most? all?) MUAs do not insert
Message-IDs for drafts.

But it works well in situations where you may have inadvertently
combined two mailboxes containing some duplicated messages.
It can also facilitate easier exporting of messages from MUAs, by
letting you be pretty sloppy during the export process, since you
don't have to worry about grabbing the same content twice and having
two+ copies of each message in your archives forever.

## Future

This program was created to fill a particular need of mine, and as
such isn't likely to be substantially updated or improved in the near
future.
Anyone is welcome to use it as a starting point for further
improvement, however.

Some possible suggestions for improvement:

- Allow deduplication across multiple mailboxes, e.g. by allowing the
  user to select two (or more) mbox files, and remove all messages
  from the first mbox that are present in the second (or subsequent)
  ones.  This seems like it could be pretty handy for managing
  archives.
- Specify other headers for duplicate detection, besides just
  Message-ID. A combination of to/from/timestamps might yield
  interesting results, as would hashing the message body in various
  ways.

Pull requests always welcome if they maintain the current
functionality and do not greatly decrease performance or introduce
instability or regressions.

