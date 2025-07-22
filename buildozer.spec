[app]

title = MeuApp
package.name = meuapp
package.domain = org.exemplo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.2.1

fullscreen = 1

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = true
android.accept_ndk_license = true

android.archs = armeabi-v7a, arm64-v8a

# (opcional) ícone
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
