## What is this?
The packacke `pynads` binds `nads`, a C++ implementation that computes the number of almosts-d-simplices in a digraph, to python.


### almost-d-simplices
In a nutshell:

Assume you have directed unweighted graph G=(V,E). Then a d-clique are d vertices, where each vertex is directly
connected (in one direction or another) to all others.
A d-simplex is then a (d+1)-clique without any loops.

An almost-d-simplex is then a collection of vertices and edges which miss exactly one edge in order to form a d-simplex.

It is formally described as a triplet (s,s',e), where s,s' are two different (d-1)-simplices which share a common (d-2)-simplex,
together with an edge e that indicates the missing edge necessary to form a d-simplex.

An example:
Three vertices V={0,1,2} have the edges E={(0,1),(0,2)}. Then this is not enough to form a 2-simplex: Either an edge
e=(1,2) or e=(2,1) is missing. Thus, with s=[0,1] and s'=[0,2] we have the two almost-2-simplices (s,s',e) and
(s,s',e').

Furthermore: Any d-simplex gives rise to (d^2+d)/2 almost-d-simplices. That is exactly the number of edges in a
d-simplex.


Some people (e.g. me) find the number of almost-d-simplices in a big graph interesting.


### Performance
This package allows one to calculate this numbers on sparse graphs in a highly efficient manner, thanks to the substantially optimised underlying C++
implementation. 

As an example: The connectome of the "The Neocortical Microcircuit Collaboration Portal" https://bbp.epfl.ch/nmc-portal/welcome consists of ~30k vertices and 8M edges, connected in a nonrandom manner. `pynads` computes the number of almost-di-simplices for all dimensions in less than three minutes on a desktop CPU.

This is notably faster than my previous native-python implementation, which would have computed for a month at least.



TODO: Write paper/doku in LaTex.


## Installation
`pip install pynads` should be enough.

### Compiling C++ code with `-march=native` for higher performance:
Advanced users my generate their own `nads_bind.$PYTHON_VERSION.so` which is probably faster on their own CPU, compared
to the non-optimised module automatically compiled during installation. On my setup this results in ~15% faster code.
```
g++ -march=native -O3 -Wall -Werror --shared -std=c++14 -fPIC `python3 -m pybind11 --includes` src/nads_bindings.cpp -o nads_bind`python3-config --extension-suffix`
```
and push the resulting `nads_bind.$PYTHON_VERSION.so` to `INSTALL_DIR/site-packages/pynads/`


## Usage
With `g` being a (directed) graph without self-loops, run:

```
from pynads import nads
res = nads(g)
```

This results in a list of Integers `res`: Each entry `res[i]` corresponds to the number of almost-(i+2)-simplices found
in the graph `g`. 


## ToDo:
-[ ] Automate build process for architecture optimized library as described above.

-[ ] Write a paper about the algorithm and link it in the documentation

-[ ] Write a few tests or something

