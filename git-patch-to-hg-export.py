#!/usr/bin/env python

from email.utils import parsedate_tz, mktime_tz
import re

def git_patch_to_hg(fin, fout):
    fout.write('# HG changeset patch\n')

    subject_re = re.compile(r'^(RE:)?\s*(\[[^]]*\])?\])?\s*', re.I)

    # headers
    for line in fin:
        if line.startswith('From: '):
            fout.write('# User %s' % line[6:])
        elif line.startswith('Date: '):
            t = parsedate_tz(line[6:])
            timestamp = mktime_tz(t)
            timezone = -t[-1]
            fout.write('# Date %d %d\n' % (timestamp, timezone))
        elif line.startswith('Subject: '):
            subject = subject_re.sub('', line[9:])
            fout.write(subject + '\n')
        elif line == '\n' or line == '\r\n':
            break

    # commit message
    for line in fin:
        if line == '---\n':
            break
        fout.write(line)

    # skip over the diffstat
    for line in fin:
        if line.startswith('diff --git'):
            fout.write('\n' + line)
            break

    # diff
    # NOTE: there will still be an index line after each diff --git, but it
    # will be ignored
    for line in fin:
        fout.write(line)

    # NOTE: the --/version will still be at the end, but it will be ignored

if __name__ == "__main__":
    import sys
    git_patch_to_hg(sys.stdin, sys.stdout)

