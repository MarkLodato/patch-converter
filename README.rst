Description
-----------

This is a small script to convert a the output of ``git format-patch`` to
something suitable for ``hg import``.  It is not robust, but should work for
most cases.

In particular, it does the following:

* Insert HG changset patch line

* Convert From: to HG User

* Convert Date: to HG Date

* Convert Subject: to the first line of the commit, followed by a blank line.

  - Any leading "Re:" and/or "[.*]" is stripped from the subject.

* Strip all other headers

* Strip everything from "---" to the first "diff --git ..." line.


Why?
----

Because ``hg import`` does not parse the Date: field, and it also does not
strip the extra stuff between "---" and the start of the diff.


Caveats
-------

The output of this script does not match exactly the output of ``hg import``.
It does not remove the extra "index" line after the "diff --git" line, it does
not remove the "--"/version from the end of the file, and it leaves the extra
diff context after the @'s.  All of these should be ignored by ``hg import``.

The script may fail to parse some messages.  It has not been tested
extensively.


Author
------

Mark Lodato <lodatom@gmail.com>
