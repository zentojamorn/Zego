Name

    EXT_paletted_texture

Name Strings

    GL_EXT_paletted_texture

Version

    $Date: 1997/07/22 21:01:04 $ $Revision: 1.1 $

Number

    78

Dependencies

    GL_EXT_paletted_texture shares routines and enumerants with
    GL_SGI_color_table with the minor modification that EXT replaces SGI.
    In all other ways these calls should function in the same manner and the
    enumerant values should be identical.  The portions of
    GL_SGI_color_table that are used are:
		ColorTableSGI, GetColorTableSGI, GetColorTableParameterivSGI, 
		GetColorTableParameterfvSGI.
		COLOR_TABLE_FORMAT_SGI, COLOR_TABLE_WIDTH_SGI,
    		COLOR_TABLE_RED_SIZE_SGI, COLOR_TABLE_GREEN_SIZE_SGI,
    		COLOR_TABLE_BLUE_SIZE_SGI, COLOR_TABLE_ALPHA_SIZE_SGI,
    		COLOR_TABLE_LUMINANCE_SIZE_SGI, COLOR_TABLE_INTENSITY_SIZE_SGI.

    Portions of GL_SGI_color_table which are not used in
    GL_EXT_paletted_texture are:
		CopyColorTableSGI, ColorTableParameterivSGI,
    		ColorTableParameterfvSGI.
		COLOR_TABLE_SGI, POST_CONVOLUTION_COLOR_TABLE_SGI,
    		POST_COLOR_MATRIX_COLOR_TABLE_SGI, PROXY_COLOR_TABLE_SGI,
    		PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI,
    		PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI, COLOR_TABLE_SCALE_SGI,
    		COLOR_TABLE_BIAS_SGI.

    EXT_paletted_texture can be used in conjunction with EXT_texture3D.
    EXT_paletted_texture modifies TexImage3DEXT to accept paletted image
    data and allows TEXTURE_3D_EXT and PROXY_TEXTURE_3D_EXT to be used a
    targets in the color table routines.  If EXT_texture3D is unsupported
    then references to 3D texture support in this spec are invalid and
    should be ignored.

Overview
    
    EXT_paletted_texture defines new texture formats and new calls to
    support the use of paletted textures in OpenGL.  A paletted texture is
    defined by giving both a palette of colors and a set of image data which
    is composed of indices into the palette.  The paletted texture cannot
    function properly without both pieces of information so it increases the
    work required to define a texture.  This is offset by the fact that the
    overall amount of texture data can be reduced dramatically by factoring
    redundant information out of the logical view of the texture and placing
    it in the palette.
    
    Paletted textures provide several advantages over full-color textures:

    * As mentioned above, the amount of data required to define a
    texture can be greatly reduced over what would be needed for full-color
    specification.  For example, consider a source texture that has only 256
    distinct colors in a 256 by 256 pixel grid.  Full-color representation
    requires three bytes per pixel, taking 192K of texture data.  By putting
    the distinct colors in a palette only eight bits are required per pixel,
    reducing the 192K to 64K plus 768 bytes for the palette.  Now add an
    alpha channel to the texture.  The full-color representation increases
    by 64K while the paletted version would only increase by 256 bytes.
    This reduction in space required is particularly important for hardware
    accelerators where texture space is limited.

    * Paletted textures allow easy reuse of texture data for images
    which require many similar but slightly different colored objects.
    Consider a driving simulation with heavy traffic on the road.  Many of
    the cars will be similar but with different color schemes.  If
    full-color textures are used a separate texture would be needed for each
    color scheme, while paletted textures allow the same basic index data to
    be reused for each car, with a different palette to change the final
    colors.

    * Paletted textures also allow use of all the palette tricks
    developed for paletted displays.  Simple animation can be done, along
    with strobing, glowing and other palette-cycling effects.  All of these
    techniques can enhance the visual richness of a scene with very little
    data.

New Procedures and Functions

    void ColorTableEXT(
	enum target,
	enum internalFormat,
	sizei width,
	enum format,
	enum type,
	const void *data);

    void ColorSubTableEXT(
	enum target,
	sizei start,
	sizei count,
	enum format,
	enum type,
	const void *data);

    void GetColorTableEXT(
	enum target,
	enum format,
	enum type,
	void *data);

    void GetColorTableParameterivEXT(
	enum target,
	enum pname,
	int *params);

    void GetColorTableParameterfvEXT(
	enum target,
	enum pname,
	float *params);

New Tokens

    Accepted by the internalformat parameter of TexImage1D, TexImage2D and
    TexImage3DEXT:
	COLOR_INDEX1_EXT		0x80E2
	COLOR_INDEX2_EXT		0x80E3
	COLOR_INDEX4_EXT		0x80E4
	COLOR_INDEX8_EXT		0x80E5
	COLOR_INDEX12_EXT		0x80E6
	COLOR_INDEX16_EXT		0x80E7

    Accepted by the pname parameter of GetColorTableParameterivEXT and
    GetColorTableParameterfvEXT:
	COLOR_TABLE_FORMAT_EXT		0x80D8
	COLOR_TABLE_WIDTH_EXT		0x80D9
	COLOR_TABLE_RED_SIZE_EXT	0x80DA
	COLOR_TABLE_GREEN_SIZE_EXT	0x80DB
	COLOR_TABLE_BLUE_SIZE_EXT	0x80DC
	COLOR_TABLE_ALPHA_SIZE_EXT	0x80DD
	COLOR_TABLE_LUMINANCE_SIZE_EXT	0x80DE
	COLOR_TABLE_INTENSITY_SIZE_EXT	0x80DF

    Accepted by the value parameter of GetTexLevelParameter{if}v:
	TEXTURE_INDEX_SIZE_EXT		0x80ED

Additions to Chapter 2 of the GL Specification (OpenGL Operation)

None

Additions to Chapter 3 of the GL Specification (Rasterization)

  Section 3.6.4, 'Pixel Transfer Operations,' subsection 'Color Index
  Lookup,' 

    Point two is modified from 'The groups will be loaded as an
    image into texture memory' to 'The groups will be loaded as an image
    into texture memory and the internalformat parameter is not one of the
    color index formats from table 3.8.'

  Section 3.8, 'Texturing,' subsection 'Texture Image Specification' is
  modified as follows:

    The portion of the first paragraph discussing interpretation of format,
    type and data is split from the portion discussing target, width and
    height.  The target, width and height section now ends with the sentence
    'Arguments width and height specify the image's width and height.'
    
    The format, type and data section is moved under a subheader 'Direct
    Color Texture Formats' and begins with 'If internalformat is not one of
    the color index formats from table 3.8,' and continues with the existing
    text through the internalformat discussion.

    After that section, a new section 'Paletted Texture Formats' has the
    text:
      If format is given as COLOR_INDEX then the image data is
      composed of integer values representing indices into a table of colors
      rather than colors themselves.  If internalformat is given as one of the
      color index formats from table 3.8 then the texture will be stored
      internally as indices rather than undergoing index-to-RGBA mapping as
      would previously have occurred.  In this case the only valid values for
      type are BYTE, UNSIGNED_BYTE, SHORT, UNSIGNED_SHORT, INT and
      UNSIGNED_INT.

      The image data is unpacked from memory exactly as for a
      DrawPixels command with format of COLOR_INDEX for a context in color
      index mode.  The data is then stored in an internal format derived from
      internalformat.  In this case the only legal values of internalformat
      are COLOR_INDEX1_EXT, COLOR_INDEX2_EXT, COLOR_INDEX4_EXT,
      COLOR_INDEX8_EXT, COLOR_INDEX12_EXT and COLOR_INDEX16_EXT and the
      internal component resolution is picked according to the index
      resolution specified by internalformat.  Any excess precision in the
      data is silently truncated to fit in the internal component precision.
  
      An application can determine whether a particular
      implementation supports a particular paletted format (or any paletted
      formats at all) by attempting to use the paletted format with a proxy
      target.  TEXTURE_INDEX_SIZE_EXT will be zero if the implementation
      cannot support the texture as given.

      An application can determine an implementation's desired
      format for a particular paletted texture by making a TexImage call with
      COLOR_INDEX as the internalformat, in which case target must be a proxy
      target.  After the call the application can query
      TEXTURE_INTERNAL_FORMAT to determine what internal format the
      implementation suggests for the texture image parameters.
      TEXTURE_INDEX_SIZE_EXT can be queried after such a call to determine the
      suggested index resolution numerically.  The index resolution suggested
      by the implementation does not have to be as large as the input data
      precision.  The resolution may also be zero if the implementation is
      unable to support any paletted format for the given texture image.
    
    Table 3.8  should be augmented with a column titled 'Index bits.'  All
    existing formats have zero index bits.  The following formats are added
    with zeroes in all existing columns:
		Name				Index bits
		COLOR_INDEX1_EXT		1
		COLOR_INDEX2_EXT		2
		COLOR_INDEX4_EXT		4
		COLOR_INDEX8_EXT		8
		COLOR_INDEX12_EXT		12
		COLOR_INDEX16_EXT		16

    At the end of the discussion of level the following text should be
    added:

      All mipmapping levels share the same palette.  If levels
      are created with different precision indices then their internal formats
      will not match and the texture will be inconsistent, as discussed above.
    
    In the discussion of internalformat for CopyTexImage{12}D, at end of the
    sentence specifying that 1, 2, 3 and 4 are illegal there should also be
    a mention that paletted internalformat values are illegal.
    
    At the end of the width, height, format, type and data section under
    TexSubImage there should be an additional sentence:

      If the target texture has an color index internal format
      then format may only be COLOR_INDEX.

    At the end of the first paragraph describing TexSubImage and
    CopyTexSubImage the following sentence should be added:

      If the target of a CopyTexSubImage is a paletted texture
      image then INVALID_OPERATION is returned.

    After the Alternate Image Specification Commands section, a new 'Palette
    Specification Commands' section should be added.

      Paletted textures require palette information to
      translate indices into full colors.  The command
	void ColorTableEXT(enum target, enum internalformat, sizei width, 
		enum format, enum type, const void *data);
      is used to specify the format and size of the palette
      for paletted textures.  target specifies which texture is to have its
      palette changed and may be one of TEXTURE_1D, TEXTURE_2D,
      PROXY_TEXTURE_1D, PROXY_TEXTURE_2D, TEXTURE_3D_EXT or
      PROXY_TEXTURE_3D_EXT.  internalformat specifies the desired format and
      resolution of the palette when in its internal form.  internalformat can
      be any of the non-index values legal for TexImage internalformat
      although implementations are not required to support palettes of all
      possible formats.  width controls the size of the palette and must be a
      power of two greater than or equal to one.  format and type specify the
      number of components and type of the data given by data.  format can be
      any of the formats legal for DrawPixels although implementations are not
      required to support all possible formats.  type can be any of the types
      legal for DrawPixels except GL_BITMAP.

      Data is taken from memory and converted just as if each
      palette entry were a single pixel of a 1D texture.  Pixel unpacking and
      transfer modes apply just as with texture data.  After unpacking and
      conversion the data is translated into a internal format that matches
      the given format as closely as possible.  An implementation does not,
      however, have a responsibility to support more than one precision for
      the base formats.

      If the palette's width is greater than than the range of
      the color indices in the texture data then some of the palettes entries
      will be unused.  If the palette's width is less than the range of the
      color indices in the texture data then the most-significant bits of the
      texture data are ignored and only the appropriate number of bits of the
      index are used when accessing the palette.

      Specifying a proxy target causes the proxy texture's
      palette to be resized and its parameters set but no data is transferred
      or accessed.  If an implementation cannot handle the palette data given
      in the call then the color table width and component resolutions are set
      to zero.

      Portions of the current palette can be replaced with
	void ColorSubTableEXT(enum target, sizei start, sizei count, 
		enum format, enum type, const void *data);
      target can be any of the non-proxy values legal for
      ColorTableEXT.  start and count control which entries of the palette are
      changed out of the range allowed by the internal format used for the
      palette indices.  count is silently clamped so that all modified entries
      all within the legal range.  format and type can be any of the values
      legal for ColorTableEXT.  The data is treated as a 1D texture just as in
      ColorTableEXT.

    In the 'Texture State and Proxy State' section the sentence fragment
    beginning 'six integer values describing the resolutions...' should be
    changed to refer to seven integer values, with the seventh being the
    index resolution.

    Palette data should be added in as a third category of texture state.

    After the discussion of properties, the following should be added:

      Next there is the texture palette.  All textures have a
      palette, even if their internal format is not color index.  A texture's
      palette is initially one RGBA element with all four components set to
      1.0.

    The sentence mentioning that proxies do not have image data or
    properties should be extended with 'or palettes.'

    The sentence beginning 'If the texture array is too large' describing
    the effects of proxy failure should change to read:

      If the implementation is unable to handle the texture
      image data the proxy width, height, border width and component
      resolutions are set to zero.  This situation can occur when the texture
      array is too large or an unsupported paletted format was requested.

Additions to Chapter 4 of the GL Specification (Per-Fragment Operations
and the Framebuffer)

None

Additions to Chapter 5 of the GL Specification (Special Functions)

None

Additions to Chapter 6 of the GL Specification (State and State
Requests)

    In the section on GetTexImage, the sentence saying 'The components are
    assigned among R, G, B and A according to' should be changed to be

      If the internal format of the texture is not a color
      index format then the components are assigned among R, G, B, and A
      according to Table 6.1.  Specifying COLOR_INDEX for format in this case
      will generate the error INVALID_ENUM.  If the internal format of the
      texture is color index then the components are handled in one of two
      ways depending on the value of format.  If format is not COLOR_INDEX,
      the texture's indices are passed through the texture's palette and the
      resulting components are assigned among R, G, B, and A according to
      Table 6.1.  If format is COLOR_INDEX then the data is treated as single
      components and the palette indices are returned.  Components are taken
      starting...

    Following the GetTexImage section there should be a new section:

      GetColorTableEXT is used to get the current texture
      palette.
	void GetColorTableEXT(enum target, enum format, enum type, void *data);

      GetColorTableEXT retrieves the texture palette of the
      texture given by target.  target can be any of the non-proxy targets
      valid for ColorTableEXT.  format and type are interpreted just as for
      ColorTableEXT.  All textures have a palette by default so
      GetColorTableEXT will always be able to return data even if the internal
      format of the texture is not a color index format.

      Palette parameters can be retrieved using
	void GetColorTableParameterivEXT(enum target, enum pname, int *params);
	void GetColorTableParameterfvEXT(enum target, enum pname, float *params);
      target specifies the texture being queried and pname
      controls which parameter value is returned.  Data is returned in the
      memory pointed to by params.

      Querying COLOR_TABLE_FORMAT_EXT returns the internal
      format requested by the most recent ColorTableEXT call or the default.
      COLOR_TABLE_WIDTH_EXT returns the width of the current palette.
      COLOR_TABLE_RED_SIZE_EXT, COLOR_TABLE_GREEN_SIZE_EXT,
      COLOR_TABLE_BLUE_SIZE_EXT and COLOR_TABLE_ALPHA_SIZE_EXT return the
      actual size of the components used to store the palette data internally,
      not the size requested when the palette was defined.

    Table 6.11, "Texture Objects" should have a line appended for
    TEXTURE_INDEX_SIZE_EXT:

    TEXTURE_INDEX_SIZE_EXT	n x Z+	GetTexLevelParameter 0	xD texture image i's index resolution	3.8	-


Revision History

Original draft, revision 0.5, December 20, 1995 (drewb) Created

Minor revisions and clarifications, revision 0.6, January 2, 1996 (drewb)
    Replaced all request-for-comment blocks with final text
    based on implementation.

Minor revisions and clarifications, revision 0.7, Feburary 5, 1996 (drewb)
    Specified the state of the palette color information
    when existing data is replaced by new data.

    Clarified behavior of TexPalette on inconsistent textures.

Major changes due to ARB review, revision 0.8, March 1, 1996 (drewb)
    Switched from using TexPaletteEXT and GetTexPaletteEXT
    to using SGI's ColorTableEXT routines.  Added ColorSubTableEXT so
    equivalent functionality is available.

    Allowed proxies in all targets.

    Changed PALETTE?_EXT values to COLOR_INDEX?_EXT.  Added
    support for one and two bit palettes.  Removed PALETTE_INDEX_EXT in
    favor of COLOR_INDEX.

    Decoupled palette size from texture data type.  Palette
    size is controlled only by ColorTableEXT.

Changes due to ARB review, revision 1.0, May 23, 1997 (drewb)
    Mentioned texture3D.

    Defined TEXTURE_INDEX_SIZE_EXT.

    Allowed implementations to return an index size of zero to indicate 
    no support for a particular format.

    Allowed usage of GL_COLOR_INDEX as a generic format in
    proxy queries for determining an optimal index size for a particular
    texture.

    Disallowed CopyTexImage and CopyTexSubImage to paletted
    formats.

    Deleted mention of index transfer operations during GetTexImage with 
    paletted formats.
