[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application version
version = 0.1

# (str) Entry point of the app
entrypoint = myapp.py

# (list) Application requirements
requirements = python3,kivy

# (list) Supported architectures
android.archs = armeabi-v7a

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Package format to use: apk, aab, or all (aab requires Android API >= 30)
package.format = apk

# (list) Permissions
android.permissions = INTERNET

# (bool) Copy .so files into .apk (for faster loading on some devices)
android.copy_libs = 1

# (str) Minimum API your app will support
android.minapi = 21

# (str) NDK API level (keep igual ao minapi)
android.ndk_api = 21

# (str) Target API level (controlado pelo sdkmanager no workflow)
# NÃO USAR android.sdk pois está depreciado

# (bool) Use SDL2
android.use_sdl2 = True

# (bool) Private app storage (usado para isolar o ambiente Python)
android.private_storage = True

# (list) Include these files into APK
source.include_exts = py,png,jpg,kv,atlas

# (str) Icon (opcional)
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash (opcional)
# presplash.filename = %(source.dir)s/presplash.png

# (str) Android NDK version usado pelo workflow
android.ndk = 25b

# (str) Entry point if renomeado
# entrypoint = main.py
