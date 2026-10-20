# Miftah al-Huruf — édition finale 1.0.0

## Fonctionnalités finalisées
- Lecteur hors connexion des trois corpus embarqués.
- Navigation page par page, favoris et historique.
- Calculateur Abjad Maghrébi selon la table définie, pivot fixe 2049.
- Normalisation arabe optionnelle et option shadda ×2.
- Décomposition lettre par lettre, charges élémentaires et trois contrôles de cohérence.
- Sélection directe d'un passage depuis l'OCR disponible de La Bourdah.
- Saisie manuelle de passages pour les scans dont l'image source reste la référence.
- Recherche plein texte dans l'index textuel effectivement embarqué.
- Rapport Master Expert en six sections.
- Calcul astronomique déterministe à partir de date, heure, latitude, longitude et UTC offset.
- Export/copie du rapport et export/import des données locales.
- Assistant source-grounded et adaptateur IA optionnel compatible avec un endpoint de type Chat Completions.
- Inventaire des sources et consultation du document technique.
- PWA hors ligne et configuration Capacitor Android.

## Fidélité documentaire
Les scans Idrīsiyya et Barhout sont conservés comme images sources. Aucune transcription, translittération, traduction ou attribution absente du corpus n'est fabriquée. L'OCR est traité comme une aide lorsqu'il existe et doit être vérifié visuellement avant un calcul exact.

Le corpus coranique n'est pas inclus dans les sources embarquées. Le Master Expert ne fabrique donc pas de verset coranique « idéal ».

## Compilation Android
La compilation finale nécessite Android Studio/SDK + Gradle sur la machine de build :

```bash
npm install
npx cap add android
npx cap sync android
npx cap open android
```

Puis produire l'APK depuis Android Studio (Build > Generate Signed Bundle / APK) ou via Gradle dans le dossier `android`.

Le code source est finalisé ; l'APK binaire n'est pas généré ici car l'environnement de travail ne possède pas le SDK Android/Gradle nécessaire.
