"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "AVOID GAME",
    version = "2017",
    description = "The best cars game",
    executables = [Executable("main.py")],
)