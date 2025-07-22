[app]

# (str) Nome do pacote (aparece no nome do app instalado)
title = MeuAppKivy

# (str) Nome da pasta principal (onde está seu main.py)
package.name = meuapp

# (str) Domínio reverso
package.domain = org.exemplo

# (str) Arquivo principal da aplicação
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# (list) Requisitos Python e Cython
requirements = python3,kivy

# (list) Arquiteturas Android a incluir (use só arm64-v8a se quiser APK menor)
android.archs = armeabi-v7a,arm64-v8a

# (str) Nome do arquivo APK gerado
android.debug = 1
android.logcat_filters = *:S python:D
android.minapi = 21
android.api = 33
android.ndk = 25b
android.ndk_api = 21

# (str) Bootstrap SDL2 (recomendado)
bootstrap = sdl2

# (int) Orientação da tela
orientation = portrait

# (str) Tema
android.theme = @android:style/Theme.NoTitleBar

# (bool) Copiar bibliotecas compartilhadas
copy_libs = 1

# (str) Ícone (opcional)
# icon.filename = %(source.dir)s/icon.png


[buildozer]

# (str) Diretório onde os arquivos temporários ficam
build_dir = .buildozer

# (str) Log level
log_level = 2

# (bool) Evita usar sudo
use_sudo = False

# (bool) Limpa antes de compilar
# clean_build = 1
