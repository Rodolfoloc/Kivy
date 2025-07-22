[app]

title = MeuAppKivy
package.name = meuapp
package.domain = org.exemplo
source.dir = .
source.include_exts = py
main.py = main.py

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = armeabi-v7a,arm64-v8a

# SDL2 é o bootstrap moderno e recomendado para apps com interface gráfica
bootstrap = sdl2

# (opcional) Mostra logs do Python no logcat
android.logcat_filters = *:S python:D

# (bool) Mantém libs embutidas no APK
copy_libs = 1

[buildozer]

log_level = 2
use_sudo = False
build_dir = .buildozer
