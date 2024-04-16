from Old_V1_Files.ConfigObjects_V1 import *
from Old_V1_Files.NetworkObjects_V1 import *
import numpy
import random


def exportVNAGraph(personList, edgeList):

    # Clear existing file and open new graph file for editing
    file = open('graphFile.vna', 'w').close()
    file = open('graphFile.vna', 'w+')

    text = "*Node data\n"
    # EXCEPTION
    file.write(text)
    text = "label influenceOpenness nuance interactiveness klout trustingOthers changeThreshold discriminationThreshold\n"
    file.write(text)


    # If you remove 'influence openess' as a variable in the class you must remove it here

    for eachPerson in personList:
        text = ""
        text = f"{eachPerson.key} "
        text = f"{text}{eachPerson.influenceOpenness} "
        text = f"{text}{eachPerson.nuance} "
        text = f"{text}{eachPerson.interactiveness} "
        text = f"{text}{eachPerson.klout} "
        text = f"{text}{eachPerson.trustingOthers} "
        text = f"{text}{eachPerson.changeThreshold} "
        text = f"{text}{eachPerson.discriminationThreshold}\n"
        # Unsure if this will work
        #text = f"{text}{eachPerson.conceptMap}\n "
        file.write(text)
    
    text = "*Tie data\n"
    file.write(text)
    text = "Source Target Weight Similarity Trust LastInteract Key\n"
    file.write(text)
    for eachEdge in edgeList:
        text = ""
        text = f"{eachEdge.connections[0].key} "
        text = f"{text}{eachEdge.connections[1].key} "
        text = f"{text}{round(eachEdge.strength)} "
        text = f"{text}{eachEdge.similarity} "
        text = f"{text}{eachEdge.trust} "
        text = f"{text}{eachEdge.lastInteract} "
        text = f"{text}{eachEdge.key} \n"
        

        file.write(text)
       

    

    file.close()



    print("")



def exportGexfGraph(personList, edgeList):

    # Clear existing file and open new graph file for editing
    file = open('graphFile.gexf', 'w').close()
    file = open('graphFile.gexf', 'w+')

    # Wrote the Gexf Header
    text = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    file.write(text)
    text = "<gexf xmlns=\"http://gexf.net/1.3\" version=\"1.3\">\n"
    file.write(text)
    text = "    <graph mode=\"static\" defaultedgetype=\"directed\">\n"
    file.write(text)
    
    # Build the Node Class Attributes
    
    text = "        <attributes class=\"node\">\n"
    file.write(text)
    text = "            <attribute id=\"0\" title=\"key\" type=\"string\"/>\n"
    file.write(text)
    text = "            <attribute id=\"1\" title=\"nuance\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"2\" title=\"interactiveness\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"3\" title=\"klout\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"4\" title=\"trustingOthers\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"5\" title=\"changeThreshold\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"6\" title=\"discriminationThreshold\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"7\" title=\"influenceOpenness\" type=\"float\"/>\n"
    file.write(text)
    text = "        </attributes>\n"
    file.write(text)

    # Build the Edge Class Attributes
    text = "        <attributes class=\"edge\">\n"
    file.write(text)
    text = "            <attribute id=\"0\" title=\"key\" type=\"string\"/>\n"
    file.write(text)
    text = "            <attribute id=\"1\" title=\"personOne\" type=\"string\"/>\n"
    file.write(text)
    text = "            <attribute id=\"2\" title=\"personTwo\" type=\"string\"/>\n"
    file.write(text)
    text = "            <attribute id=\"3\" title=\"similarity\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"4\" title=\"trust\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"5\" title=\"lastInteract\" type=\"float\"/>\n"
    file.write(text)
    text = "            <attribute id=\"6\" title=\"strength\" type=\"float\"/>\n"
    file.write(text)

    text = "        </attributes>\n"
    file.write(text)

    # Nodes
    text = "        <nodes>\n"
    file.write(text)
    # If you remove 'influence openess' as a variable in the class you must remove it here
    for eachPerson in personList:
        text = f"           <node id=\"{eachPerson.key}\" label=\"{eachPerson.key}\" >\n"
        file.write(text)
        text = f"               <attvalues>\n"
        file.write(text)
        text = f"                   <attvalue for =\"0\" value=\"{eachPerson.key}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"1\" value=\"{eachPerson.nuance}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"2\" value=\"{eachPerson.interactiveness}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"3\" value=\"{eachPerson.klout}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"4\" value=\"{eachPerson.trustingOthers}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"5\" value=\"{eachPerson.changeThreshold}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"6\" value=\"{eachPerson.discriminationThreshold}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"7\" value=\"{eachPerson.influenceOpenness}\" />\n"
        file.write(text)
        text = f"               </attvalues>\n"
        file.write(text)
        text = f"           </node>\n"
        file.write(text)

        # Unsure if this will work
        #text = //add concept map??
    text = "        </nodes>\n"
    file.write(text)

    # Add edges
    
    text = "        <edges>\n"
    file.write(text)

    for eachEdge in edgeList:
        text = f"           <edge source=\"{eachEdge.connections[0].key}\" target=\"{eachEdge.connections[1].key}\" >\n"
        file.write(text)
        text = f"               <attvalues>\n"
        file.write(text)
        text = f"                   <attvalue for =\"0\" value=\"{eachEdge.key}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"1\" value=\"{eachEdge.connections[0].key}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"2\" value=\"{eachEdge.connections[1].key}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"3\" value=\"{eachEdge.similarity}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"4\" value=\"{eachEdge.trust}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"5\" value=\"{eachEdge.lastInteract}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"6\" value=\"{eachEdge.strength}\" />\n"
        file.write(text)
        text = f"                   <attvalue for =\"7\" value=\"{eachPerson.influenceOpenness}\" />\n"
        file.write(text)
        text = f"               </attvalues>\n"
        file.write(text)
        text = f"           </edge>\n"
        file.write(text)
   

       
    text = "        </edges>\n"
    file.write(text)
    text = "    </graph>\n"
    file.write(text)
    text = "</gexf>\n"
    file.write(text)
    

    file.close()



    print("")