class Table:
    def __init__ (self, ref, matiere, poids, hauteur, longueur, largeur, prix_vente, prix_fab, nbre_table):
        self.ref=ref
        self.matiere=matiere
        self.poids=poids
        self.hauteur=hauteur
        self.largeur=largeur
        self.prix_vente=prix_vente
        self.__prix_fab=prix_fab
        self.__nbre_table=nbre_table
    def get_prix_fab(self):
        return prix_fab
    def affichage(self):
        print("La reference est:",self.ref)
        print("La matiere est:",self.matiere)
        print("La poids de la table est:",self.poids)
        print("La hauteur de la table est:",self.hauteur)
        print("La largeur de la table:",self.largeur)
        print("La prix de la table est:",self.prix_vente)
        print("Le prix de la fabrication de la tanble est:",self.__prix_fab)
        print("La nombre de la table est:", self.__nbre_table)
    def gain(self):
        print("Le gain est :",str(self.__nbre_table*self.prix_vente),"FCFA")
t1=Table("ref1","bois","kg","cm","cm","cm",250,50,25)
t1.affichage()
t1.gain()
