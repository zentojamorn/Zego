XXX - Not complete yet!!!

Name

    EXT_index_material

Name Strings

    GL_EXT_index_material

Version

    $Date: 1997/07/22 21:00:58 $ $Revision: 1.1 $

Number

    94

Dependencies

    None

Overview

    This extends color index lighting to include a way for the current
    index to contribute to the color index produced by lighting.  This
    works much like ColorMaterial does for RGBA lighting by allowing
    one or more color index material properties to be attached to the
    current index.

    The color index lighting formula is also modified so that the lit
    color index may be bitwise shifted in order to allow greater control
    when using lighting and fog together in color index mode.

New Procedures and Functions

    void IndexMaterialEXT (enum face, enum mode )

New Tokens

    Accepted by the <cap> parameter of Enable, Disable, IsEnabled,
    and by the <pname> parameter of GetBooleanv, GetIntegerv,
    GetFloatv, and GetDoublev:

	INDEX_MATERIAL_EXT

    Accepted by the <pname> parameter of GetBooleanv, GetIntegerv,
    GetFloatv, and GetDoublev:

	INDEX_MATERIAL_PARAMETER_EXT
	INDEX_MATERIAL_FACE_EXT

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

    In Section 2.13.5 "Color Index Lighting", the discussion of color
    index lighting is continued after the computation of the final color
    index as follows:

    Arithmetic on Color Indexes

    After a final color index is computed, the index is converted to a
    fixed-point value with an unspecified number of bits to the right
    of the binary point, the nearest fixed-point value is selected.
    Then the fixed-point value is shifted by |index_shift| bits, left
    if index_shift is > 0 and right otherwise.  In either case the
    shift is zero filled.  Then the signed integer offset index_offset
    is added to the index.  index_shift and index_offset are set using
    the Material Command with <pname> set to INDEX_SHIFT and
    INDEX_OFFSET respectively.

    Index Material

    It is possible to attach one or more color index material properties
    to the current index, so that they continuously track its value.  This
    behavior is enabled and disabled by calling Enable or Disable with
    the symbolic constant INDEX_MATERIAL_EXT.  The command that controls
    which of these modes is selected is

	void IndexMaterial (enum face, enum mode);
    
    <face> is one of FRONT, BACK, or FRONT_AND_BACK, indicating whether
    the front material, back material, or both are affected by the current
    index.  <mode> must be INDEX_OFFSET.  The replacements made to 
    material properties are permanent; the replaced values remain until
    changed by either sending a new index or by setting a new material
    value when IndexMaterial is not currently enabled to override that
    particular value.  When INDEX_MATERIAL is enabled, the indicated
    parameter or parameters always track the current index.

    Section 2.13.6 "Clamping or Masking" is modified slightly as
    follows: "For a color index, if lighting is enabled, the color index
    is already in fixed-point, otherwise, the index is first converted
    to fixed-point..."

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

    INVALID_ENUM is generated if IndexMaterial parameter <face> is not FRONT,
    BACK, or FRONT_AND_BACK.

    INVALID_ENUM is generated if IndexMaterial parameter <mode> is not
    INDEX_OFFSET.

    INVALID_OPERATION is generated if IndexMaterial is called between
    execution of Begin and the corresponding execution of End.

New State

								Initial
    Get Value				Get Command	Type	Value			Attrib
    ---------				-----------	----	-------			------

    INDEX_MATERIAL_EXT			IsEnabled	B	False			lighting/enable
    INDEX_MATERIAL_PARAMETER_EXT	GetIntegerv	Z1	INDEX_OFFSET		lighting
    INDEX_MATERIAL_FACE_EXT		GetIntegerv	Z3	FRONT_AND_BACK		lighting
    INDEX_SHIFT				GetMaterialfv	2 x R	0			lighting
    INDEX_OFFSET			GetMaterialfv	2 x R	0			lighting

New Implementation Dependent State

    None
