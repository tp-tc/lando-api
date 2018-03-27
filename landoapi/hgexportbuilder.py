# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Module for constructing Mercurial patches in 'hg export' format.
"""

HG_EXPORT_PATCH_TEMPLATE = """
# HG changeset patch
# User {author_name} <{author_email}>
# Date {patchdate}
{commit_message}

{diff}
""".strip()


def build_patch_for_revision(
    diff, author_name, author_email, commit_message, date_modified
):
    """Generate a 'hg export' patch using Phabricator Revision data.

    Args:
        diff: A string holding a Git-formatted patch.
        author: A string with information about the patch's author.
        commit_message: A string containing the full commit message.
        date_modified: (int) A number of seconds since Unix Epoch representing
            the date when revision was modified.

    Returns:
        A string containing a patch in 'hg export' format.
    """
    # Back-date the patch to the last modification date of the Revision it's
    # based on.
    patchdate = '%s +0000' % date_modified

    return HG_EXPORT_PATCH_TEMPLATE.format(
        author_name=no_line_breaks(author_name),
        author_email=no_line_breaks(author_email),
        patchdate=patchdate,
        commit_message=commit_message,
        diff=diff,
    )


def no_line_breaks(s):
    """Return s with all line breaks removed."""
    return s.replace('\n', '').replace('\r', '')
