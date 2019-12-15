from specbase import Specification



class Recommendation_1e0188ff_V20(Specification):
    '''All curves in the data section should be defined in the "~C" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L371-L372

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_295ce2f5_V20(Specification):
    '''The "~W" section's "NULL" item is commonly "-9999", "-999.25" or "-9999.25".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L290

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_33fde11f_V20(Specification):
    '''Columns in the data section should be right-justified.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L455-L456

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_76bc6f36_V20(Specification):
    '''Columns in the data section should be the same width on all lines.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L455-L456

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_ac080c9b_V20(Specification):
    '''The "~W" section's "DATE" item should be formatted "yyyy mm dd".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L325

    '''
    spec_type = "Recommendation"
    spec_version = 2.0


class Recommendation_e774d525_V12(Specification):
    '''The "~V" section should be the first in a file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L238

    '''
    spec_type = "Recommendation"
    spec_version = 1.2


class Requirement_02189a30_V12(Specification):
    '''Exponents are not permitted in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L442

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_04852388_V12(Specification):
    '''The "~C" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L354

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_0506647e_V12(Specification):
    '''If wrapped, all lines will be <= 80 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L255

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_050ee8c6_V20(Specification):
    '''The "STOP" item in the "~W" section must have an evaluated value identical to the first column on the last row of the "~A" data section (after accounting for wrapping), though it can be formatted to a different precision.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L259-L260

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_11935617_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: any characters immediately following the first period in the line are the unit, and these cannot contain a colon.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L195-L196

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_1560c85e_V12(Specification):
    '''The "~V" section must have a "WRAP" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L249

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_156a0dd0_V20(Specification):
    '''The "~W" section must contain a "LIC" item if "PROV" is ""Alberta"".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L344

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_1c3c274a_V20(Specification):
    '''All curves in the "~C" section should exist in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L376

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_1f83dbbf_V12(Specification):
    '''The "~W" section must contain a "FLD" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L305

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_22c3094d_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must contain at least a period, space, and colon in that order.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L178-L185

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_26313cb5_V20(Specification):
    '''The data section should contain a continuous interval i.e. no repeat sections in the same file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L66-68

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_28887504_V12(Specification):
    '''If "START"'s value is greater than "STOP"'s value, then "STEP" must have a minus sign.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L291

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_29d11973_V20(Specification):
    '''If the difference between each data value in the first curve is not identical, then the "STEP" item must have a value of 0.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L287-L288

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_30ec9f97_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then index values in the data section should be increasing from row to row.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L272

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_319e82b7_V12(Specification):
    '''The "~W" section must contain either a "UWI" or "API" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L324-L328

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_31d4c381_V12(Specification):
    '''The "~W" section must contain a "LOC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L308

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_32382858_V12(Specification):
    '''The "~W" section must contain a "WELL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L302

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_3a0eca5e_V20(Specification):
    '''The "~V" section must have a "WRAP" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L223-L227

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_4bc5615c_V20(Specification):
    '''The "~W" section must contain a "SRVC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L319

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_4cf3bd92_V12(Specification):
    '''The "~W" section must contain a "STOP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L285

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_51363549_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: any characters after the first space following the first period are the data, and must be to the left of the last colon in the line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L201-L203

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_51538f9e_V20(Specification):
    '''The "STRT" item in the "~W" section must have an evaluated value identical to the first column on the first row of the "~A" data section, though it can be formatted to a different precision.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L259-L260

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_5246a495_V20(Specification):
    '''The data "~A" section must be the last section in the file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L450

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_53d5490b_V12(Specification):
    '''"~" must be the first non-space and non-quotation character in a file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L207

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_56bd207b_V12(Specification):
    '''If wrapped, the depth value in the data section will be on its own line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L255

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_57ef6f2c_V20(Specification):
    '''If the first curve has the mnemonic "DEPT" or "DEPTH" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must all have the same unit.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L263-L265

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_58ce23ff_V12(Specification):
    '''All curves in the "~C" section should exist in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L363

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_5a7116e6_V20(Specification):
    '''If wrapped, all lines will be <= 80 chars including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L230-L232

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_5e659217_V12(Specification):
    '''The "~W" section must contain a "COMP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L299

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_6d0fe5c5_V12(Specification):
    '''"#" can appear as the first non-space and non-quotation character on any line above the data section, and will then be treated as a comment line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L215

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_6f8be5cf_V12(Specification):
    '''The "~W" section must contain a "STRT" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L279

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_6fe3e4d3_V20(Specification):
    '''The "~C" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L369

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_720e2c74_V20(Specification):
    '''The filename must end with ".las" (if loaded from a file).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L69

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_72819089_V20(Specification):
    '''The "~W" section must contain a "STEP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L281

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_747d68aa_V12(Specification):
    '''Each column in the data section should be separated by at least one space.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L428

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_76f9bb33_V12(Specification):
    '''In wrapped mode, decimal points must be vertically aligned in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L439

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_7a2b8433_V20(Specification):
    '''Only the ASCII characters 10, 13 and 32-126 inclusive are permitted (others should be converted to spaces).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L60-L63

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_7bd873ea_V12(Specification):
    '''The filename must end with ".las" (if loaded from a file).

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L177

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_7f5ea346_V20(Specification):
    '''The "~W" section must contain a "DATE" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L323

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_83bb03f2_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must not contain a colon before the first period.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L191-L192

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_8600c172_V12(Specification):
    '''All curves in the data section should be defined in the "~C" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L355-L356

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_876b02a6_V12(Specification):
    '''The "~V" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L238

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_8c56ca76_V20(Specification):
    '''The "~W" section must contain a "WELL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L299

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_8f6825de_V20(Specification):
    '''Any customer defined sections - i.e. not "V", "W", "C", "P", "O", or "A" - must be after the "~V" section but before the "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L74-L77

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_945ce7eb_V12(Specification):
    '''The "~W" section must contain a "NULL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L296

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_94c9090c_V12(Specification):
    '''If unwrapped, the maximum line length in the entire file is 256 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L253

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_95616c0b_V12(Specification):
    '''If the increment between depth values in the data section is variable then "STEP" should be zero.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L293

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_977097e5_V20(Specification):
    '''The value of "STOP" divided by the value of "STEP" should be an integer.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L277

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_9b47b40c_V20(Specification):
    '''The "~W" section must contain a "STOP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L275

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_9da09c06_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must have the same unit.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L264-L266

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_9e6f699e_V20(Specification):
    '''Line termination should be ASCII 13 ASCII 10.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L64-L65

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_a1aad622_V20(Specification):
    '''The "~W" section must contain either a "UWI" or "API" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L327-L337

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_a6803691_V20(Specification):
    '''For every non-comment line in the "~V", "~W", "~C" and "~P" sections: it must only contain spaces at the start and end of the mnemonic, not in the middle.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L192-L193

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_a8e1c57e_V20(Specification):
    '''Comment lines with "#" as the first non-space character can occur anywhere above the "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L170-L173

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_aef5d20f_V20(Specification):
    '''If the first curve is "DEPT" or "DEPTH" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must have a unit of either "M", "F", or "FT".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L263-L265

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_aef71ce0_V20(Specification):
    '''The "~W" section must contain a "NULL" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L290

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b08e59a3_V20(Specification):
    '''The "~V" section must be the first section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L212

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b0c1e0d9_V20(Specification):
    '''Each column in the data section should be separated by at least one space.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L453

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b41da740_V20(Specification):
    '''If wrapped, all lines in the data "~A" section will be <= 80 characters including "\r" and "\n".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L459-L460

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b6f149ca_V20(Specification):
    '''The first curve item must have a mnemonic of either "DEPT", "DEPTH", or "TIME".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L378-L379

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_b92251b6_V20(Specification):
    '''If the first curve's value increases, then the "STEP" item should be positive, otherwise if it decreases, it should be negative.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L283-L287

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_bcfa4a30_V20(Specification):
    '''If wrapped, the depth value in the data section will be on its own line.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L458

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_c8398d9a_V20(Specification):
    '''Sections begin with a tilde as the first non-space character and are uniquely defined by the following character, therefore only one of each section is permitted per LAS file.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L70-L73

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_c86e987a_V20(Specification):
    '''The "~W" section must contain a "COMP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L295

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_ca22faa4_V20(Specification):
    '''The value of "STRT" divided by the value of "STEP" should be an integer.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L272-L273

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_cc44a0ca_V12(Specification):
    '''The "~V" section must have a "VERS" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L246

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_d12c85e6_V20(Specification):
    '''If the differences between each succesive data value in the first curve are identical, then the "STEP" item should be equal to this difference.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L283-L287

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d2573f6f_V20(Specification):
    '''The "~W" section must contain a "STRT" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L256

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d4af44eb_V12(Specification):
    '''The last section in the file must be the data "~A" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L187

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_d551b058_V20(Specification):
    '''Blank lines are not permitted in the data section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L452

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d5864b53_V20(Specification):
    '''If the first curve has the mnemonic "TIME" then the "STRT", "STOP", "STEP" items in the "~W" section, and the first curve itself, must evaluate as an integer or decimal number.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L265-L267

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_d6bf9fd4_V20(Specification):
    '''The "~W" section must contain a "FLD" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L303

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_dc1f9a52_V20(Specification):
    '''The "~W" section must contain a "LOC" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L307

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_df0957a2_V12(Specification):
    '''Either "PROV" or each of the "CNTY", "STAT", and "CTRY" items should be in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L311-L316

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_e0d0b3fa_V12(Specification):
    '''A "SRVC" item must exist in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L318

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_e52f05b2_V12(Specification):
    '''Uppercase characters immediately following a "~" are "reserved for use by the committee".

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L207

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_e8d6b016_V20(Specification):
    '''Either "PROV" or each of the "CNTY", "STAT", and "CTRY" items should be in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L311-L317

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f0cf897f_V20(Specification):
    '''The "~W" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L250

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f5b59a3f_V12(Specification):
    '''The "~W" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L271

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_f606ba86_V20(Specification):
    '''The "~V" section must have a "VERS" item containing fixed content.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L217

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_f7382d97_V12(Specification):
    '''The "~W" section must contain a "STEP" item.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L290

    '''
    spec_type = "Requirement"
    spec_version = 1.2


class Requirement_f78b11ff_V20(Specification):
    '''The "~V" section must exist.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/7ff375/standards/LAS_20_Update_Jan2014.txt#L212

    '''
    spec_type = "Requirement"
    spec_version = 2.0


class Requirement_fcfb425b_V12(Specification):
    '''A "DATE" item must exist in the "~W" section.

    Link to the relevant part of the Log ASCII Standard specification:

    https://github.com/kinverarity1/lasio/blob/c0abaf/standards/LAS12_Standards.txt#L321

    '''
    spec_type = "Requirement"
    spec_version = 1.2


