# Miftah al-Huruf

Prototype mobile-first/offline reader for La Bourdah, Sirr Idrissiya, Barhout/Celcelutiye, plus the technical source.

## What is included
- Offline page-image reader for the three main scanned books.
- Exact Abjad Maghrébin table supplied by the user.
- Exact four-element classification and pivot 2049.
- Three-way arithmetic verification.
- Structured six-part analysis screen.
- Local assistant shell.
- PWA manifest/service worker.

## Android/APK
This package is web/PWA source prepared for Capacitor. A compiled/signed APK is **not included** because the current build environment does not contain a working Android SDK/Gradle toolchain. To package it, put the contents in a Capacitor project, add Android, copy the web assets, and build the release APK with Android Studio/Gradle.

The four source PDFs are included as files; the three main books also have compressed page images for offline reading.
