# Standards

The Log ASCII Standard file format specifications are copied here:

## Version 1.2

- [LAS12.pdf](LAS12.pdf)
- [LAS12_Standards.txt](LAS12_Standards.txt)

## Version 2.0

- [las_20_updated_july2009.pdf](las_20_updated_july2009.pdf)
- [LAS_20_Update_Jan2014.pdf](LAS_20_Update_Jan2014.pdf)
- [LAS_20_Update_Jan2014.txt](LAS_20_Update_Jan2014.txt)

## Version 3.0 (not supported by `lasio` yet)

- [LAS_3_File_Structure.pdf](LAS_3_File_Structure.pdf)

# Specifications

One aim for `lasio` is to provide a method which checks whether a particular LAS
file meets all of the requirements (and recommendations) of the relevant
specification (above).

In order to achieve this, I've pulled out all the statements from the
specifications which are effectively requirements ("LAS files must xyz") or
recommendations ("LAS files should xyz"), and manually listed them in
[specifications.md](specifications.md). This is a machine-readable Markdown
file.

The script [parse_rules_from_markdown.py](parse_rules_from_markdown.py) can then
be run manually to extract each rule (whether a requirement or recommendation)
and create stub code containing a class for each rule.

```
$ python standards/parse_rules_from_markdown.py
from specbase import Specification



class Recommendation_08a2bd5f_V20(Specification):
    '''The "~W" section's "NULL" item is commonly "-9999", "-999.25" or "-9999.25".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L290

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_0e774882_V20(Specification):
    '''Columns in the data section should be right-justified.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L455-L456

    '''
    spec_type = "Recommendation"
    spec_version = 2.0
```

... and so on. 

The idea is that then this code is added or updated manually to the `lasio` code
repository as the file [../lasio/spec/spec_stubs.py](lasio/spec/spec_stubs.py),
and therefore available in the `lasio` package as ``lasio.spec.spec_stubs``.

Then the actual code which checks a LAS file to see whether the requirement is
met or not should be implemented as a class with a ``check(las_file_object) ->
True | False`` method, in the ``[../lasio/spec/checks.py](lasio.spec.checks)``
module. The class should inherit from the relevant requirement class in
``lasio.spec.spec_stubs``.

Later, these classes should also be expanded to have a ``fix(las_file_object) ->
LASFile`` method which would fix the LAS file so that it now abides by the
relevant  requirement/recommendation.

Any functionality common to all requirements/recommendations should be
implemented in the
``[../lasio/spec/specbase.py](lasio.spec.specbase.Specification)`` class.

The final user-facing interface should be accessible from
``[../lasio/spec/__init__.py](lasio.spec)``. I see this as functions or classes
which simply collect the relevant classes from ``lasio.spec.checks`` ad run
them. Methods can be added to ``LASFile`` to call these functions. I'm not sure
what we might end up with but some examples would be:

- ``LASFile().check_conforming() -> True | False``
- ``LASFile().conformity() -> LASConformity`` which provides information on 
  which requirements/recommendations are met and which fail
- ``LASFile().make_conforming(requirements=True, recommendations=False) -> 
  LASFile`` - to make a LAS file conformant to the specification
