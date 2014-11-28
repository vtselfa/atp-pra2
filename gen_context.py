#!/usr/bin/python
#coding=utf8

# Este script genera ficheros de contexto preparados para usarse con Multi2sim
# a partir de la lista de benchmarks pasada por linea de comandos.

import sys

from bench_suites import spec2006

if len(sys.argv) < 2:
    sys.stderr.write("USO: programa bench [bench]\n")
    sys.exit(1)

# calculix da problemas
if "calculix" in sys.argv[1:]:
	sys.stderr.write("Aviso: No pueden lanzarse múltiples instancias de <calculix> usando el mismo directorio, ya que todas intentan modificar el mismo fichero.\n")


for i, bench in enumerate(sys.argv[1:]):

	# Error si el bench no existe
	if bench not in spec2006:
		sys.stderr.write("\nEl benchmark <" + bench + "> no pertenece a la suite spec2006.\n")
		sys.stderr.write("Estos son los benchmartks disponibles, manquer:\n")
		sys.stderr.write(", ".join(spec2006))
		sys.stderr.write("\n")
		sys.exit(1)

	# Imprimir el fichero de contexts por la salida estándar
	print("\n# " + bench)
	print("[ Context " + str(i) + " ]")
	for option in spec2006[bench]:
		print(option + " = " + spec2006[bench][option])

