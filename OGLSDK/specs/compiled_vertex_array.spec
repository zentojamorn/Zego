XXX - Not complete yet!!!

Name

    EXT_compiled_vertex_array

Name Strings

    GL_EXT_compiled_vertex_array

Version

    $Date: 1997/07/22 21:00:37 $ $Revision: 1.1 $

Number

    97

Dependencies

    None

Overview

    This extension defines an interface which allows static vertex array
    data to be cached or pre-compiled for more efficient rendering.  This
    is useful for implementations which can cache the transformed results
    of array data for reuse by several DrawArrays, ArrayElement, or
    DrawElements commands.  It is also useful for implementations which
    can transfer array data to fast memory for more efficient processing.

    For example, rendering an M by N mesh of quadrilaterals can be
    accomplished by setting up vertex arrays containing all of the
    vertexes in the mesh and issuing M DrawElements commands each of
    which operate on 2 * N vertexes.  Each DrawElements command after
    the first will share N vertexes with the preceding DrawElements
    command.  If the vertex array data is locked while the DrawElements
    commands are executed, then OpenGL may be able to transform each
    of these shared vertexes just once.

Issues

    * Is compiled_vertex_array the right name for this extension?

    * Should there be an implementation defined maximum number of array
      elements which can be locked at a time (i.e. MAX_LOCKED_ARRAY_SIZE)?

      Probably not, the lock request can always be ignored with no resulting
      change in functionality if there are insufficent resources, and allowing
      the GL to define this limit can make things difficult for applications.
    
    * Should there be any restrictions on what state can be changed while
      the vertex array data is locked?

      Probably not.  The GL can check for state changes and invalidate
      any cached vertex state that may be affected.  This is likely to
      cause a performance hit, so the preferred use will be to not change
      state while the vertex array data is locked.
    
New Procedures and Functions

    void LockArraysEXT (int first, sizei count)
    void UnlockArraysEXT (void)

New Tokens

    Accepted by the <pname> parameter of GetBooleanv, GetIntegerv,
    GetFloatv, and GetDoublev:

	ARRAY_ELEMENT_LOCK_FIRST_EXT
	ARRAY_ELEMENT_LOCK_COUNT_EXT

Additions to Chapter 2 of the 1.1 Specification (OpenGL Operation)

   After the discussion of InterleavedArrays, add a description of
   array compiling/locking.

   The currently enabled vertex arrays can be locked with the command
   LockArraysEXT.  When the vertex arrays are locked, the GL
   can compile the array data or the transformed results of array
   data associated with the currently enabled vertex arrays.  The
   vertex arrays are unlocked by the command UnlockArraysEXT.

   Between LockArraysEXT and UnlockArraysEXT the application
   should ensure that none of the array data in the range of
   elements specified by <first> and <count> are changed.
   Changes to the array data between the execution of LockArraysEXT
   and UnlockArraysEXT commands may affect calls may affect DrawArrays,
   ArrayElement, or DrawElements commands in non-sequential ways.

   While using a compiled vertex array, references to array elements
   by the commands DrawArrays, ArrayElement, or DrawElements which are
   outside of the range specified by <first> and <count> are undefined.

Additions to Chapter 3 of the 1.1 Specification (Rasterization)

    None

Additions to Chapter 4 of the 1.1 Specification (Per-Fragment Operations
and the Frame Buffer)

    None

Additions to Chapter 5 of the 1.1 Specification (Special Functions)

    LockArraysEXT and UnlockArraysEXT are not complied into display lists
    but are executed immediately.

Additions to Chapter 6 of the 1.1 Specification (State and State Requests)

    None

Additions to the GLX Specification

    XXX - Not complete yet!!!

GLX Protocol

    XXX - Not complete yet!!!

Errors

    INVALID_VALUE is generated if LockArrarysEXT parameter <first> is less
    than zero.

    INVALID_VALUE is generated if LockArraysEXT parameter <count> is less than
    or equal to zero.

    INVALID_OPERATION is generated if LockArraysEXT is called between execution
    of LockArraysEXT and corresponding execution of UnlockArraysEXT.

    INVALID_OPERATION is generated if UnlockArraysEXT is called without a
    corresponding previous execution of LockArraysEXT.

    INVALID_OPERATION is generated if LockArraysEXT or UnlockArraysEXT is called
    between execution of Begin and the corresponding execution of End.

New State
								Initial
    Get Value				Get Command	Type	Value	Attrib
    ---------				-----------	----	-------	------

    ARRAY_ELEMENT_LOCK_FIRST_EXT	GetIntegerv	Z+	0	client-vertex-array
    ARRAY_ELEMENT_LOCK_COUNT_EXT	GetIntegerv	Z+	0	client-vertex-array

New Implementation Dependent State

    None
