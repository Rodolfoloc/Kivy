[app]
title = MeuAppKivy
package.name = meuapp
package.domain = org.exemplo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Versão do SDK e build-tools
android.sdk = 31
android.ndk = 23b
android.api = 31
android.build_tools_version = 34.0.0

# Ativa o uso do AndroidX
android.enable_androidx = 1
android.use_android_support = 0

# Ativa os serviços padrões
android.permissions = INTERNET

# Se usar assets (imagens, fontes, etc.), descomente a linha abaixo
# android.presplash = assets/presplash.png

# Usa OpenJDK 17 (compatível com GitHub Actions runner)
android.gradle_dependencies =

# Se você tiver problemas com o ambiente, defina:
# android.accept_sdk_license = True

# Caminho de saída do APK
android.dist_name = meuapp

[toolchain]
# arquitetura padrão, se quiser adicionar x86 para emulador:
# android.archs = armeabi-v7a,arm64-v8a
android.archs = armeabi-v7a

[buildozer.packaging]
# inclui arquivos adicionais se necessário
# include_patterns = assets/*,data/*

[buildozer.android]
# Força o uso do SDK/NDK pré-instalado
# Se usar caminhos customizados, declare aqui

[hostpython]
# Se você estiver empacotando dependências nativas complexas, pode usar isso:
# hostpython = path/to/hostpython
