; test.ams -- Practica 1: operacion 5+9*7-10*5-3
; instrucciones: mov neg inc jmp loop

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.DATA
numero DB 11111111b



.code
main proc
    Mov ax,0
	Mov ecx,5

	L1:
		inc ax
        loop L1
        jmp et1

    et1:
    mov bx, numero
    neg numero


main endp
end main


