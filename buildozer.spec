[app]
title = MeuAppKivy
package.name = meuapp
package.domain = org.exemplo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.sdk = 31
android.ndk = 23b
android.api = 31
android.build_tools_version = 34.0.0

android.enable_androidx = 1
android.use_android_support = 0

android.permissions = INTERNET

# android.presplash = assets/presplash.png
# android.icon = assets/icon.png

# Aceita automaticamente as licenças do SDK
android.accept_sdk_license = True

# Caminho de saída do APK
android.dist_name = meuapp

[toolchain]
android.archs = armeabi-v7a

[buildozer.packaging]
# include_patterns = assets/*,data/*

[buildozer.android]
# Use variáveis de ambiente no GitHub Actions
# Ex: ANDROID_SDK_ROOT já está no GITHUB_ENV

[hostpython]
# hostpython = path/to/hostpython
