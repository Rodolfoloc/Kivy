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

# (list) Application requirements
requirements = python3,kivy

# (str) Entry point of the app
# Use your main python file name
entrypoint = myapp.py

# (list) Permissions required by the app
android.permissions = INTERNET

# (bool) Whether to include the Kivy launcher or package your app standalone
# False means standalone APK
android.arch = armeabi-v7a

# (int) Target Android API (use current stable)
android.api = 33

# (int) Minimum Android API your app will support
android.minapi = 21

# (int) Android SDK build tools version
android.sdk = 33

# (int) Android NDK version
android.ndk = 25b

# (str) Android NDK API level
android.ndk_api = 21

# (bool) Whether to copy the .so files
android.copy_libs = 1

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Use SDL2 backend (True)
android.use_sdl2 = True

# (str) Supported orientation
orientation = portrait

# (str) Source include patterns (default is empty)
# source.include_exts = py,png,jpg,kv,atlas

# (list) List of modules to include/exclude
# exclude_modules = 

# (str) Icon of your app
# icon.filename = %(source.dir)s/data/icon.png
