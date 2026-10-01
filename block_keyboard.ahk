#Requires AutoHotkey v2.0
#SingleInstance Force

; Exige les droits d'administrateur (indispensable pour bloquer les entrées système)
if not A_IsAdmin {
    Run('*RunAs "' A_ScriptFullPath '"')
    ExitApp()
}

; Bloque toutes les entrées clavier et souris via l'API Windows
BlockInput("On")

; Empêche le script de se fermer
Persistent()