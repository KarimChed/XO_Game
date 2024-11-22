class Morpion:
    def __init__(self):
        self.joueurs = {}  # Associe "X" et "O" aux noms des joueurs
        self.joueur_actuel = "X"
        self.grille = None  # La grille sera initialisée à chaque partie

    def initialiser_grille(self):
        # Réinitialise la grille de jeu 3x3
        self.grille = [[" " for _ in range(3)] for _ in range(3)]

    def afficher_grille(self):
        # Affiche une grille alignée et plus compacte
        print("\n   0   1   2")
        for i, ligne in enumerate(self.grille):
            print(f"{i}  {' | '.join(ligne)}")
            if i < 2:
                print("  ---|---|---")

    def verifier_victoire(self):
        # Vérifie les conditions de victoire
        for ligne in self.grille:
            if ligne[0] == ligne[1] == ligne[2] != " ":
                return True
        for col in range(3):
            if self.grille[0][col] == self.grille[1][col] == self.grille[2][col] != " ":
                return True
        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] != " ":
            return True
        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] != " ":
            return True
        return False

    def verifier_egalite(self):
        # Vérifie si tous les emplacements sont remplis sans victoire
        for ligne in self.grille:
            if " " in ligne:
                return False
        return True

    def jouer_coup(self, ligne, colonne):
        # Permet au joueur actuel de jouer un coup
        if self.grille[ligne][colonne] == " ":
            self.grille[ligne][colonne] = self.joueur_actuel
            if self.verifier_victoire():
                self.afficher_grille()
                print(f"Félicitations {self.joueurs[self.joueur_actuel]} ({self.joueur_actuel}) ! Vous avez gagné !")
                return True
            elif self.verifier_egalite():
                self.afficher_grille()
                print("Match nul !")
                return True
            self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"
        else:
            print("Cette case est déjà occupée, choisissez une autre.")
        return False

    def demarrer(self):
        # Saisie des noms des joueurs avec contrôle pour éviter les doublons
        print("Bienvenue au jeu de Morpion !")
        while True:
            joueur_x = input("Entrez le nom du joueur pour 'X' : ").strip()
            joueur_o = input("Entrez le nom du joueur pour 'O' : ").strip()
            if joueur_x.lower() == joueur_o.lower():
                print("Erreur : Les noms des joueurs doivent être différents. Réessayez.")
            else:
                self.joueurs["X"] = joueur_x
                self.joueurs["O"] = joueur_o
                break

        # Boucle pour relancer une nouvelle partie
        while True:
            self.initialiser_grille()
            print("\nNouvelle partie commencée !")
            print("Instructions :")
            print("1. Entrez 'q' à tout moment pour quitter la partie.")
            print("2. Jouez en entrant les coordonnées sous la forme 'ligne,colonne'.")

            # Boucle principale d'une partie
            while True:
                self.afficher_grille()
                try:
                    choix = input(f"{self.joueurs[self.joueur_actuel]} ({self.joueur_actuel}), entrez votre coup (ligne,colonne) ou 'q' pour quitter : ").strip()
                    if choix.lower() == "q":
                        print("Merci d'avoir joué ! À bientôt.")
                        return
                    ligne, colonne = map(int, choix.split(","))
                    if ligne not in range(3) or colonne not in range(3):
                        print("Veuillez entrer des coordonnées valides (0, 1 ou 2).")
                        continue
                    if self.jouer_coup(ligne, colonne):
                        break
                except ValueError:
                    print("Entrée invalide. Veuillez entrer les coordonnées sous la forme 'ligne,colonne'.")

            # Demander si les joueurs veulent rejouer
            rejouer = input("Voulez-vous rejouer ? (o/n) : ").strip().lower()
            if rejouer != "o":
                print("Merci d'avoir joué ! À bientôt.")
                break


# Lancement du jeu
if __name__ == "__main__":
    jeu = Morpion()
    jeu.demarrer()
