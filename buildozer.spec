[app]

title = MeuAppKivy
package.name = meuapp
package.domain = org.exemplo
version = 0.1

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

bootstrap = sdl2
android.logcat_filters = *:S python:D
copy_libs = 1

[buildozer]

log_level = 2
use_sudo = False
build_dir = .buildozer
