#Requires AutoHotkey v2.0

/*
vk1D : 無変換
vk1C : 変換
*/

; 無変換を押しながら変換でIMEON
#HotIf GetKeyState("vk1D")
vk1C::vk1C
#HotIf

; 無変換を押しながら無変換でIMEOFF
#HotIf GetKeyState("vk1C")
vk1D::vk1D
#Hotif

; カーソル移動
vk1D & i:: Send("{Blind}{UP}")
vk1D & j:: Send("{Blind}{LEFT}")
vk1D & k:: Send("{Blind}{DOWN}")
vk1D & l:: Send("{Blind}{RIGHT}")

; ワープ移動
vk1D & <::Home
vk1D & >::End
vk1D & p::PgUp
vk1D & `;::PgDn

; 削除
vk1D & u::Delete
vk1D & o::BackSpace

; 生成スクリプト読み込み
#Include ./include.ahk