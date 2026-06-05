# Note d'architecture - Gestionnaire de tâches

## 1. Contexte
* **Objectif métier :** L'application est une solution de gestion de tâches (API et interface) permettant aux utilisateurs de créer, suivre l'avancement et archiver leurs missions au quotidien. Elle centralise les statuts et les échéances pour optimiser la productivité de l'équipe ou de l'individu.
* **Contraintes :** Développement réalisé par une équipe de 5 personnes avec des délais restreints. L'environnement cible est limité à une exécution locale reproductible via Docker Compose.

## 2. Vue des services
| Service | Rôle | Image / stack | Port |
| :--- | :--- | :--- | :--- |
| **Frontend** | Interface utilisateur (UI) | `node:20-alpine` (React) | 3000 |
| **API** | Logique métier et requêtes | `python:3.12-slim` (FastAPI) | 8000 |
| **DB** | Persistance des données | `postgres:15-alpine` | 5432 |

## 3. Flux principaux
* **Flux Applicatif :** Le Client web accède au Frontend (port 3000), qui communique en HTTP (REST) avec l'API (port 8000). L'API lit et écrit les données de manière persistante sur la Base de Données (TCP:5432) au sein du réseau privé virtuel `task-network`.
* **Flux CI/CD :** Le développeur pousse son code sur la branche `main`. GitHub Actions intercepte le push, exécute les tests, construit l'image de l'API et la pousse sur le GitHub Container Registry (GHCR).

## 4. Choix d'orchestration
* **Docker Compose :** Ce choix garantit un environnement local parfaitement reproductible pour tous les développeurs et valide les dépendances de démarrage (ex: `depends_on: service_healthy` pour la base de données). Kubernetes a été identifié mais exclu du périmètre final pour se concentrer sur la stabilité de la CI/CD.
* **Stratégie de déploiement :** Redéploiement standard avec recréation des conteneurs éphémères (`docker compose up -d`), tout en conservant l'état de la base via un volume Docker nommé.

## 5. CI/CD
* **Outil :** GitHub Actions.
* **Étapes du pipeline :**
    1. **Lint :** Vérification de la syntaxe Python (Flake8).
    2. **Test :** Exécution automatisée avec Pytest en "Fail Fast" (bloque si le lint échoue).
    3. **Build & Push :** Construction de l'image Docker et envoi sur le registre GHCR.
* **Stockage des secrets :** Aucun mot de passe dans le code. Le workflow utilise le token éphémère natif `${{ secrets.GITHUB_TOKEN }}` fourni dynamiquement par GitHub pour s'authentifier sur le registre. Les variables d'environnement locales utilisent un fichier `.env` non versionné.

## 6. Observabilité (aperçu)
* Le monitoring avancé (Grafana/Prometheus) étant hors périmètre, l'observabilité repose sur les logs centralisés du moteur Docker (`docker compose logs`) et sur le healthcheck actif (`pg_isready`) de PostgreSQL qui assure l'état de santé du service de base de données.

## 7. Limites connues
* **Limite 1 (SPOF sur la DB) :** La base de données PostgreSQL est un conteneur unique. S'il tombe en production physique, le service est interrompu. *Piste d'amélioration :* Mettre en place un système de backup automatisé (dump) ou une réplication Master/Slave.
* **Limite 2 (Sécurité des conteneurs) :** Le backend s'exécute avec l'utilisateur "root" par défaut à l'intérieur du conteneur. *Piste d'amélioration :* Créer un utilisateur non-privilégié dédié (ex: `USER appuser`) dans la directive finale du Dockerfile.