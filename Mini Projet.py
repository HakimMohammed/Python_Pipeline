    #---------------------------SAISIR-----------------------------
def saisir():
    choix="O"
    i=1
    while choix=="O":
        print("-----------------------Candidat",i,"---------------------")
        while True:
            NCIN=input("Saisir le NCIN:\n")
            if NCIN.isupper()==True:
                break
        while True:
            NOM=input("Saisir le nom:\n")
            if NOM.isalpha()==True:
                break
        while True:
            PRENOM=input("Saisir le prénom:\n")
            if PRENOM.isalpha()==True:
                break
        while True:
            AGE=input("Saisir l'age:\n")
            if AGE.isdigit()==True:
                break
        while True:
            NOTE=input("Saisir la note:\n")
            if (float(NOTE)>0 and float(NOTE)<20) and (len(NOTE)>=5):
                break
            else:
                print("pour sasir une note inférieur a 10 , écrire à cette forme : '09.25'\n Si le nombre n'a pas de virgule, écrire à cette forme: '10.00' ") 
        while True:
            DECISION=input("Saisir la décision(ajourné--admis--refusé):\n")
            if DECISION=='ajourné' or DECISION=='admis' or DECISION=='refusé' :
                break
        i+=1
        print("--------------------------------------------------")
        ligne=NCIN+"|"+NOM+"|"+PRENOM+"|"+AGE+"|"+NOTE+"|"+DECISION+"\n"
        C=open("concours.txt","a")
        C.write(ligne)
        choix=input("Voulez vous ajouter une autre personne?--OUI(O)--NON(N)\n")
    C.close()


    #---------------------------ADMIS-------------------
def admis():
    A=open("concours.txt","r")
    Ad=open("admis.txt","a")
    for ligne in A:
        L=ligne.split("|")
        if L[5]=="admis\n" :
            Ad.write(ligne)
    A.close()
    Ad.close()
    

    #-------------------ADMIS-------FINALS---------------
def admisFinal():
    Ad=open("admis.txt","r")
    AdF=open("admisFinal.txt","a")
    for ligne in Ad:
        L=ligne.split("|")
        age=int(L[3])
        if L[5]=="admis\n" and age<=30 :
            AdF.write(ligne)
    Ad.close()
    AdF.close()

    
    #---------------------------ATTENTE-----------------------
def attente():
    Ad=open("admis.txt","r")
    Att=open("attente.txt","a")
    for ligne in Ad:
        L=ligne.split("|")
        age=int(L[3])
        if L[5]=="admis\n" and age>30 :
            NCINatt=L[0]
            NOMatt=L[1]
            PRENOMatt=L[2]
            NOTEatt=L[4]
            Donné=NCINatt+"|"+NOMatt+"|"+PRENOMatt+"|"+NOTEatt+"\n"
            Att.write(Donné)
    Ad.close()
    Att.close()


    #-------------------------STATISTIQUES------------------------------------
def statistiques(dec):
    NbAd=0
    NbRe=0
    NbAj=0
    S=open("concours.txt","r")
    for ligne in S:
        L=ligne.split("|")
        if L[5]=="admis\n" :
            NbAd+=1
        elif L[5]=="ajourné\n":
            NbAj+=1
        else:
            NbRe+=1
    NbC=NbAd+NbAj+NbRe
    
    if dec=="admis" :
        PAd=(NbAd/NbC)*100
        print("Le pourcentage des candidats admis est:",PAd,"%")
    elif dec=="ajourné":
        PAj=(NbAj/NbC)*100
        print("Le pourcentage des candidats ajournés est:",PAj,"%")
    else:
        PRe=(NbRe/NbC)*100
        print("Le pourcentage des candidats admis est:",PRe,"%")
    S.close()


    #---------------------------CLASSEMENT---------------------------------

        
def classement():
    CAtt=open("classementAttente.txt","a")
    Att=open("attente.txt","r")
    Notes=[]
    
    #Put all the notes in a list in a decroissant order
    for ligne in Att:
        L=ligne.split("|")
        Notes.append(L[3])
    Notes.sort(reverse=True)
    Att.close()
    Notesv2=[]
    
    #Create a list without occurances
    for element in Notes:
        if element not in Notesv2:
            Notesv2.append(element)

    #Comparaison des notes: if a candidat's note is the same as the element for the list
    #The candidat will be added to the fichier
    for i in range(len(Notesv2)):
        Att=open("attente.txt","r")
        for ligne in Att:
            Cand=ligne.split("|")
            if Notesv2[i]==Cand[3]:
                CAtt.write(ligne)
        Att.close()
    CAtt.close()
    
while True:
    print("----------------------MENU--------------------------")
    Ch=input("--Saisir '1' pour saisir des candidats--\n--Saisir '2' pour classer les candidats admis--\n--Saisir '3' pour classer les candidats admis et ont moins de 30 ans--\n--Saisir '4' pour classer les candidats admis et ont plus de 30 ans--\n--Saisir '5' pour afficher le pourcentage de une decision de votre choix--\n--Saisir '6' pour ordonner les candidats admis et ont plus de 30 ans--\n")
    if Ch=='1':
        saisir()
    elif Ch=='2':
        try:
            admis()
            print("Tache Terminé")
        except (FileNotFoundError, IOError):
            print("Remplis le fichier des candidats")
    elif Ch=='3':
        try:
            admisFinal()
            print("Tache Terminé")
        except (FileNotFoundError, IOError):
            print("Remplis le fichier des admis")
    elif Ch=='4':
        try:
            attente()
            print("Tache Terminé")
        except (FileNotFoundError, IOError):
            print("Remplis le fichier des admis")
    elif Ch=='5':
        try:
            while True:
                Decision=input("Saisir la décision à laquelle vous voulez calculer le pourcentage:\n")
                if Decision=='ajourné' or Decision=='admis' or Decision=='refusé' :
                    break
            statistiques(Decision)
        except (FileNotFoundError, IOError):
            print("Remplis le fichier des candidats")
    elif Ch=='6':
        try:
            classement()
            print("Tache Terminé")
        except (FileNotFoundError, IOError):
            print("Remplis le fichier des attentes")
    else:
        print("Choix invalide")
    print("\n\n----------------------------------------")
    T=input("Pour arréter saisir 'N'\nPour continuer saisir autre chose\n")
    if T=='N':
        print("FIN DU PROGRAMME")
        break
        
    



    
