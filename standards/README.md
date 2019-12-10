# Standards

The Log ASCII Standard file format specifications are copied here:

## Version 1.2

- [LAS12.pdf](LAS12.pdf)
- [LAS12_Standards.txt](LAS12_Standards.txt)

## Version 2.0

- [las_20_updated_july2009.pdf](las_20_updated_july2009.pdf)
- [LAS_20_Update_Jan2014.pdf](LAS_20_Update_Jan2014.pdf)
- [LAS_20_Update_Jan2014.txt](LAS_20_Update_Jan2014.txt)

## Version 3.0

- [LAS_3_File_Structure.pdf](LAS_3_File_Structure.pdf)

# Specifications

I've pulled out all the statements like "files must do this", etc, and listed them
succinctly in [specifications.md](specifications.md). This Markdown file is actually
intended to be machine readable, in order to generate stub code for code in ``lasio.spec``,
which actually checks LAS files for conformity and provides a link right back to the
section of the specification that has not been met.

## Generating stub code

Run the Python script ``parse_rules_from_markdown.py``. This will print the source
code for a Python module to stdout:

```bash
$ python standards/parse_rules_from_markdown.py
from specbase import Specification



class Recommendation_08a2bd5f_V20(Specification):
    '''The "~W" section's "NULL" item is commonly "-9999", "-999.25" or "-9999.25".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L290

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_0e774882_V20(Specification):
    '''Columns in the data section should be right-justified.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L455-L456

    '''
    spec_type = "Recommendation"
    spec_version = 2.0
```

... and so on. This output is then added to the lasio repository by hand as the
file ``lasio/spec/spec_stubs.py``.

In order to actually implement a check, follow the pattern shown in ``lasio/spec/checks.py``.
Everything else should be automatic. NOTE: This is a work in progress and as such the code
in that module is not updated yet.
