XXX - Not complete yet!!!

Name

    EXT_index_texture

Name Strings

    GL_EXT_index_texture

Version

    $Date: 1997/07/22 21:01:01 $ $Revision: 1.1 $

Number

    93

Dependencies

    EXT_paletted_texture is required

Overview

    This extends the definition of texturing so that it is supported
    in color index mode.  This extension builds on the notion of
    texture images which have color index internal formats which was
    introduced in EXT_paletted_texture.

    This extension also introduces a new texture environment function
    ADD which is useful for combining lighting and texturing in
    color index mode.

Issues

    * EXT_paletted_texture should probably have defined
        TEXTURE_BORDER_INDEX
        TEXTURE_INDEX_SIZE
      Should we go ahead and introduce them in this extension?

    * ADD is defined differently for RGBA mode in SGIX_texture_add_env
      Should we add TEXTURE_ENV_SHIFT and TEXTURE_ENV_OFFSET parameters
      so that the environment functions works similarly?  Probably not.

New Procedures and Functions

    None

New Tokens

    None

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

    None

Additions to Chapter 3 of the 1.1 Specification (Rasterization)

    In Section 3.8, the sentence "Texturing is specified only for RGBA
    mode; its use in color index mode is undefined." is deleted.  And
    the sentence "These details include specification of the image to
    be texture mapped, the means by which the image is filtered when
    applied to the primitive, and the function that determines what
    RGBA value is produced given a fragment color and an image value."
    is modified to read "...determine what RGBA or color index value
    is produced given a fragment color or index...".

    The remaining discussion of texturing is modified as per
    EXT_paletted_texture with the following modifications:

    The discussion of restrictions on the <internalFormat> parameter
    for CopyTexImage1D and CopyTexImage2D is modifies to read: "...except
    that <internalFormat> may not be specified as 1, 2, 3, or 4 nor may
    <internalFormat> be specified using one of the color index internal
    formats unless the GL is in color index mode."

    Use of texture palettes is supported in both RGBA mode and color
    index mode.  The texture palette is applied to color indexes extracted
    from the texture array only when the texture palette has a Luminance,
    Alpha, Luminance Alpha, Intensity, RGB, or RGBA internal format and
    the GL is in RGBA mode or when the texture palette has a color index
    internal format and the GL is in color index mode.  If both the
    texture image and the texture palette have color index internal
    formats and the GL is in RGBA mode, then the texture is inconsistent.

    In Section 3.8.5 "Texture Environments and Texture Functions", the
    sentence discussing possible environment parameters is modified to
    say: "...TEXTURE_ENV_MODE may be set to one of REPLACE, MODULATE,
    DECAL, BLEND, or ADD...".   Also Tables 3.10 and 3.11 are extended
    to include the following new row and column

        Cf is the index from the incoming fragment
        Ct is the filtered texture index
        Cv is the index computed by the texture environment function

    Base            REPLACE   MODULATE  DECAL     BLEND     ADD
    Internal Format Tex Func  Tex Func  Tex Func  Tex Func  Tex Func
    --------------- --------  --------  --------  --------  --------
    .               .         .         .         .         .
    .               .         .         .         .         undef
    .               .         .         .         .         .
    COLOR_INDEX     Cv=Ct     Cv=Cf*Ct  undef     undef     Cv=Cf+Ct
    .               .         .         .         .         .
    .               .         .         .         .         undef
    .               .         .         .         .         .

    In Section 3.8.6 "Texture Application", is modified to include
    a description of what happens in color index mode.  "In RGBA
    mode this function replaces the incoming fragment's R, G, B, and A
    values.  These are the color values passed to subsequent operations.
    In color index mode the resulting index is first masked (bitwise
    ANDed) with 2^n - 1, where n is the number of bits in a color in
    the color index buffer and then passed on to subsequent operations."

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

Dependencies on EXT_paletted_texture

    EXT_paletted_texture is required.  This extension depends on the
    notion of color index internal formats for texture images as introduced
    by EXT_paletted_texture.

    EXT_paletted_texture is modified by this extension by allowing texture
    palettes to be used in color index mode.

Errors

    None

New State

    None

New Implementation Dependent State

    None
