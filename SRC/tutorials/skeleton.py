# -*- python -*-
# $RCSfile: skeleton.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2014/09/27 21:41:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.tutorials import tutorial
TutoringItem = tutorial.TutoringItem
TutorialClass = tutorial.TutorialClass

TutorialClass(
    subject = "Skeleton",
    ordering=2,
    lessons = [
    TutoringItem(
    subject="Introduction",
    comments=

    """This tutorial is designed to give users an overview of how to
    create and modify an OOF2 BOLD(Skeleton).

    As you saw in the BOLD(Simple Example) tutorial, you can't create
    an FE mesh directly from a Microstructure in OOF2.

    You need to first create a BOLD(Skeleton), before you get to the
    FE mesh.  The Skeleton is a lightweight BOLD(geometric)
    representation of its FE mesh counterpart.  The main task in
    creating a Skeleton is adapting it to material boundaries.  """
        
    ),

##        TutoringItem(
##        subject="Why skeleton?",
##        comments=

##        """Let us assume that we don't have skeleton, meaning we only
##        have FE mesh.

##        You spent a considerable amount of time to mesh your
##        microstructure.

##        What if you chose the wrong element type in the beginning?

##        You need to either start over or write a program to correct
##        your mistakes, which will not be so easy.

##        With skeleton, you don't need to go through this kind of
##        hassle.

##        You're always a click away from your FE mesh with customizable
##        element types.

##        Also, compared to FE mesh, skeleton is extremely
##        BOLD(lighter), that is, it is easy to be manipulated.

##        Factoring in a highly intensive computation needed in
##        BOLD(meshing) stage, it is easy to see why we need
##        BOLD(skeleton).

##        Further information on skeleton can be found in the manual.
##        """ ),

##     TutoringItem(
##     subject="Graphics window",
##     comments=
    
##     """Open a graphics window, if none has been opened yet, with
##     the BOLD(Graphics/New) command in the BOLD(Windows) menu.
    
##     """ ),

    TutoringItem(
    subject="Creating a Microstructure from an Image File",
    comments=

    """Get started by creating a Microstructure.

    Locate the file BOLD(small.ppm) within the share/oof2/examples
    directory in your OOF2 installation.

    Open the BOLD(Microstructure) page and click BOLD(New from Image
    File) to create a new microstructure.

    In the file selection dialog box, navigate to
    BOLD(small.ppm).
    
    Click BOLD(OK) to load the Image and create the Microstructure.
    """,

    signal = ("new who", "Microstructure")
    ),
    
    TutoringItem(
    subject="Categorizing Pixels",
    comments=

    """The micrograph features BOLD(eight) distinct colors, each
    corresponding exactly to a microstructural feature.  Since the
    correspondence between colors and features is trivial, we can
    group pixels automatically.

    Open the BOLD(Image) page and click the BOLD(Group) button.

    Go back to the BOLD(Microstructure) page and you will see that
    BOLD(8) pixel groups have been created for the microstructure.
    """ ),

    TutoringItem(
    subject="The Skeleton Page",
    comments=

    """Now, open the BOLD(Skeleton) page, where we will spend most of
    the time in this tutorial.
    
    The page is comprised of three parts.

    The top part contains a BOLD(Skeleton Selector) and administrative
    features.  The BOLD(Skeleton Selector) is the two pull-down menus
    labelled BOLD(Microstructure) and BOLD(Skeleton).  The first lets
    you choose a Microstructure and the second lets you choose a
    Skeleton belonging to that Microstructure.

    The BOLD(Skeleton Status) pane on the left is a display for
    Skeleton summary data such as number of nodes and elements.
    
    The BOLD(Skeleton Modification) pane on the right contains a bunch
    of skeleton modification tools that we will use to adapt a
    Skeleton to the material boundaries in its Microstructure.  """ ),

    TutoringItem(
    subject="Creating a New Skeleton",
    comments=

    """Click BOLD(New...) to create an initial skeleton.
    
    As in other cases, to give a skeleton a user-defined name, check
    the little square box and type in a name of your liking.

    The number of elements in the initial skeleton can be set with the
    parameters, BOLD(x_elements) and BOLD(y_elements).

    You can choose the element shape with the BOLD(skeleton_geometry)
    parameter.

    For this tutorial, just use the default values for the initial
    skeleton: BOLD(x_elements)=4, BOLD(y_elements)=4, and
    BOLD(skeleton_geometry)=QuadSkeleton.

    Click BOLD(OK) to create the Skeleton.
    """,
        
    signal = ("new who", "Skeleton")
    ),

    TutoringItem(
    subject="Heterogeneous Elements",
    comments=
    
    """ Open a BOLD(Graphics) window if you haven't already.  It
    should be showing the skeleton on top of the micrograph.

    For a Skeleton to be a good representation of a Microstructure,
    the BOLD(Elements) in the Skeleton must not cross boundaries
    between different BOLD(pixel types).  Two pixels are defined to
    have the same type if they have the same Material assigned to them
    and if they belong to the same pixel groups.  Since we haven't
    assigned Materials yet, and since we've assigned groups according
    to pixel color, in this tutorial pixel color is synonymous with
    pixel type.

    Except for one BOLD(yellow) element at the top-right corner of the
    skeleton, all the elements are BOLD(heterogeneous), meaning that
    these elements contain pixels of two or more pixel types.

    We want every element to be as homogeneous as possible."""  ),

    TutoringItem(
    subject="Refining Elements",
    comments=

    """Let us subdivide these heterogeneous elements as the first step
    towards making them homogeneous.

    In the BOLD(Skeleton Modification) pane in the BOLD(Skeleton)
    page, set the BOLD(method) pull-down menu to BOLD(Refine).

    Four parameters need to be set.

    The parameter BOLD(targets) determines which elements should be
    refined.  Select BOLD(Heterogeneous Elements) and set its
    BOLD(threshold) to be BOLD(1.0), meaning any heterogeneous
    elements will be refined.  (All elements with a BOLD(homogeneity)
    less than 1.0 will be refined.  The BOLD(homogeneity) is the
    largest fraction of an element's area belonging to a single pixel
    type.)
    
    The second parameter BOLD(criterion) determines whether to accept
    or reject the resulting refinement.  Select BOLD(Unconditional).

    The parameter BOLD(degree) controls the degree of
    subdivision.  It specifies into how many segments each edge of an
    element will be divided.

    Each refinement BOLD(degree) has a parameter BOLD(rule_set) that
    contains two options.  The BOLD(conservative) rule_set preserves
    the topology of the target element. That is, if you refine a
    quadrilateral, you'll get only quadrilaterals, whenever possible.
    The BOLD(liberal) rule_set may mix triangles and quadrilaterals,
    if the mix yields a better result.

    Choose BOLD(Trisection) and BOLD(conservative) for its rule_set.

    Finally, the parameter BOLD(alpha) determines how elements are
    refined when there are two or more possibilities.  When
    BOLD(alpha) is near zero, oof2 chooses the arrangement that
    produces elements with the best shapes.  When BOLD(alpha) is near
    one, it tries to make the elements as homogeneous as possible.
    Set BOLD(alpha) to 0.5.

    Click BOLD(OK) to refine the Skeleton.  """,

    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="The Refined Skeleton",
    comments=

    """ The refined skeleton should be displayed in the graphics
    window.

    Every element (except one in the top-right corner) has been
    divided into 9 elements.  As a result, a larger fraction of the
    Microstructure's area is covered by homogeneous elements.

    At the bottom of the BOLD(Skeleton Status) pane in the
    BOLD(Skeleton) page, there is a BOLD(Homogeneity Index).  This
    number indicates the homogeneity of the entire skeleton.

    As the skeleton becomes more homogeneous and adapts to material
    boundaries, the Homogeneity Index gets closer to BOLD(1).

    Click BOLD(Undo) and BOLD(Redo), while checking out Homogeneity
    Index.

    The number has been increased from BOLD(0.7305) to BOLD(0.8726).
    """ ),
    
    TutoringItem(
    subject="Another Refinement",
    comments=
    
    """We're still one more BOLD(Refine) away from being satisfied.

    This time, leave BOLD(targets) set to BOLD(Heterogeneous Elements)
    and set BOLD(threshold) to BOLD(0.9), so that only elements less
    than 90% homogeneous will be refined.

    Click BOLD(OK) to start refining.  """,
        
    signal = "Skeleton modified",
    ),

    TutoringItem(
    subject="No More Refinements!",
    comments=

    """The Skeleton looks okay -- no material boundary is very far
    from an element boundary -- but the element boundaries don't
    really coincide with the material boundaries.  More work is
    necessary.

    At this point, more refinements may not yield a favorable result.

    You don't want to refine a skeleton to the point where it
    inevitably inherits the jagged pixel boundaries of the micrograph.

    Thus, we need a different approach to resolve issues with the
    elements near the material boundaries.  """ ),

    TutoringItem(
    subject="Moving Nodes to Material Boundaries",
    comments=

    """While BOLD(refinement) is more of a chop-and-hope-for-the-best
    approach to the heterogeneity issue, the BOLD(node motion) tools
    deal with the issue directly.

    OOF2 provides three different methods of moving nodes in adapting
    to material boundaries -- BOLD(Snap Nodes), BOLD(Anneal), and
    BOLD(Move Nodes).

    BOLD(Snap Nodes) first looks for boundary points -- intersections
    between material boundaries and element edges -- and moves nodes
    to the corresponding points, if the result is favorable.

    BOLD(Anneal), on the other hand, moves nodes to randomly chosen
    points and accepts only the ones that are beneficial.

    The BOLD(Move Nodes) toolbox in the BOLD(Graphics) window allows
    you to move nodes manually.  """ ),
      
    TutoringItem(
    subject="Snapping Nodes",
    comments=

    """Select the BOLD(Snap Nodes) method in the BOLD(Skeleton
    Modification) pane in the BOLD(Skeleton) page.

    This tool will move nodes of target elements to the material
    boundary points along the edges of the elements.

    Select BOLD(Heterogeneous Elements) for the BOLD(targets)
    parameter and set the BOLD(threshold) to be BOLD(0.9), meaning it
    will attempt to move nodes of elements with homogeneity less than
    BOLD(0.9).  """ ),

    TutoringItem(
    subject="Snapping Nodes -- continued",
    comments=
    
    """For the BOLD(criterion) parameter, select BOLD(Average Energy)
    and set its parameter BOLD(alpha) to be BOLD(1).

    The quality of a Skeleton element is quantified by a functional,
    E, which is called an "energy" because of its role in the Skeleton
    annealing process.  E ranges from 0 for good elements to 1 for bad
    elements.  There are two contributions to E: a shape energy, which
    is minimized for squares and equilateral triangles; and a
    homogeneity energy, which is minimized for completely homogeneous
    elements.  The parameter BOLD(alpha) governs the relative weight
    of these two terms.  BOLD(alpha)=0 gives all the weight to the
    shape energy, while BOLD(alpha)=1 ignores shape and emphasizes
    homogeneity.

    By setting BOLD(alpha)=1, we've told the BOLD(Snap Nodes) tool
    that it's ok if moving a node creates badly shaped elements, as
    long as doing so makes them more homogeneous. (We'll fix the bad
    shapes next.)

    Click BOLD(OK) to make changes.  The BOLD(Homogeneity Index)
    increases from 0.957 to 0.989.""",
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Rationalizing Elements",
    comments=

    """ Because BOLD(Snap Nodes) considered only homogeneity, some
    elements have been badly distorted while adapting themselves to
    the material boundaries.
    
    Select the BOLD(Skeleton Modification) method to
    BOLD(Rationalize).

    This modification tool automatically removes badly shaped
    elements, provided the changes meet a certain criterion.

    Set BOLD(targets) to BOLD(All Elements).

    Set BOLD(criterion) to BOLD(Average Energy) and set BOLD(alpha) to
    BOLD(0.8).  With this setting, the BOLD(Rationalize) tool will
    only make changes that lower the average energy E of the affected
    elements.  BOLD(alpha) determines how E is computed.

    For the BOLD(method) parameter, select BOLD(Specified).

    Three rationalization techniques are listed.  Move the mouse
    pointer over each technique to get more information about it.
    Make sure all three are selected and click BOLD(OK), while keeping
    the default values for their parameters.

    The summary for the modification is displayed in the BOLD(OOF
    Messages) window.  Also, in the graphics window, you will notice
    that many of the badly shaped elements are gone.  """,

    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="The Skeleton Selection Page",
    comments=

    """ Open the BOLD(Skeleton Selection) page in the main OOF2
    window.  This page provides tools for selecting Skeleton
    components -- elements, segments, and nodes -- and for
    manipulating groups of them.

    Set BOLD(Selection Mode) to BOLD(Elements).

    From the BOLD(Element Selection Operations) pane in the right side
    of the page, select BOLD(Select By Homogeneity) for the parameter
    BOLD(Action) and set its BOLD(threshold) to be BOLD(0.9), to
    select all elements less than 90% homogeneous.

    We will apply the next modification only to the selected elements.
        
    Now, click BOLD(OK) to make a selection.""",

    signal = "changed element selection"
    ),
      
    TutoringItem(
    subject="Splitting Quadrilaterals",
    comments=

    """Return to the BOLD(Skeleton) page and select BOLD(Split Quads)
    for the modification method.  This tool splits target
    quadrilaterals into two triangles.  A split is accepted only if it
    meets a specified criterion.

    Select BOLD(Selected Elements) for the parameter BOLD(targets).

    Set BOLD(criterion) to be BOLD(Average Energy) with
    BOLD(alpha)=BOLD(0.9).

    A quadrilateral element can be split along either of its two
    diagonals.  The BOLD(split_how) parameter determines how OOF2
    decides which diagonal to choose.  BOLD(Geographic) examines the
    element's neighbors to see if it's likely that there's a material
    boundary crossing the target element on a diagonal.
    BOLD(TrialAndError) splits a quadrilateral along the both
    diagonals and chooses the better of the two.  Set BOLD(split_how)
    to BOLD(Geographic).
        
    Click BOLD(OK) to modify the skeleton.""",
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Rationalizing, again",
    comments=

    """A handful of quadrilaterals have been split, but some badly
    shaped triangles were generated.

    Select BOLD(Rationalize) and apply it to the Skeleton with the
    same settings as before.  """,
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Skeleton Selection",
    comments=

    """Go back to the BOLD(Skeleton Selection) page and again select
    elements by homogeneity with the threshold set to BOLD(0.9).

    Notice the reduced number of selected elements.
    """,

    signal = "changed element selection"
    ),
    
    TutoringItem(
    subject="Annealing",
    comments=

    """Return to the BOLD(Skeleton) page and select BOLD(Anneal) for
    the modification method.  BOLD(Anneal) moves nodes BOLD(randomly)
    and accepts or rejects the new positions according to the given
    criterion.  On each iteration, BOLD(Anneal) attempts to move each
    node once, but it chooses the nodes in a random order.

    Select BOLD(Selected Elements) for its BOLD(targets), meaning it
    will attempt to move nodes of the selected elements only.

    For BOLD(criterion), select BOLD(Average Energy) with BOLD(alpha)
    of BOLD(0.9).

    Set BOLD(T) to be BOLD(0.0) and also set BOLD(delta) to be
    BOLD(1.0).  Move the mouse over these parameters to get more
    information.
    
    For BOLD(iteration), select BOLD(Conditional Iteration), which
    stops annealing when certain conditions are met.  Set
    BOLD(condition) to BOLD(Acceptance Rate), and set the
    BOLD(acceptanceRate) parameter to BOLD(7).  This will terminate
    the annealing procedure if it starts accepting fewer than 7% of
    the attempted moves.

    Set BOLD(extra) to BOLD(3), to require that the BOLD(condition) be
    satisfied for three consecutive iterations before actually
    terminating the procedure.

    Leave BOLD(maximum) set to BOLD(100), setting an absolute limit on
    the number of iterations.
        
    Click BOLD(OK).

    Watch the BOLD(Message) and BOLD(Graphics) windows to monitor the
    progress.""",
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Rationalizing ...",
    comments=

    """If you recall, we set BOLD(alpha) to BOLD(0.9) during the
    anneal.  This put a strong emphasis on homogeneity, thus many
    elements may have been distorted severely.

    Select BOLD(Rationalize) for the modification method and click
    BOLD(OK).  """,
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Reduced No. of Heterogeneous Elements",
    comments=
    
    """Open the BOLD(Skeleton Selection) page and select elements by
    homogeneity with BOLD(threshold) = BOLD(0.9).

    You will notice that the number of elements selected is
    significantly reduced.  """,
        
    signal = "changed element selection"
    ),
    
    TutoringItem(
    subject="Annealing Again",
    comments=
    
    """Return to BOLD(Skeleton) page and do the BOLD(Anneal) one more
    time with the same settings as before.  """,

    signal = "Skeleton modified"
    ),
    
    TutoringItem(
    subject="Rationalizing ...",
    comments=

    """Again, we need to BOLD(Rationalize) the skeleton before we move
    on to the next step.

    Use the same settings as before.  """,
        
    signal = "Skeleton modified"
    ),        

    TutoringItem(
    subject="Almost Done",
    comments=

    """Open the BOLD(Skeleton Selection) page and select elements by
    homogeneity with the BOLD(threshold) being BOLD(0.9).

    There should be very few elements selected.  (Because of
    randomness in some modification methods, your results may vary.)

    Set the BOLD(threshold) to be BOLD(0.8) and click BOLD(OK).

    There should be very few elements selected, meaning that most of the
    elements have been adapted to the material boundaries
    successfully.""",
        
    signal = "changed element selection"
    ),        
    
    TutoringItem(
    subject="Skeleton Quality Control",
    comments=

    """Move back to the BOLD(Skeleton) page and check the
    BOLD(Homogeneity Index).

    It should be almost BOLD(1), which implies the skeleton is nearly
    homogeneous.

    We'll now turn our attention to elements' quality, more precisely,
    their shape.

    The tools for improving the skeleton's quality include BOLD(Swap
    Edges), BOLD(Merge Triangles), and BOLD(Smooth).

    These tools, however, can potentially affect material boundaries
    that have been established already.  Thus, we need to be extra
    careful not to disturb the existing boundaries.  The best way to
    avoid this potentially sorry situation is to pin down all the
    nodes along the boundaries.

    The next slide will teach you how to do this.  """ ),

    TutoringItem(
    subject="Pinning Nodes",
    comments=
    
    """Go to the BOLD(Pin Nodes) page.

    In the pull-down menu labelled BOLD(Method), Select BOLD(Pin
    Internal Boundary Nodes). Click BOLD(OK).

    All the nodes along the boundaries should be selected and
    displayed as BOLD(yellow) dots.

    These nodes are not going to move at all, until they are unpinned.
    """,
        
    signal = "new pinned nodes"
    ),
    
    TutoringItem(
    subject="Swapping edges",
    comments=

    """Go back to the BOLD(Skeleton) page in the OOF2 main window and
    select BOLD(Swap Edges) for the modification method.  This takes
    any two neighboring elements and reorients their shared edge.

    A swapped edge is accepted only when it meets a certain
    criterion.

    Select BOLD(All Elements) for BOLD(targets).

    Select BOLD(Average Energy) for BOLD(criterion).

    Set BOLD(alpha) to BOLD(0.5), putting equal emphasis on shape and
    homogeneity.

    Click BOLD(OK) to swap edges.

    Try BOLD(Undo)-BOLD(Redo) to see the changes wrought by the edge
    swap.

    Also, it is a good idea to BOLD(Rationalize) the skeleton to remove
    potential bad elements created by the swap.  """,
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Merging Triangles",
    comments=
    
    """In addition to BOLD(Swap Edges), you can merge two neighboring
    triangles into a quadrilateral.

    Select BOLD(Merge Triangles) for the modification method.

    Select BOLD(All Elements) for BOLD(targets) and select
    BOLD(Limited Unconditional) for BOLD(criterion).

    Set BOLD(alpha) to BOLD(0.5), BOLD(homogeneity) to BOLD(0.9), and
    BOLD(shape_energy) to BOLD(0.4).

    By doing this, you're accepting any changes, unless they produce
    elements for which the homogeneity drops below the specified value
    or the shape energy goes above the specified value.
    
    Click BOLD(OK) to merge triangles.

    Again, use BOLD(Undo)-BOLD(Redo) to see the changes better.  """,
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Smoothing the Skeleton",
    comments=

    """We're going to give the skeleton finishing touches by applying
    BOLD(Smooth).  BOLD(Smooth) works much like BOLD(Anneal), except
    that instead of picking node positions randomly, it moves each
    node to the average position of its neighbors.

    Select BOLD(Smooth) for the modification method.

    Select BOLD(All Nodes) for BOLD(targets).

    Select BOLD(Limited Unconditional) for BOLD(criterion) and set its
    parameters BOLD(alpha) to BOLD(0.5), BOLD(homogeneity) to
    BOLD(0.9), and BOLD(shape_energy) to BOLD(0.4).

    Select BOLD(Fixed Iterations) for BOLD(iteration).  Set the number
    of BOLD(iterations) to 5.

    Click BOLD(OK).

    Updates are reported in the same way as in BOLD(Anneal).  """,
        
    signal = "Skeleton modified"
    ),

    TutoringItem(
    subject="Saving a Skeleton",
    comments=

    """ The BOLD(Save/Skeleton) command in the BOLD(File) menu in the
    main OOF2 window, and the BOLD(Save) button on the BOLD(Skeleton)
    page both allow you to save Skeletons to a file.

    The BOLD(format) parameter in the file selector dialog box was
    discussed in the BOLD(Microstructure) tutorial.

    When you save a Skeleton, its Microstructure is saved with it in
    the data file.  Loading the data file with the BOLD(Load/Data) or
    BOLD(Load/Script) commands from the BOLD(File) menu restores both
    the Microstructure and the Skeleton.  """ ),

    TutoringItem(
    subject="Homework",
    comments=
    
    """You must like what you see in the graphics window.  Anyway, we
    have covered most of the issues related to Skeleton modifications.
    
    Related topics not covered in this tutorial include BOLD(Active
    Areas), and the BOLD(Move Node) toolbox.  """ )
      
    ])
