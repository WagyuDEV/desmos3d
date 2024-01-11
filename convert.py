import stl
from stl import mesh

your_mesh = mesh.Mesh.from_file('input.stl')
your_mesh.save('output.stl',mode=stl.Mode.ASCII)
