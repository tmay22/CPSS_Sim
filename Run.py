import Setup
import Graph


def main():

    global personList_glob
    global edgeList_glob

    print("")
    setupOption= input("Choose Setup Option: \n 1. Default \n 2. Small (10 pers) \n...etc \n")
    
    

    print("You Selected " + setupOption)
    
    setupOutput = Setup.build(setupOption)

    personList_glob = setupOutput[0]
    edgeList_glob = setupOutput[1]

    exportChoice= input("Would you like to export to graph? (Y/N) \n")
    if "Y" in exportChoice or "y" in exportChoice:
        #writtenFile = Graph.exportVNAGraph(personList_glob, edgeList_glob)
        writtenFile = Graph.exportGexfGraph(personList_glob, edgeList_glob)
    
    print("hello")
if __name__ == "__main__":
    main()