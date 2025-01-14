XXX - Not complete yet!!!

Name

    EXT_index_func

Name Strings

    GL_EXT_index_func

Version

    $Date: 1997/07/22 21:00:55 $ $Revision: 1.1 $

Number

    95

Dependencies

    None

Overview

    This extension provides a way to discard fragments when a comparison
    between the fragment's index value and a reference index fails.  This
    may be used similarly to the alpha test which is available in RGBA mode.

New Procedures and Functions

    void IndexFuncEXT (enum func, float ref)

New Tokens

    Accepted by the <cap> parameter of Enable, Disable, and IsEnabled,
    and by the <pname> parameter of GetBooleanv, GetIntegerv, GetFloatv,
    and GetDoublev:

	INDEX_TEST_EXT

    Accepted by the <pname> parameter of GetBooleanv, GetIntegerv,
    GetFloatv, and GetDoublev:

	INDEX_TEST_FUNC_EXT
	INDEX_TEST_REF_EXT

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

    None

Additions to Chapter 3 of the 1.1 Specification (Rasterization)

    None

Additions to Chapter 4 of the 1.1 Specification (Per-Fragment Operations
and the Frame Buffer)

    A new section is added immediately following section 4.1.3 Alpha Test.

    Index Test

    This step applies only to color index mode.  The index test discards
    a fragment conditional on the outcome of a comparison between the
    incoming fragment's index value and a constant reference value.  The
    comparison is enabled or disabled with the generic Enable and Disable
    commands using the symbolic constant INDEX_TEST_EXT.  When disabled,
    it is as if the comparison always passes.  The test is controlled with

	void IndexFunc (enum func, float ref);
    
    <func> is a symbolic constant indicating the index test function; <ref>
    is a reference value.  <ref> is converted to a fixed-point value
    according to the rules given for a color index in section 2.13.9.  For
    purposes of the index test, the fragment's index value is also rounded
    to the nearest integer representable in the color index portion of the
    framebuffer.  The possible constants specifying the test function are
    NEVER, ALWAYS, LESS, LEQUAL, EQUAL, GEQUAL, GREATER, or NOTEQUAL,
    meaning pass the fragment never, always, if the fragment's index value
    is less than, less than or equal to, equal to, greater than, or not
    equal to the reference value, respectively.

Additions to Chapter 5 of the 1.1 Specification (Special Functions)

    None

Additions to Chapter 6 of the 1.1 Specification (State and State Requests)

    None

Additions to the GLX Specification

    XXX - Not complete yet!!!

GLX Protocol

    XXX - Not complete yet!!!

Errors

    INVALID_ENUM is generated if the <func> parameter of IndexFuncEXT
    is not one of NEVER, ALWAYS, LESS, LEQUAL, EQUAL, GEQUAL, GREATER, or
    NOTEQUAL.

    INVALID_OPERATION is generated if IndexFuncEXT is called between
    execution of Begin and corresponding execution of End.

New State
								Initial
    Get Value				Get Command	Type	Value	Attrib
    ---------				-----------	----	-------	------

    INDEX_TEST_EXT			IsEnabled	B	False	color-buffer/enable
    INDEX_TEST_FUNC_EXT			GetFloatv	Z8	ALWAYS	color-buffer
    INDEX_TEST_REF_EXT			GetFloatv	R	0	color-buffer

New Implementation Dependent State

    None
