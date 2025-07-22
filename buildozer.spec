[app]

# Nome interno do aplicativo (sem espaços)
title = MeuAppKivy
package.name = meuapp
package.domain = org.exemplo

# Arquivo Python principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Main script
entrypoint = main.py

# Versão do app
version = 0.1

# Ícone do aplicativo (opcional)
# icon.filename = %(source.dir)s/icon.png

# Incluir arquivos e pastas extras
# android.add_assets = assets/

# Módulos que seu app usa
requirements = python3,kivy

# Orientação (portrait, landscape ou all)
orientation = portrait

# Suporte a armazenamento interno
android.private_storage = true

# Versão mínima e alvo do Android
android.minapi = 21
android.api = 33

# Versão do Android Build Tools (evita erros com versões novas)
android.build_tools_version = 33.0.2

# NDK recomendado
android.ndk = 23b

# Aceitar licenças automaticamente (necessário para CI/CD)
android.accept_sdk_license = true
android.accept_ndk_license = true

# Impede que o Buildozer baixe uma versão recente demais
android.sdk = 33

# Habilite suporte a multitouch
android.enable_armeabi_v7a = 1
android.enable_arm64_v8a = 1

# (opcional) evitar crashes com entrada de teclado em versões recentes do Android
android.entrypoint = org.kivy.android.PythonActivity

# Versão do Python-for-Android (opcional, use uma estável se necessário)
# p4a.branch = master

# Logs
log_level = 2

# Excluir arquivos grandes
ignore_setup_py = 1

[buildozer]

# pasta onde o APK será gerado
bin_dir = bin

# limpar builds antigos
clean_build = false
