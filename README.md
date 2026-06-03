---

[devops-fil-rouge-table2]
Équipe : COUTHOUIS Edgar, ANTIER Guillaume, PHILIBERT Benjamin, GUILLAUME Quentin, LECHAT Noé
Groupe / promo : B3 INFO
Dépôt : https://github.com/lechatn/devops-fil-rouge-table2.git

---

Description du sujet
En 3–5 phrases : que fait l'application ? Qui est l'utilisateur cible ?

Cette application est une API couplée à une base de données, conçue pour simplifier la gestion de tâches au quotidien. Elle permet de créer, de suivre l'avancement, de modifier et d'archiver des missions spécifiques en s'appuyant sur un système de statuts et d'échéances. L'utilisateur cible principal est tout professionnel, étudiant ou équipe de projet cherchant à structurer son flux de travail, optimiser son organisation et gagner en productivité. De plus, grâce à son architecture orientée API, cette solution se destine également aux développeurs qui souhaiteraient l'intégrer facilement comme backend (serveur) pour alimenter une application mobile, un site web ou un tableau de bord sur mesure.

---

Stack technique prévu
| Composant | Choix | Justification (1 phrase) |
| --------- | ----- | -------------------------- |
| Backend / API | Python (FastAPI) | Framework moderne et très performant qui permet de développer rapidement une API avec une documentation (Swagger) générée automatiquement. |
| Base de données | PostgreSQL | Système relationnel reconnu pour sa fiabilité, idéal pour garantir l'intégrité et structurer proprement les données des tâches. |
| Front (optionnel) | React | Bibliothèque JavaScript incontournable pour créer une interface utilisateur moderne, réactive et fluide. |
| Orchestration cible | Docker Compose | L'utilisation des conteneurs garantit que l'application tourne de la même manière partout. |

---

Rôles dans l'équipe
| Membre | Rôle | Responsabilité principale |
| ------ | ---- | ------------------------- |
| Guillaume | Lead Dev | Code applicatif (développement de l'API) |
| Benjamin | Lead Dev | Dockerfile du service (conteneurisation de l'application) |
| Edgar | Lead Ops | Compose, K8s, monitoring, doc déploiement |
| Noé | Lead Qualité / CI | Pipeline, tests, revue sécurité de base |
| Quentin | Lead Doc / Produit | README, note d'archi, post-mortem |

---

Objectifs du fil rouge (3 minimum)

* **Architecture & Conteneurisation (S1-S2) :** Développer l'API de gestion de tâches (FastAPI) connectée à la base de données (PostgreSQL)
* **Automatisation & Qualité (S3) :** Mettre en place un pipeline d'intégration continue (CI) robuste qui exécute les tests, valide le code, puis build et push l'image Docker automatiquement à chaque fusion sur la branche `main`.
* **Orchestration & Déploiement (S4) :** Déployer l'application complète sur un cluster Kubernetes avec des manifests configurés pour assurer la disponibilité du service.
* **Documentation & Bilan (S5) :** Finaliser la note d'architecture détaillée du système et rédiger un post-mortem complet du projet pour valider les choix techniques et l'organisation de l'équipe.

---

Jalons — état d'avancement
| Séance | Livrable | Statut (à cocher) |
| ------ | -------- | ----------------- |
| S1 | README cadrage | ☑ |
| S2 | Dockerfile(s) + DB en container | ☐ |
| S3 | docker-compose + CI vert | ☐ |
| S4 | Manifests K8s appliqués | ☐ |
| S5 | Monitoring + post-mortem | ☐ |
| S6 | Soutenance prête | ☐ |

---

Démarrage local (à compléter au fil des séances)
# À documenter progressivement — pas besoin de tout remplir en S1
git clone https://github.com/lechatn/devops-fil-rouge-table2.git


---

Communication d'équipe
Canal utilisé  :

- Discord (serveur dédié au projet)

---

Participation S1 (optionnel, 2 lignes)
Retour sur le jeu de rôle ou le cas déploiement : une leçon retenue pour le projet.
-> La mise en pratique a mis en évidence l'importance de bien définir les rôles de chacun dès le départ pour éviter de se retrouver dans une situtation critique.