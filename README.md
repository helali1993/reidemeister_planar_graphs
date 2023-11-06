# reidemeister_planar_graphs
Preform Reidemeister moves on Signed Planar Graphs
Please read the PDF file "Report" for more details.

# Summary
We present our program dealing with Reidemeister moves on alternating knot di-
agrams and their signed planar graphs. We highlight theorems (1) and (2) as they provide the
basis for our approach. We developed our program to take as input knot diagrams represented as a
Gauss codes, one of them is a reducible knot diagram, the program then derives their signed planar
graphs. It takes the signed planar graph of the unreduced knot diagram, checks if there are any
possible Reidemeister moves, performs them and modify its signed planar graphs. In the end, the
program compares the pairs of signed planar graphs.
Our program was written using Python. We have also utilized external modules and libraries,
two important mentions are “NetworkX” and “pyknotid”. More details are found throughout the
report and also in the References.
The details of the program were shown. We gave an overview the overall structure and algorithm.
We then displayed the different classes and their roles. we also introduced the main script and other
crucial modules. we walked through the process of the construction of the signed planar graphs
and execution Reidemeister moves. We provided detailed examples of such constructions, and in
the appendix(A), we display the different outputs on our knot diagram collection.
The program still has many areas that require development. We highlighted the approach in
our development phase, and showed how our program might face difficulties with anomali6 es such
loops or parallel edges in the signed planar graphs. More tests and different knot diagrams should
be run on the program as validation tests, this would definitely optimize our results and discover
bugs or errors. Also, a major drawback currently is the limit on knot diagrams to have a maximum
of 10 crossings.
We provided insights regarding future work. Firstly, The adaptation of a more general approach
than our trial-and-error methodology should be used. Secondly, utilizing OOP to overcome certain
challenges, we add that OOP is an easy and straightforward solution for the ten crossing drawback.
