


![Calcium bilding regions visualizer](https://github.com/BioinformaticaUNQ/calcio_binding_regions_visualazer-grupo1/blob/master/extras/title.png)

### Introducción
La idea del software es permitir la visualización de regiones conservadas de unión a ligando en estructuras homólogas y la energía de unión a la proteína problema.

#### Diagrama
[link](https://drive.google.com/file/d/1h2ju2dqpvOuVUFev65_zBPxWC4CvQwab/view?usp=sharing)


#### Requisitos
- [Biopython](https://biopython.org/)
- ?

#### Instrucciones

```bash
pip install -r requisitos
```

#### EPICAS DEL PROYECTO
- ***Ingreso estructura PDB***
  - ***Validar estructura***
- ***Busqueda de proteinas homologas***
- ***Alineamiento***
- ***Calculo de energia de union del ión***
- ***Determinar regiones conservadas***
- ***Visualizar***
  - Estructura problema
  - Regiones de calcio
  - Energia union al metal


#### Funcionamiento del sistema:

1. El sistema permite la carga de una estructura proteica a analizar en el formato PDB, para ello se debe seleccionar el archivo pdb de la proteína que se desea analizar. Una vez completado el paso anterior aparecerá en el recuadro lateral derecho la ruta de referencia al archivo.

2. Para chequear que el pdb es valido y hay presencia de calcio se deberá hacer click en el botón ***Check PDB*** que hace dicha validación y habilita los botones que nos permitiran seguir con el analisis.
En el caso que la verificación haya sido exitosa se verá un recuadro verde con la frase “OK: PDB file is correct”.

3. La búsqueda de proteínas homólogas se hace haciendo click en el boton ***“Generate FASTA”*** que genera archivo Fasta que contendrá las homólogas.
Este proceso puede demorar varios minutos.
 
#### Detalles de interfaz

Luego de correr la instancia incial se puede seguir el chequeo y analisis del pdb mediante los siguientes botones:
 
- “Open Graphic” muestra en pantalla el árbol filogenético de las homólogas obtenidas en la consulta Blast. Además generar un archivo newick en el directorio ./temp para poder ser utilizado en un software externo.
 
- “Show alignment” muestra en pantalla la alineación de las homologas obtenidas.
 
- “Generate FoldX Files” despliega una tabla donde se muestran las posiciones en la estructura primaria de la proteína donde se une el calcio con sus respectivas energías.
 
- “Open in PyMol” abre el software con la proteína cargada y coloreando las regiones de unión calcio según la configuración de Angstrom y el color seleccionado.




# Contribuciones:

### Personas que participaron activamente del proyecto:✨

<table>
	<tr>
		<td>
<a href="https://github.com/BioinformaticaUNQ/calcio_binding_regions_visualazer-grupo1/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=BioinformaticaUNQ/calcio_binding_regions_visualazer-grupo1" />
</a>
		</td>
	</tr>
</table>


