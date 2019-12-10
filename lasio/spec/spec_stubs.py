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


class Recommendation_3bde8349_V12(Specification):
    '''The "~V" section should be the first in a file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L238

    '''
    spec_type = "Recommendation"
    spec_version = 1.2


class Recommendation_6eb1a614_V20(Specification):
    '''Columns in the data section should be the same width on all lines.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L455-L456

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_8bed560a_V20(Specification):
    '''The "~W" section's "DATE" item should be formatted "yyyy mm dd".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L325

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Requirement_02498b77_V12(Specification):
    '''The "~W" section must contain a "STOP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L285

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_02498b77_V20(Specification):
    '''The "~W" section must contain a "STOP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L275

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_155977ae_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must have the same unit.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L264-L266

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_164f0b3b_V20(Specification):
    '''Line termination should be ASCII 13 ASCII 10.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L64-L65

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_182dfbeb_V20(Specification):
    '''The value of "STOP" divided by the value of "STEP" should be an integer.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L277

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_1972c610_V12(Specification):
    '''The "~W" section must contain a "STRT" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L279

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_1972c610_V20(Specification):
    '''The "~W" section must contain a "STRT" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L256

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_1ca43442_V12(Specification):
    '''The "~V" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L238

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_1ca43442_V20(Specification):
    '''The "~V" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L212

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_21282381_V20(Specification):
    '''The first curve item must have a mnemonic of either "DEPT", "DEPTH", or "TIME".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L378-L379

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_252bd2c0_V12(Specification):
    '''In wrapped mode, decimal points must be vertically aligned in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L439

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_28054151_V12(Specification):
    '''All curves in the "~C" section should exist in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L363

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_28054151_V20(Specification):
    '''All curves in the "~C" section should exist in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L376

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_298af068_V12(Specification):
    '''The "~W" section must contain a "LOC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L308

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_298af068_V20(Specification):
    '''The "~W" section must contain a "LOC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L307

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_2ab6770f_V12(Specification):
    '''The "~W" section must contain either a "UWI" or "API" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L324-L328

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_2ab6770f_V20(Specification):
    '''The "~W" section must contain either a "UWI" or "API" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L327-L337

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_2c5f39e3_V20(Specification):
    '''If the first curve is "DEPT" or "DEPTH" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must have a unit of either "M", "F", or "FT".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L263-L265

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_2e226993_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: any characters after the first space following the first period are the data, and must be to the left of the last colon in the line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L201-L203

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_2e3a6a5b_V12(Specification):
    '''The "~C" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L354

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_2e3a6a5b_V20(Specification):
    '''The "~C" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L369

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_30a53620_V20(Specification):
    '''The "~W" section must contain a "SRVC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L319

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_37f0e2ce_V12(Specification):
    '''"#" can appear as the first non-space and non-quotation character on any line above the data section, and will then be treated as a comment line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L215

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_3e11989c_V20(Specification):
    '''Sections begin with a tilde as the first non-space character and are uniquely defined by the following character, therefore only one of each section is permitted per LAS file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L70-L73

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_3eab6146_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must only contain spaces at the start and end of the mnemonic, not in the middle.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L192-L193

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_40963f36_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: any characters immediately following the first period in the line are the unit, and these cannot contain a colon.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L195-L196

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_47cc2c6e_V12(Specification):
    '''If unwrapped, the maximum line length in the entire file is 256 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L253

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_4c2ab507_V20(Specification):
    '''The "STOP" item in the "~W" section must have an evaluated value identical to the first column on the last row of the "~A" data section (after accounting for wrapping), though it can be formatted to a different precision.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L259-L260

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_4c69d6cf_V20(Specification):
    '''The value of "STRT" divided by the value of "STEP" should be an integer.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L272-L273

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_54d61702_V12(Specification):
    '''If the increment between depth values in the data section is variable then "STEP" should be zero.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L293

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_593de2b6_V12(Specification):
    '''If wrapped, all lines will be <= 80 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L255

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_5bd0c6fb_V12(Specification):
    '''The filename must end with ".las" (if loaded from a file).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L177

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_5bd0c6fb_V20(Specification):
    '''The filename must end with ".las" (if loaded from a file).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L69

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_63fb8a44_V12(Specification):
    '''A "SRVC" item must exist in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L318

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_65ff1e7f_V20(Specification):
    '''If the first curve has the mnemonic "DEPT" or "DEPTH" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must all have the same unit.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L263-L265

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_6bd5b8a1_V20(Specification):
    '''Any customer defined sections - i.e. not "V", "W", "C", "P", "O", or "A" - must be after the "~V" section but before the "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L74-L77

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_6ed92e2f_V12(Specification):
    '''The "~W" section must contain a "NULL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L296

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_6ed92e2f_V20(Specification):
    '''The "~W" section must contain a "NULL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L290

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_6edd61eb_V12(Specification):
    '''If wrapped, the depth value in the data section will be on its own line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L255

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_6edd61eb_V20(Specification):
    '''If wrapped, the depth value in the data section will be on its own line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L458

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_6f98f1b6_V20(Specification):
    '''Comment lines with "#" as the first non-space character can occur anywhere above the "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L170-L173

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_74d93cc2_V20(Specification):
    '''The "~W" section must contain a "DATE" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L323

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_77d68e4d_V20(Specification):
    '''The data "~A" section must be the last section in the file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L450

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_7f5f2413_V12(Specification):
    '''Each column in the data section should be separated by at least one space.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L428

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_7f5f2413_V20(Specification):
    '''Each column in the data section should be separated by at least one space.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L453

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_8064dcdf_V12(Specification):
    '''If "START"'s value is greater than "STOP"'s value, then "STEP" must have a minus sign.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L291

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_817d9e80_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must not contain a colon before the first period.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L191-L192

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_818db293_V12(Specification):
    '''The "~W" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L271

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_818db293_V20(Specification):
    '''The "~W" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L250

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_86fb7144_V12(Specification):
    '''The "~W" section must contain a "WELL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L302

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_86fb7144_V20(Specification):
    '''The "~W" section must contain a "WELL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L299

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_893fbc09_V20(Specification):
    '''If the difference between each data value in the first curve is not identical, then the "STEP" item must have a value of 0.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L287-L288

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_98adef59_V12(Specification):
    '''A "DATE" item must exist in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L321

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_998e52e9_V12(Specification):
    '''The last section in the file must be the data "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L187

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_9d35e0f4_V12(Specification):
    '''The "~W" section must contain a "STEP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L290

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_9d35e0f4_V20(Specification):
    '''The "~W" section must contain a "STEP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L281

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_9ddc616b_V12(Specification):
    '''The "~W" section must contain a "COMP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L299

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_9ddc616b_V20(Specification):
    '''The "~W" section must contain a "COMP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L295

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_a6f400ad_V20(Specification):
    '''The "~W" section must contain a "LIC" item if "PROV" is ""Alberta"".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L344

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_a76c7fbf_V12(Specification):
    '''Uppercase characters immediately following a "~" are "reserved for use by the committee".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L207

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_a9548971_V12(Specification):
    '''Exponents are not permitted in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L442

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_abb4aa9b_V20(Specification):
    '''Only the ASCII characters 10, 13 and 32-126 inclusive are permitted (others should be converted to spaces).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L60-L63

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_ac939d8a_V20(Specification):
    '''The data section should contain a continuous interval i.e. no repeat sections in the same file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L66-68

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b8a07e05_V20(Specification):
    '''Blank lines are not permitted in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L452

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_bcbb74d7_V12(Specification):
    '''"~" must be the first non-space and non-quotation character in a file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L207

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_bf8e8899_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must contain at least a period, space, and colon in that order.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L178-L185

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_c56fbf40_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then index values in the data section should be increasing from row to row.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L272

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_ce1be5e2_V20(Specification):
    '''The "STRT" item in the "~W" section must have an evaluated value identical to the first column on the first row of the "~A" data section, though it can be formatted to a different precision.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L259-L260

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_cefc3fe5_V12(Specification):
    '''Either "PROV" or each of the "CNTY", "STAT", and "CTRY" items should be in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L311-L316

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_cefc3fe5_V20(Specification):
    '''Either "PROV" or each of the "CNTY", "STAT", and "CTRY" items should be in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L311-L317

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d2213008_V12(Specification):
    '''The "~W" section must contain a "FLD" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L305

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_d2213008_V20(Specification):
    '''The "~W" section must contain a "FLD" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L303

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d7a5ecdc_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must evaluate as an integer or decimal number.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L265-L267

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_db68c8a7_V20(Specification):
    '''If the first curve's value increases, then the "STEP" item should be positive, otherwise if it decreases, it should be negative.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L283-L287

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_dc117f06_V12(Specification):
    '''The "~V" section must have a "VERS" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L246

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_dc117f06_V20(Specification):
    '''The "~V" section must have a "VERS" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L217

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_e19bf57a_V12(Specification):
    '''All curves in the data section should be defined in the "~C" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L355-L356

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_e19bf57a_V20(Specification):
    '''All curves in the data section should be defined in the "~C" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L371-L372

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_eb45a69c_V12(Specification):
    '''The "~V" section must have a "WRAP" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaffc1656e7acdfdb12efff37d0f2cf845c66/standards/LAS12_Standards.txt#L249

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_eb45a69c_V20(Specification):
    '''The "~V" section must have a "WRAP" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L223-L227

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f2d638cb_V20(Specification):
    '''The "~V" section must be the first section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L212

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f405d6d5_V20(Specification):
    '''If the differences between each succesive data value in the first curve are identical, then the "STEP" item should be equal to this difference.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L283-L287

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f517ebec_V20(Specification):
    '''If wrapped, all lines will be <= 80 chars including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L230-L232

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f9ab0bab_V20(Specification):
    '''If wrapped, all lines in the data "~A" section will be <= 80 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff37548c896bd50f08671e638ab35720f272591/standards/LAS_20_Update_Jan2014.txt#L459-L460

    '''
    spec_type = "Requirement"
    spec_version = 2.0


