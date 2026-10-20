# Construire l'APK Android

## Pré-requis

- Node.js récent
- Android Studio
- Android SDK + Build Tools
- JDK compatible avec la version de Gradle/Android Gradle Plugin utilisée

## Commandes

```bash
npm install
npx cap add android
npx cap sync android
npx cap open android
```

Dans Android Studio :
1. attendre la synchronisation Gradle ;
2. sélectionner `app` ;
3. choisir `Build > Generate Signed Bundle / APK` ;
4. choisir APK ;
5. créer/sélectionner le keystore ;
6. produire la version release.

Alternative en terminal après `npx cap add android` :

```bash
cd android
./gradlew assembleDebug
```

Le résultat debug sera dans `android/app/build/outputs/apk/debug/`.
