import functions
import networkx as nx

G = functions.graph_network(year = None, all = True)
print(f"Grafo com {G.number_of_edges()} arestas e {G.number_of_nodes()} vértices")
nx.write_gml(G, "grafo_clique.gml")

functions.centralidade_G(G, "Resultados")
functions.comunidades_G(G)
    
HG = functions.hypergraph_network(year = None, all = True)
print(f"Hipergrafo com {HG.number_of_edges()} arestas e {HG.number_of_nodes()} vértices")
   
for x in range(1,4):
    linegraph = HG.get_linegraph(s=x, edges=False)
    print(f"Linegraph com {linegraph.number_of_edges()} arestas e {linegraph.number_of_nodes()} vértices")

    functions.degree_centrality_hg(HG, "Resultados", x)
    functions.centralidade_HG(linegraph, "Resultados", x)

functions.comunidades_HG(HG)
functions.comunidades_eventos()