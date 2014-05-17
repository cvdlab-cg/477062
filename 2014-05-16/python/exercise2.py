'''***********************HOMEWORK3:Esercizio2*********************************'''
"""importo di librerie"""
from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/baljinderjit/Desktop/GraficaComputazionaleProgetti/lar-cc/lib/py')
from larcc import *
from sysml import *
from exercise1 import *
'''***********************************************************'''
########################################
'''deinizioni'''
Dom1D = INTERVALS(1)(24)
Bezier = BEZIER(S1)

#######################################################################
'''----colori------'''
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]
'''***********************************************************'''
'''***********************************************************'''
coloreStrada = rgb([50,50,50])
colorePalazzo = rgb([179,119,85])
colorePavimento = rgb([98,51,24])
colorePalazzoVicino1 = rgb([223,222,189])
colorePalazzoVicino2 = rgb([190,167,196])
colorePalazzoVicino3 = rgb([140,140,140])
colorePalazzoVicino4 = rgb([152,242,224])
colorePalazzoVicino5 = rgb([200,240,150])
colorePalazzoVicino6 = rgb([236,150,142])
coloreTerra = rgb([140,140,140])

'''***********************************************************'''



#VIEW(STRUCT(MKPOLS(master)))
appartamento = STRUCT(MKPOLS(master))

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
master = assemblyDiagramInit([5,5,9])([[.2,4,.2,4,.2],[0.2,4,0.2,2,.2],[0.5,4,.2,4,.2,4,.2,4,.2]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)
########################################################################################
#elimino il volume ai volumi in particolare lascio solo pareti e una stanza piena
toRemove = [55,145]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

toMerge = 55
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  
#VIEW(STRUCT([hpc,cell]))    
master = diagram2cell(diagram,master,toMerge)   
#VIEW(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
'''finestra1 piano0'''
toMerge = 46
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra
diagram = assemblyDiagramInit([3,1,3])([[1,1,1],[.2],[2.5,3,3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la aprete tra cucine e bagno ed elimino i volumi del bagno e cucina
toRemove = [231]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

'''porta piano0'''
toMerge = 133
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la porta
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio porta principale
toRemove = [236]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

'''porta tra soggiorno e camera'''
toMerge = 97
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la porta
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio porta principale
toRemove = [242]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
##########################tolgo la parete tra cucine e bagno
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

'''finestra1'''

#seleziono la cella  per fare la finestra1
toMerge = 204
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono le misure della finestra2 dalla cella
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella della finestra1
toRemove = [60]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#####################################################
'''finestra2'''
toMerge = 201
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra2
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la aprete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [256]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


toMerge = 156
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra
diagram = assemblyDiagramInit([3,1,1])([[1,.1,3],[.2],[1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [261,113,259]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 146
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
diagram = assemblyDiagramInit([3,1,2])([[.6,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimino la cella per fare le porta tra salone e bagno
toRemove = [260]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [258]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
'''fine piano 0'''
'''---------------fine piano1---------------'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [139,54,155,71]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
'''finestra1piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 47
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra2
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[1,1.5,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la aprete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [261]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################

'''finestra2piano1 sopra alla porta piano0'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 128
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la finestra2
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[1,1.5,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [268]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
'''piano1 interno porta bagno1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 142
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la porta
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[0,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [275]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
#####################################################
'''piano2 interno camere'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 94
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [282]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
'''finestra bagno piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [236]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
#####################################################
'''finestra soggiorno piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 174
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [288]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
'''finestra cucina piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 12
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [295]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
#####################################################
'''porta ingresso piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 155
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [300]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
'''finestra  piano1'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 76
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[.5,.5,1],[.2],[2,2,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [306]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################

'''porta  parte centrale'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 59
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [311]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
#####################################################
'''fine piano1'''
'''-------------inizio piano2---------------------'''
'''elimino volume camere'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [53,132,146,68]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

'''finestra camera piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 47
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[1,1.5,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [313]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################
'''finestra camera piano2-2finestre attaccate'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 122
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([6,1,3])([[1,1,1,1,1,1],[.2],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#elimio la parete tra cucine e baglio ed elimino i volumi del bagno e cucina
toRemove = [320,326]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################

########################################
'''finestra camera piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 13
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [335]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################
'''finestra bagno piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 180
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [342]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################

'''finestra bagno piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 181
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1,.5,.5],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [349]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################

'''finestra soggiorno piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 164
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [356]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################

'''finestra soggiorno piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 165
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [363]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################


'''ingresso pinao2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 147
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [368]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################
'''ingresso piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 148
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,2])([[.5,.5,1],[.2],[2.5,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [372]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################
########################################
'''doppie finestre  piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 74
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([6,1,3])([[1,1,1,1,1,1],[.2],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [378,387]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################

########################################
'''finestra piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toMerge = 72
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[1,1,1],[.2],[2.5,3,3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [393]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################


########################################
'''tolgo volume camere piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [139,66,126,52]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
########################################
'''finestra camera piano3-2finestre attaccate'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 118
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([6,1,3])([[1,1,1,1,1,1],[.2],[1,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [396,402]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################
'''finestra camera piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 47
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[1,1.5,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [411]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################
###########################
'''finestra camera piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 14
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[1,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [418]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################


###########################
'''inizo interni piano 2 camera'''
'''ingresso tra soggiorno e camera'''

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 82
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [425]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################
###########################
'''ingresso tra soggiorno e camera'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 83
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[.2],[1.5,.5,.5],[0,2.5,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [432]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################
###########################
'''ingresso tra soggiorno e bagno piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 123
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[0,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [436]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################

'''ingresso tra bagno e cucina piano2'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 97
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[1],[1,.5,1],[0,1,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [446]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################

###########################

'''ingresso tra cucina e bagno piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 98
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([1,3,3])([[1],[1,.5,1],[0,1,2]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [453]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################

'''ingresso tra soggiorno e bagno piano3'''
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toMerge = 122
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))
#dimensiono sulla cella la camera
diagram = assemblyDiagramInit([3,1,3])([[1,.5,1],[.2],[0,2,1]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)
toRemove = [460]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)
###########################
'''***************************************fine palazzo************************************'''
'''*********************modello di una macchina con Bezier****************'''
############Bezier#############

############baseSotto-Bezier#############
base0 = [[2,0, 4.03], [3.26,0, 4.03], [4.04,0,4.02], [5.01,0, 3.99]]
base0 = MAP(Bezier(base0))(Dom1D)
#####baseSottoAngolinoDestroSottoRuotaDietro-Bezier#########
angolinoRuotaDietro = [[5.01,0, 3.99], [5.07,0, 4.1], [4.96,0, 4.03], [5.16,0, 4.04]]
angolinoRuotaDietro = MAP(Bezier(angolinoRuotaDietro))(Dom1D)
#####RuotaDietro-Bezier#########
ruotaDietro = [[5.97,0, 4.08], [5.79,0, 3.73], [5.2,0, 3.83], [5.16,0, 4.04]]
ruotaDietro = MAP(Bezier(ruotaDietro))(Dom1D)
#####baseDietroRuota-Bezier#########
base1 = [[5.97,0, 4.08], [6.17,0, 4.08], [6.31,0,4.12], [6.54,0, 4.19]]
base1 = MAP(Bezier(base1))(Dom1D)
#####altezzaDietroDaSotto-Bezier####
altezza0 = [[6.33,0, 5.06], [6.4,0, 4.81], [6.55,0, 4.64], [6.54,0, 4.19]]
altezza0 = MAP(Bezier(altezza0))(Dom1D)
#####angolinoDietro1-Bezier#########
altezza1 = [[6.23,0, 5.07], [6.28,0, 5.05], [6.28,0, 5.06], [6.33,0, 5.06]]
altezza1 = MAP(Bezier(altezza1))(Dom1D)
#####angolinoDietro2-Bezier#########
altezza2 = [[6.21, 0,5.15], [6.15,0, 5.04], [6.26,0, 5.14], [6.23,0,5.07]]
altezza2 = MAP(Bezier(altezza2))(Dom1D)
#####angolinoDietro3-Bezier#########
altezza3 = [[6.21,0, 5.15], [6.31,0, 5.11], [6.42,0, 5.07], [6.49,0, 5.23]]
altezza3 = MAP(Bezier(altezza3))(Dom1D)
#####AngolinoAltoDietro-Bezier#########
alto0 = [[6.12,0, 5.23], [6.28,0, 5.28], [6.42,0,5.23], [6.49,0, 5.23]]
alto0 = MAP(Bezier(alto0))(Dom1D)
################################################################################
vista1 = STRUCT([base0,angolinoRuotaDietro,ruotaDietro,base1,altezza0,altezza1,
	altezza2,altezza3,alto0])
################################################################################
#####altoTettoDietro-Bezier#########
alto1 = [[6.12,0, 5.23], [5.9,0, 5.06], [5.89,0, 5.23], [5.41,0, 5.23]]
alto1 = MAP(Bezier(alto1))(Dom1D)
#####altoTettoDietro-Bezier#########
alto2 = [[4.31,0, 5.31], [4.54,0, 5.3], [4.94,0, 5.21], [5.41,0, 5.23]]
alto2 = MAP(Bezier(alto2))(Dom1D)
#####altoTettoCentro-Bezier#########
alto3 = [[4.31,0, 5.31], [3.99,0, 5.3], [4.1,0, 5.65], [2.72,0, 5.54]]
alto3 = MAP(Bezier(alto3))(Dom1D)
#####altoTettoAvantiSpecchio-Bezier#########
alto4 = [[1.83,0, 5.15], [2.1,0, 5.26], [2.2,0, 5.34], [2.72,0, 5.54]]
alto4 = MAP(Bezier(alto4))(Dom1D)
#####altoSpecchietto-Bezier#########
alto5 = [[1.83,0, 5.15], [1.85,0, 5.37], [1.74,0, 5.31], [1.6,0, 5.21]]
alto5 = MAP(Bezier(alto5))(Dom1D)
#####altoSpecchietto-Bezier#########
specchietto0 = [[1.7,0, 5.13], [1.68,0, 5.11], [1.63,0, 5.16], [1.6,0, 5.21]]
specchietto0 = MAP(Bezier(specchietto0))(Dom1D)
#####altoSpecchietto1-Bezier#########
specchietto1 = [[0.89,0, 4.81], [1.32,0, 5.15], [1.66,0, 4.94], [1.7,0, 5.13]]
specchietto1 = MAP(Bezier(specchietto1))(Dom1D)
################################################################################
vista2 = STRUCT([vista1,alto1,alto2,alto3,alto4,alto5,specchietto0,specchietto1])
################################################################################
#####davantiFaroCofano-Bezier#########
avanti0 = [[0.89,0, 4.81], [0.74,0, 4.77], [0.84,0, 4.85], [0.7,0, 4.73]]
avanti0 = MAP(Bezier(avanti0))(Dom1D)
#####davantifaroSottoCofano-Bezier#########
avanti1 = [[0.16,0, 4.33], [0.31,0, 4.49], [0.58,0, 4.63], [0.7,0, 4.73]]
avanti1 = MAP(Bezier(avanti1))(Dom1D)
#####davantiSotto-Bezier#########
avanti2 = [[0.16,0, 4.33], [0.24,0, 4.33], [0.25,0, 4.22], [0.31,0, 4.14]]
avanti2 = MAP(Bezier(avanti2))(Dom1D)
#####basePrimaDellaRuotaSx-Bezier#########
base1 = [[1.03,0, 3.99], [0.09,0, 3.98], [0.04,0, 4.11], [0.31,0, 4.14]]
base1 = MAP(Bezier(base1))(Dom1D)
#####basePrimaDellaRuotaSx-Bezier#########
base2 = [[1.03,0, 3.99], [1.13,0, 4.13], [1.14,0, 3.98], [1.25,0, 3.92]]
base2 = MAP(Bezier(base2))(Dom1D)
#####ruotaDavanti-Bezier#########
ruotaAvanti = [[1.91,0, 4.06], [1.71,0, 3.75], [1.35,0, 3.84], [1.25,0, 3.92]]
ruotaAvanti = MAP(Bezier(ruotaAvanti))(Dom1D)
#####pezzetoDietroRuotaAvanti-Bezier#########
base3 = [[1.91,0, 4.06], [2,0, 4], [2,0, 4], [2,0, 4.03]]
base3 = MAP(Bezier(base3))(Dom1D)
################################################################################
vistalaterale = STRUCT([vista2,avanti0,avanti1,avanti2,base1,base2,ruotaAvanti,base3])
vistalaterale = T(3)(-4)(vistalaterale)
################################################################################
##############################################
'''inizia la vista dall alto'''
##############################################
Al0 = [[0,2.28,3.6], [0,1.39,3.77], [0,0.72,3.47], [0,0.5,3.32]]
Al0 = MAP(Bezier(Al0))(Dom1D)
##############################################
Al1 = [[0,0.23,2.16], [0,0.36,2.7], [0,0.25,2.83], [0,0.5,3.32]]
Al1 = MAP(Bezier(Al1))(Dom1D)
##############################################
Al2 = [[0,0.23,2.16], [0,0.01,1.94], [0,0.34,1.92], [0,0.24,1.75]]
Al2 = MAP(Bezier(Al2))(Dom1D)
##############################################
Al3 = [[0,0.49,0.71], [0,0.34,0.93], [0,0.3,1.57], [0,0.24,1.75]]
Al3 = MAP(Bezier(Al3))(Dom1D)
##############################################
Al4 = [[0,0.49,0.71], [0,1.01,0.41], [0,1.72,0.33], [0,2.29,0.44]]
Al4 = MAP(Bezier(Al4))(Dom1D)
##############################################
Al5 = [[0,2.49,0.5], [0,2.5,0.4], [0,2.51,0.16], [0,2.29,0.44]]
Al5 = MAP(Bezier(Al5))(Dom1D)
##############################################
Al6 = [[0,2.49,0.5], [0,3.97, 1.03], [0,5.42, 0.15], [0,6.08, 0.88]]
Al6 = MAP(Bezier(Al6))(Dom1D)
##############################################
Al7 = [[0,6.34,0.91], [0,6.29,0.93], [0,6.26,0.86], [0,6.08,0.88]]
Al7 = COLOR(RED)(MAP(Bezier(Al7))(Dom1D))
##############################################
Al8 = [[0,6.34,0.91], [0,6.37,1.61], [0,6.4,2.67], [0,6.33,3.14]]
Al8 = MAP(Bezier(Al8))(Dom1D)
##############################################
Al9 = [[0,6.06,3.16], [0,6.17,3.17], [0,6.26,3.16], [0,6.33,3.14]]
Al9 = MAP(Bezier(Al9))(Dom1D)
##############################################
Al10 = [[0,6.06,3.16], [0,5.58,3.88], [0,3.89,3.01], [0,2.46,3.56]]
Al10 = MAP(Bezier(Al10))(Dom1D)
##############################################
Al11 = [[0,2.28,3.6], [0,2.44,3.83], [0,2.56,3.73], [0,2.46,3.56]]
Al11 = MAP(Bezier(Al11))(Dom1D)
##############################################
'''interni'''
##############################################
Al12 = [[0,2.07,2.51], [0,2.61,3.18], [0,2.63,3.1], [0,3.62,2.69]]
Al12 = MAP(Bezier(Al12))(Dom1D)
##############################################
Al13 = [[0,2.07,2.51], [0,1.61,1.83], [0,2.38,0.83], [0,3.03,1.11]]
Al13 = MAP(Bezier(Al13))(Dom1D)
##############################################
Al14 = [[0,3.64,1.39], [0,3.58,1.37], [0,3.3,1.25], [0,3.03,1.11]]
Al14 = MAP(Bezier(Al14))(Dom1D)
##############################################
Al15 = [[0,3.64,1.39], [0,3.55,2.03], [0,3.57,2.19], [0,3.62,2.69]]
Al15 = MAP(Bezier(Al15))(Dom1D)
##############################################
Al16 = [[0,4.74,2.59], [0,4.59,2.58], [0,4.5,2.59], [0,3.62,2.69]]
Al16 = MAP(Bezier(Al16))(Dom1D)
##############################################
Al17 = [[0,4.74,2.59], [0,4.92,2.06], [0,4.84,1.71], [0,4.75,1.47]]
Al17 = MAP(Bezier(Al17))(Dom1D)
##############################################
Al18 = [[0,3.64,1.39], [0,3.98,1.42], [0,4.36,1.43], [0,4.75,1.47]]
Al18 = MAP(Bezier(Al18))(Dom1D)
##############################################
Al19 = [[0,6.06,3.16], [0,6.03,2.33], [0,6.04,2.08], [0,6.08,0.88]]
Al19 = MAP(Bezier(Al19))(Dom1D)
##############################################
Al20 = [[0,4.88, 1.54], [0,5.11, 1.58], [0,5.69, 1.87], [0,6.05, 1.88]]
Al20 = MAP(Bezier(Al20))(Dom1D)
##############################################
Al21 = [[0,4.88,1.54], [0,4.9,1.7], [0,4.93,2.04], [0,4.88,2.5]]
Al21 = MAP(Bezier(Al21))(Dom1D)
##############################################
Al22 = [[0,6.045,2.18], [0,5.53,2.22], [0,5.44,2.37], [0,4.88,2.5]]
Al22 = MAP(Bezier(Al22))(Dom1D)
################################################################################
vistaAlto = STRUCT([Al0,Al1,Al2,Al3,Al4,Al5,Al6,Al7,Al8,Al9,Al10,
	Al11,Al12,Al13,Al14,Al15,Al16,Al17,Al18,Al19,Al20,Al21,Al22])
vistaAlto = T(3)(2)(MAP([S2,S3,S1])(vistaAlto))
################################################################################
'''vista frontale'''
##############################################
fronte0 = [[0,9.84,3.85], [0,9.71,3.92], [0,9.42,3.73], [0,9.45,3.96]]
fronte0 = MAP(Bezier(fronte0))(Dom1D)
##############################################
fronte1 = [[0,7.4,3.94], [0,8.86,3.92], [0,8.33,3.91], [0,9.45,3.96]]
fronte1 = MAP(Bezier(fronte1))(Dom1D)
##############################################
fronte2 = [[0,7.4,3.94], [0,7.4,3.8], [0,7.02,3.83], [0,7.01,3.9]]
fronte2 = MAP(Bezier(fronte2))(Dom1D)
##############################################
fronte3 = [[0,7.06,4.95], [0,6.92,4.88], [0,6.99,4.31], [0,7.01,3.9]]
fronte3 = MAP(Bezier(fronte3))(Dom1D)
##############################################
fronte4 = [[0,7.06,4.95], [0,7.11,4.98], [0,7.12,4.98], [0,7.19,5]]
fronte4 = MAP(Bezier(fronte4))(Dom1D)
##############################################
fronte5 = [[0,7.14,5.14], [0,7.17,5.1], [0,7.18,5.06], [0,7.19,5]]
fronte5 = MAP(Bezier(fronte5))(Dom1D)
##############################################
fronte6 = [[0,7.14,5.14], [0,6.84,4.97], [0,6.79,5.4], [0,7.16,5.18]]
fronte6 = MAP(Bezier(fronte6))(Dom1D)
##############################################
fronte7 = [[0,7.21, 5.09], [0,7.18, 5.13], [0,7.2, 5.14], [0,7.16, 5.18]]
fronte7 = MAP(Bezier(fronte7))(Dom1D)
##############################################
fronte8 = [[0,7.21, 5.09], [0,7.29, 5.13], [0,7.51, 5.18], [0,7.59, 5.14]]
fronte8 = MAP(Bezier(fronte8))(Dom1D)
##############################################
fronte9 = [[0,7.81, 5.42], [0,7.73, 5.33], [0,7.61, 5.22], [0,7.59, 5.14]]
fronte9 = MAP(Bezier(fronte9))(Dom1D)
##############################################
fronte10 = [[0,7.81, 5.42], [0,8.52, 5.53], [0,8.66, 5.48], [0,9.02, 5.43]]
fronte10 = MAP(Bezier(fronte10))(Dom1D)
##############################################
fronte11 = [[0,9.6, 5.1], [0,9.13, 5.17], [0,9.33, 5.03], [0,9.02, 5.43]]
fronte11 = MAP(Bezier(fronte11))(Dom1D)
##############################################
fronte12 =[[0,9.6, 5.1], [0,9.64, 5.13], [0,9.64, 5.12], [0,9.69, 5.14]]
fronte12 = MAP(Bezier(fronte12))(Dom1D)
##############################################
fronte13 = [[0,9.94, 5.18], [0,9.93, 5.27], [0,9.65, 5.31], [0,9.69, 5.14]]
fronte13 = MAP(Bezier(fronte13))(Dom1D)
##############################################
fronte14 =[[0,9.94, 5.18], [0,9.8, 4.9], [0,9.66, 5.31], [0,9.65, 5]]
fronte14 = MAP(Bezier(fronte14))(Dom1D)
##############################################
fronte15 = [[0,9.84, 3.85], [0,9.91, 4.69], [0,9.81, 5.03], [0,9.65, 5]]
fronte15 = MAP(Bezier(fronte15))(Dom1D)
##############################################
'''interni vista frontale'''
##############################################
frontInterno0 = [[0,8.96, 5.4], [0,8.6, 5.47], [0,7.99, 5.43], [0,7.87, 5.4]]
frontInterno0 = MAP(Bezier(frontInterno0))(Dom1D)
##############################################
frontInterno1 = [[0,7.93, 4.9], [0,7.29, 4.79], [0,7.74, 5.33], [0,7.87, 5.4]]
frontInterno1 = MAP(Bezier(frontInterno1))(Dom1D)
##############################################
frontInterno2 = [[0,7.93, 4.9], [0,8.62, 5], [0,9.76, 4.62], [0,8.96, 5.4]]
frontInterno2 = MAP(Bezier(frontInterno2))(Dom1D)
##############################################
################################################################################
vistafrontale = STRUCT([fronte0,fronte1,fronte2,fronte3,fronte4,fronte5,
	fronte6,fronte7,fronte8,fronte9,fronte10,fronte11,fronte12,fronte13,
	fronte14,fronte15,frontInterno0,frontInterno1,frontInterno2])
vistafrontale = T([2,3])([-6.5,-4])(vistafrontale)
################################################################################
vistaAltoLateraleFrontale = STRUCT([vistaAlto,T(2)(4)(vistalaterale),
	vistalaterale,vistafrontale])
################################################################################
###########################################
'''vista da dietro'''
####################base#######################
dietro0 = [[0,7.49,1.67], [0,8.03,1.62], [0,8.84,1.64], [0,9.33,1.67]]
dietro0 = MAP(Bezier(dietro0))(Dom1D)
#####################ruotaSx######################
dietro1 = [[0,7.49,1.67], [0,7.47,1.5], [0,7.51,1.46], [0,7.01,1.51]]
dietro1 = MAP(Bezier(dietro1))(Dom1D)
###################altoSx########################
dietro2 = [[0,7.17,2.75], [0,6.88,2.86], [0,6.9,1.35], [0,7.01,1.51]]
dietro2 = MAP(Bezier(dietro2))(Dom1D)
###################specchiettoSx########################
dietro3 = [[0,7.17,2.75], [0,7.07,2.89], [0,7.38,2.91], [0,7.38,2.79]]
dietro3 = MAP(Bezier(dietro3))(Dom1D)
###################AltoSx########################
dietro4 = [[0,7.65,2.79], [0,7.57,2.78], [0,7.45,2.79], [0,7.38,2.79]]
dietro4 = MAP(Bezier(dietro4))(Dom1D)
###################AltoSx########################
dietro5 = [[0,7.65,2.79], [0,7.85,3.03], [0,7.78,3.11], [0,8.18,3.06]]
dietro5 = MAP(Bezier(dietro5))(Dom1D)
###################AltoSx########################
dietro6 = [[0,9.16,2.79], [0,8.85,3.18], [0,8.97,3.08], [0,8.18,3.06]]
dietro6 = MAP(Bezier(dietro6))(Dom1D)
###################AltoSx########################
dietro7 = [[0,9.16,2.79], [0,9.31,2.8], [0,9.38,2.8], [0,9.44,2.78]]
dietro7 = MAP(Bezier(dietro7))(Dom1D)
###################specchiettoDx########################
dietro8 = [[0,9.63,2.76], [0,9.69,2.93], [0,9.38,2.87], [0,9.44,2.78]]
dietro8 = MAP(Bezier(dietro8))(Dom1D)
###################altoDX########################
dietro9 = [[0,9.63,2.76], [0,9.9,2.82], [0,9.88,1.88], [0,9.83,1.62]]
dietro9 = MAP(Bezier(dietro9))(Dom1D)
###################altoDX########################
dietro10 = [[0,9.33,1.67], [0,9.28,1.37], [0,9.92,1.51], [0,9.83,1.62]]
dietro10 = MAP(Bezier(dietro10))(Dom1D)
##############################################
'''interni'''
##############################################
###################specchioAlto########################
dietroInterno0 = [[0,7.92,2.99], [0,7.77,2.68], [0,8.15,2.9], [0,8.88,2.83]]
dietroInterno0 = MAP(Bezier(dietroInterno0))(Dom1D)
###################specchioAlto########################
dietroInterno1 = [[0,7.92,2.99], [0,8.77,3.03], [0,8.99,3.09], [0,8.88,2.83]]
dietroInterno1 = MAP(Bezier(dietroInterno1))(Dom1D)
###################sottoSx########################
dietroInterno2 = [[0,7.3,2.33], [0,7.23,2.46], [0,8.38,2.42], [0,8.21,2.42]]
dietroInterno2 = MAP(Bezier(dietroInterno2))(Dom1D)
###################sottoSx########################
dietroInterno3 = [[0,8.26,2.12], [0,8.18,2.28], [0,8.15,2.32], [0,8.21,2.42]]
dietroInterno3 = MAP(Bezier(dietroInterno3))(Dom1D)
###################sottoSx########################
dietroInterno4 = [[0,8.26,2.12], [0,7.54,2.16], [0,7.28,2.18], [0,7.3,2.33]]
dietroInterno4 = MAP(Bezier(dietroInterno4))(Dom1D)
###################sottoDx########################
dietroInterno4 = [[0,8.26,2.12], [0,7.54,2.16], [0,7.28,2.18], [0,7.3,2.33]]
dietroInterno4 = MAP(Bezier(dietroInterno4))(Dom1D)
###################sottoDx########################
dietroInterno5 = [[0,8.59,2.43], [0,8.62,2.28], [0,8.61,2.18], [0,8.54,2.13]]
dietroInterno5 = MAP(Bezier(dietroInterno5))(Dom1D)
###################sottoDx########################
dietroInterno6 = [[0,9.48,2.25], [0,9.26,2.1], [0,8.7,2.14], [0,8.54,2.13]]
dietroInterno6 = MAP(Bezier(dietroInterno6))(Dom1D)
###################sottoSx########################
dietroInterno7 = [[0,9.48,2.25], [0,9.64,2.38], [0,9.23,2.46], [0,8.59,2.43]]
dietroInterno7 = MAP(Bezier(dietroInterno7))(Dom1D)
###################cerchioInternoCentrale########################
dietroInterno8 = [[0,8.4,2.13], [0,8.24,2.13], [0,8.14,2.38], [0,8.37,2.46]]
dietroInterno8 = MAP(Bezier(dietroInterno8))(Dom1D)
###################cerchioInternoCentrale########################
dietroInterno9 = [[0,8.4,2.13], [0,8.53,2.08], [0,8.73,2.42], [0,8.37,2.46]]
dietroInterno9 = MAP(Bezier(dietroInterno9))(Dom1D)
################################################################################
vistaDaDietro = STRUCT([dietro0,dietro1,dietro2,dietro3,dietro4,dietro5,
	dietro6,dietro7,dietro8,dietro9,dietro10,dietroInterno0,dietroInterno1,
	dietroInterno2,dietroInterno3,dietroInterno4,dietroInterno5,dietroInterno6,
	dietroInterno7,dietroInterno8,dietroInterno9])
vistaDaDietro = T([1,2,3])([6.5,-6.5,-1.62])(vistaDaDietro)
################################################################################
macchina = STRUCT([vistaAltoLateraleFrontale,vistaDaDietro])
macchina = T([1,2,3])([2,-7,.1])(macchina)
macchina1 = T([1,2,3])([10,0,0])(macchina)
macchina2 = T([1,2,3])([-10,0,0])(macchina)


'''***************************************fine macchina************************************'''
appartamento = COLOR(colorePalazzo)(STRUCT(MKPOLS(master)))
vistaCompleta = STRUCT([macchina,macchina1,macchina2,appartamento])
#VIEW(vistaCompleta)
'''***************************************fine macchinaEPalazzo************************************'''
'''***************************************faccio la strada************************************'''
strada = CUBOID([50,8,30])
strada = T([1,2,3])([-20,-8,-30])(strada)
strada = COLOR(coloreStrada)(strada)
stradaPalazzoMacchina = STRUCT([vistaCompleta,strada])
#VIEW(stradaPalazzoMacchina)

'''*************************faccio i modelli dei palazzi vicini con Bezier*******************'''
##############################################
cl0 = [[0.31, 1.51], [0.15, 3.48], [1.19, 2.56], [1.41, 3.23]]
cl0 = MAP(Bezier(cl0))(Dom1D)
##############################################
cl1 =[[0.31, 1.51], [1.32, 0.69], [1.28, 0.95], [2.23, 0.85]]
cl1 = MAP(Bezier(cl1))(Dom1D)
##############################################
cl2 = [[5.26, 0.61], [5.2, 0.21], [4.77, 0.32], [2.23, 0.85]]
cl2 = MAP(Bezier(cl2))(Dom1D)
##############################################
cl3 = [[5.26, 0.61], [4.92, 3.07], [4.53, 3.53], [2.92, 3.04]]
cl3 = MAP(Bezier(cl3))(Dom1D)
##############################################
cl4 = [[1.41, 3.23], [2.1, 3.54], [2.1, 2.96], [2.92, 3.04]]
cl4 = MAP(Bezier(cl4))(Dom1D)

base = STRUCT([cl0,cl1,cl2,cl3,cl4])
base = SOLIDIFY(base)
vicino1 = PROD([base, Q(10)])
vicino1 = T([1,2,3])([15,0,0])(vicino1)
vicino1 = COLOR(colorePalazzoVicino1)(vicino1)
##############vicino2#############
base1 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base1 = SOLIDIFY(base1)
vicino2 = PROD([base1, Q(20)])
vicino2 = T([1,2,3])([-10,0,0])(vicino2)
vicino2 = COLOR(colorePalazzoVicino2)(vicino2)
##############vicino3#############
base2 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base2 = SOLIDIFY(base2)
vicino3 = PROD([base2, Q(50)])
vicino3 = T([1,2,3])([5,15,-30])(vicino3)
vicino3 = COLOR(colorePalazzoVicino3)(vicino3)
'''***************************************fine pavimento************************************'''
'''*************************metto insieme tutto il progetto***************************'''
progetto = STRUCT([stradaPalazzoMacchina,vicino1,vicino2,vicino3])
'''************************base palazzo***************************'''
pavimento = CUBOID([50,10,30])
pavimento = T([1,2,3])([-20,-1,-30])(pavimento)
pavimento = COLOR(coloreTerra)(pavimento)

pavimento2 = CUBOID([50,10,30])
pavimento2 = T([1,2,3])([-20,-18,-30])(pavimento2)
pavimento2 = COLOR(coloreTerra)(pavimento2)
'''************************fine palazzo***************************'''
progetto = STRUCT([progetto,pavimento,pavimento2])
'''************************************************'''
pavimentoprincipale = CUBOID([100,100,1])
pavimentoprincipale = T([1,2,3])([-40,-50,-30])(pavimentoprincipale)
pavimentoprincipale = COLOR(coloreTerra)(pavimentoprincipale)
'''************************************************'''
'''*************************modello palazzo davanti***********************'''

base3 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base3 = SOLIDIFY(base3)
vicino4 = PROD([base3, Q(20)])
vicino4 = T([1,2,3])([-20,-15,.1])(vicino4)
vicino4 = COLOR(colorePalazzoVicino6)(vicino4)


base4 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base4 = SOLIDIFY(base4)
vicino5 = PROD([base4, Q(10)])
vicino5 = T([1,2,3])([-10,-15,.1])(vicino5)
vicino5 = COLOR(colorePalazzoVicino5)(vicino5)

base5 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base5 = SOLIDIFY(base5)
vicino6 = PROD([base5, Q(15)])
vicino6 = T([1,2,3])([-5,-15,.1])(vicino6)
vicino6 = COLOR(colorePalazzoVicino4)(vicino6)

base6 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base6 = SOLIDIFY(base6)
vicino7 = PROD([base6, Q(5)])
vicino7 = T([1,2,3])([5,-15,.1])(vicino7)
vicino7 = COLOR(colorePalazzoVicino5)(vicino7)

base7 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base7 = SOLIDIFY(base7)
vicino8 = PROD([base7, Q(10)])
vicino8 = T([1,2,3])([13,-15,.1])(vicino8)
vicino8 = COLOR(colorePalazzoVicino4)(vicino8)

base8 = STRUCT([cl0,cl1,cl2,cl3,cl4])
base8 = SOLIDIFY(base8)
vicino9 = PROD([base8, Q(20)])
vicino9 = T([1,2,3])([20,-15,.1])(vicino9)
vicino9 = COLOR(colorePalazzoVicino6)(vicino9)
'''************************************************'''
'''************************************************'''
progetto = STRUCT([pavimentoprincipale,progetto,vicino4,vicino5,vicino6,vicino7,vicino8,vicino9])
VIEW(progetto)