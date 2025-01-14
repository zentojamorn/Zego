XXX - Not complete yet!!!

Name

    EXT_index_array_formats

Name Strings

    GL_EXT_index_array_formats

Version

    $Date: 1997/07/22 21:00:52 $ $Revision: 1.1 $

Number

    96

Dependencies

    None

Overview

    This extends the number of packed vertex formats accepted by
    InterleavedArrays to include formats which specify color indexes
    rather than RGBA colors.

New Procedures and Functions

    None

New Tokens

    Accepted by the <format> parameter of InterleavedArrays

	IUI_V2F_EXT
	IUI_V3F_EXT
	IUI_N3F_V2F_EXT
	IUI_N3F_V3F_EXT
	T2F_IUI_V2F_EXT
	T2F_IUI_V3F_EXT
	T2F_IUI_N3F_V2F_EXT
	T2F_IUI_N3F_V3F_EXT

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

    Table 2.5 is extended to include the following new formats

    format               et ec ei en st sc sv  tc  pc  pi  pn   pv   s
    --------------------------------------------------------------------
    IUI_V2F_EXT          -  -  T  -  -  -  2   -   -   -   -    i   i+2f
    IUI_V3F_EXT          -  -  T  -  -  -  3   -   -   -   -    i   i+3f
    IUI_N3F_V2F_EXT      -  -  T  T  -  -  2   -   -   -   i   i+3f i+5f
    IUI_N3F_V3F_EXT      -  -  T  T  -  -  3   -   -   -   i   i+3f i+6f
    T2F_IUI_V2F_EXT      T  -  T  -  2  -  2   -   -   2f  -   i+2f i+4f
    T2F_IUI_V3F_EXT      T  -  T  -  2  -  3   -   -   2f  -   i+2f i+5f
    T2F_IUI_N3F_V2F_EXT  T  -  T  T  2  -  2   -   -   2f i+2f i+5f i+7f
    T2F_IUI_N3F_V3F_EXT  T  -  T  T  2  -  3   -   -   2f i+2f i+5f i+8f

    i = sizeof(UNSIGNED_INT), rounded up to the nearest multiple of f.

    with corresponding changes to the command sequence used to describe
    the operation of the InterleavedArrays command.

Additions to Chapter 3 of the 1.1 Specification (Rasterization)

    None

Additions to Chapter 4 of the 1.1 Specification (Per-Fragment Operations
and the Frame Buffer)

    None

Additions to Chapter 5 of the 1.1 Specification (Special Functions)

    None

Additions to Chapter 6 of the 1.1 Specification (State and State Requests)

    None

Additions to the GLX Specification

    XXX - Not complete yet!!!

GLX Protocol

    XXX - Not complete yet!!!

Errors

    None

New State

    None

New Implementation Dependent State

    None
