import matplotlib.pyplot as plt
import numpy as np

def draw_faces(G):
	facia=make_graph.make_facia(G)
	
	triangle_block_text_lines=["beginShape();"]
	for s in facia:
		for v in s:
			triangle_block_text_lines.append("vertex(%sx[t],%sy[t],%sz[t]);" %(v,v,v))
		triangle_block_text_lines.append("endShape(CLOSE);")
	
	triangle_block="\n".join(triangle_block_text_lines)
	
	d=open(str(N)+"_edges.js",'w')
	d.write(triangle_block)
	d.close()



def draw_graph(G):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	node_xyz = np.array([G.nodes[v]['pos'] for v in sorted(G)])
	edge_xyz = np.array([
		(
			G.nodes[u]['pos'],
			G.nodes[v]['pos']
		) for u, v in G.edges()
	])

	ax.scatter(*node_xyz.T, s=100, ec="w")

	for vizedge in edge_xyz:
		ax.plot(*vizedge.T, color="tab:gray")
	
	def _format_axes(ax):
		"""Visualization options for the 3D axes."""
		# Turn gridlines off
		ax.grid(False)
		# Suppress tick labels
		for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
			dim.set_ticks([])
		# Set axes labels
		ax.set_xlabel("x")
		ax.set_ylabel("y")
		ax.set_zlabel("z")
	
	_format_axes(ax)
	fig.tight_layout()
	plt.show()



	
	
	