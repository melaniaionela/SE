import sys, threading, logging, os
from Queue import Queue
class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})
   
def utilisation():
    #Affichage mode d'utilisation
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """
def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath("__file__")) + os.path.sep
    
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename = working_dir + 'bonjour.log',
                        level=logging.INFO)    
    logging.info("Main start")
    print "start"
    #La boucle principale
    if argv is None:
        argv = sys.argv
        print "rien d'afficher"
    if len(argv) == 1:
        utilisation()
    else:
        #Argument 1 est le nom de fichier avec un noms per ligne
        #mmeThread = []
        #mThread = []
        #mlleThread = []
        qMme = Queue(10)
        qMlle = Queue(10)
        qM = Queue(10)
        myfile =working_dir +""+ argv
        with open(myfile,'r') as f:
            #Dites bonjour a chaque personne de fichier
            for ligne in f:
                if ligne[0:4] == "Mme." : 
                    mme_local = Bonjour(ligne.strip(' \r\n'))
                    qMme.put(mme_local)
                   # mmeThread.append(mme_local)
                elif ligne[0:5] == "Mlle.":
                    mlle_local = Bonjour(ligne.strip(' \r\n'))
                    #mlleThread.append(mlle_local)
                    qMlle.put(mlle_local)
                elif ligne[0:2] == "M.":
                    m_local = Bonjour(ligne.strip(' \r\n'))
                    qM.put(m_local)
                    #mThread.append(m_local)
    while not qMlle.empty():
        qMlle.get().start()
    qMlle.task_done()
    while not qMme.empty():                      
        qMme.get().start()
    qMme.task_done()
    while not qM.empty():
        qM.get().start()
    qM.task_done()  
    print "stop"
    logging.info("Main stop")
    return 

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    myfile = "personnes.txt"   
    #main(myfile)
    try:
        sys.exit(main(myfile)) # => SystemExit
    except SystemExit:
        print("sys.exit() parfait")
    except:
        print("error")
    
