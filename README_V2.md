# Miftah al-Huruf — V2

Cette version étend le prototype avec :

- Abjad Maghrébi exclusif et pivot 2049.
- Vérification arithmétique en trois contrôles.
- Historique, favoris, mode clair/sombre.
- Lecteur hors ligne des trois ouvrages.
- OCR arabe local préindexé pour **La Bourdah**.
- Recherche plein texte locale dans l'index OCR de La Bourdah.
- Sélection d'une page OCR et transfert direct vers le calculateur.
- Pour **Les Noms Idrīsiyya** et **Livre Barhout** : arabe original seulement, sans transcription, translittération, turc ni OCR automatique.
- Master Expert en six sections.
- Module astronomique : longitude solaire/signe, âge et phase lunaire, lever/coucher du Soleil, jour gouverneur et heure planétaire à partir de date/heure/latitude/longitude/UTC offset.
- RAG local : récupération des passages indexés et génération d'un prompt strictement source-grounded.
- Adaptateur optionnel vers un endpoint IA compatible Chat Completions. Aucune clé n'est fournie dans le projet.

## Limites documentaires

Les PDF Idrīsiyya et Barhout fournis sont essentiellement des scans. Ils ne fournissent pas une traduction française validée exploitable automatiquement. L'application n'invente donc pas de traduction française. Elle conserve l'original arabe en image et indique lorsqu'une traduction validée n'est pas disponible.

Le corpus coranique n'est pas inclus dans cette V2. La section « Identification et Sélection Sacrée » ne fabrique donc pas un verset prétendument idéal.

## Compilation Android

Le projet reste un projet web/PWA empaquetable par Capacitor. La machine de travail actuelle ne contient pas l'Android SDK/Gradle nécessaires à la production finale d'un APK.

Commandes :

```bash
npm install
npx cap add android
npx cap sync android
npx cap open android
```

Puis générer un APK signé depuis Android Studio.
