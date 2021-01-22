#include <stdio.h>
#include <iostream>

#include "../nads/nads.cpp" 

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(nads_bind, m) {
  m.doc() = "Python interface for nads";

  m.def("compute_nads", [](std::vector<value_t>& vertices,
                                 std::vector<std::vector<value_t>>& edges,
                                 bool directed,
                                 int min_dimension,
                                 int max_dimension) {

    // flagser parameters
    flagser_parameters params;
    params.min_dimension = 2;
    params.max_dimension = -1;

    // Building the graph
    auto graph = filtered_directed_graph_t(vertices, directed);
    for (auto& edge : edges) graph.add_edge(edge[0], edge[1]);

    // Running nads count_nads routine
    auto nads = count_nads(graph, params);

    return nads;
  });
}
