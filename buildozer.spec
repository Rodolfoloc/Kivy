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
# API e ferramentas fixadas para compatibilidade com GitHub Actions
#android.sdk = 31
android.ndk = 23b
android.api = 31
android.build_tools_version = 34.0.0

# Evita problemas com build-tools > 34
android.accept_sdk_license = True

# AndroidX ativado, suporte legado desativado
android.enable_androidx = 1
android.use_android_support = 0

# Permissões básicas (adicione mais conforme necessário)
android.permissions = INTERNET

# Ícones e splash screen opcionais
# android.icon = assets/icon.png
# android.presplash = assets/presplash.png

# Nome do pacote de saída (pasta bin/)
android.dist_name = meuapp

[toolchain]
# Arquitetura mínima para Android (adicione arm64-v8a se quiser multiplataforma)
android.archs = armeabi-v7a

[buildozer.packaging]
# Incluir arquivos adicionais se necessário
# include_patterns = assets/*,data/*

[buildozer.android]
# Caminhos explícitos para o SDK/NDK se necessário
# sdk_path = $HOME/android-sdk
# ndk_path = $HOME/android-sdk/ndk/23.1.7779620

[hostpython]
# hostpython = path/to/hostpython
