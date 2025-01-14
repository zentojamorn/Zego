XXX - Not complete yet!!!

Name

    EXT_cull_vertex

Name Strings

    GL_EXT_cull_vertex

Version

    $Date: 1997/07/22 21:00:40 $ $Revision: 1.1 $

Number

    98

Dependencies

    None

Overview

    This extension introduces a method for culling vertexes in object
    space based on the value of the dot product between the normal at
    the vertex and a culling eye direction.

    Culling a polygon by examining its vertexes in object space can be
    more efficient than screen space polygon culling since the transformation
    to screen space (which may include a division by w) can be avoided for
    culled vertexes.  Also, vertex culling can be computed before vertexes
    are assembled into primitives.  This is a useful property when drawing
    meshes with shared vertexes, since a vertex can be culled once, and the
    resulting state can be used for all primitives which share the vertex.

Issues

    * Should FrontFace affect the comparison of the dot product?
      It may be useful.  For non-local eye positions it is easy for
      the application to flip the eye direction in order to cull
      either front or back faces.  This doesn't work as well for
      local eye positions.  We'll defer this for now; it is easy
      to add as an extension later.

    * Could determine the eye position/direction in object space
      by transforming the vector (0, 0, 1, 0) by the inverse of
      the composite of the modelview and projection transformations.
      Seems better to have the application provide the eye position/direction
      than to have OpenGL pick one arbitrarily.

New Procedures and Functions

    void CullParameterfvEXT (enum pname, float *params)
    void CullParameterdvEXT (enum pname, double *params)

New Tokens

   Accepted by the <cap> parameter of Enable, Disable, and
   IsEnabled, and by the <pname> parameter of GetBooleanv,
   GetIntegerv, GetFloatv, and GetDoublev:

       CULL_VERTEX_EXT

   Accepted by the <pname> parameter of CullParameterfvEXT,
   CullParameterdvEXT, GetBooleanv, GetIntegerv, GetFloatv, and
   GetDoublev:

       CULL_VERTEX_EYE_POSITION_EXT
       CULL_VERTEX_OBJECT_POSITION_EXT

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

   Before the discussion of Clipping, add a description of 
   vertex culling.

   Vertex Culling

   Vertex culling may be used to eliminate vertexes which are
   part of back facing primitives.  Vertex culling is enabled
   or disabled by using the Enable or Disable commands with
   the symbolic constant CULL_VERTEX_EXT.

   When vertex culling is enabled, vertexes are classified as
   front or back facing according to the sign of the dot
   product between the normal at the vertex and an eye direction
   vector from the vertex toward the eye position.  When
   (normal dot eye_direction) <= 0 the vertex is classified as
   back facing.  When (normal dot eye_direction) > 0 the vertex
   is classified as front facing.  Vertexes are culled when the
   face orientation determined by the dot product is the same
   as the face specified by CullFace.  When all of the vertexes
   of a polygon are culled, then the polygon is culled.

   The eye direction used for vertex culling is determined
   by the culling eye position.  The culling eye position
   is homogeneous (like a light position).  When the w component
   of the position is non-zero, the position is local and the
   eye direction at each vertex is computed by subtracting
   the vertex position from the eye position.  When the w
   component of the position is zero, the position is non-local
   and the is used as the eye direction for all vertexes.

   The culling eye position is specified by the CullParameter
   command.  Positions specified when <pname> is
   CULL_VERTEX_EYE_POSITION_EXT are in eye space and are
   transformed by the inverse of the current MODELVIEW
   transformation.  Positions specified when <pname> is
   CULL_VERTEX_OBJECT_POSITION_EXT are in object space and are
   used directly.

   Vertex culling is performed independently of face culling.
   Polygons on the silhouettes of objects may have both front
   and back facing vertexes.  Since polygons are culled only
   when all of their vertexes are culled, face culling may have
   to be used in addition to vertex culling in order to correctly
   cull silhouette polygons.

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

    INVALID_ENUM if <pname> parameter to CullParameterfvEXT or
    CullParameterdvEXT is not CULL_VERTEX_EYE_POSITION_EXT, or
    CULL_VERTEX_OBJECT_POSITION_EXT.

    INVALID_OPERATION if CullParameterfvEXT or CullParameterdvEXT called
    between execution of Begin and the corresponding execution of End.

New State

								Initial
    Get Value				Get Command	Type	Value		Attrib
    ---------				-----------	----	-------		------

    CULL_VERTEX_EXT			IsEnabled	B	False		transform/enable
    CULL_VERTEX_OBJECT_POSITION_EXT	GetFloatv	P	(0,0,1,0)	transform
    CULL_VERTEX_EYE_POSITION_EXT	GetFloatv	P	(0,0,1,0)	transform

New Implementation Dependent State

    None
