import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def buscarEDecodificarInstrucao():
    #print ('Implementar a buscarEDecodificarInstrucao')

    instrucao = memoria.getValorMemoria(registrador_cp)
    print(instrucao)
    if instrucao == 0x00:
        print("Instrução ADD Registrador e Byte")
        return 0
    elif instrucao == 0x01:
        print("Instrução ADD Registrador e Registrador")
        return 1
    elif instrucao == 0x10:
        print("Instrução INC Registrador")
        return 2
    elif instrucao == 0x20:
        print("Instrução DEC Registrador")
        return 3
    elif instrucao == 0x30:
        print("Instrução SUB Registrador e Byte")
        return 4
    elif instrucao == 0x31:
        print("Instrução SUB Registrador e Registrador")
        return 5
    elif instrucao == 0x40:
        print("Instrução MOV Registrador e Byte")
        return 6
    elif instrucao == 0x41:
        print("Instrução MOV Registrador e Registrador")
        return 7
    elif instrucao == 0x50:
        print("Instrução JMP Byte")
        return 8
    elif instrucao == 0x60:
        print("Instrução CMP Registrador e Byte")
        return 9
    elif instrucao == 0x61:
        print("Instrução CMP Registrador e Registrador")
        return 10
    elif instrucao == 0x70:
        print("Instrução JZ Byte")
        return 11
    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_cp, registrador_ax, registrador_bx, registrador_cx, registrador_dx, flag_zero

    if idInstrucao == 0:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax += valor
        elif idRegistrador == 3:
            registrador_bx += valor
        elif idRegistrador == 4:
            registrador_cx += valor
        elif idRegistrador == 5:
            registrador_dx += valor
    elif idInstrucao == 1:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2 and idRegistrador2 == 3:
            registrador_ax += registrador_bx 
        elif idRegistrador == 2 and idRegistrador2 == 4:
            registrador_ax += registrador_cx
        elif idRegistrador == 2 and idRegistrador2 == 5:
            registrador_ax += registrador_dx
        elif idRegistrador == 3 and idRegistrador2 == 2:
            registrador_bx += registrador_ax
        elif idRegistrador == 3 and idRegistrador2 == 4:
            registrador_bx += registrador_cx
        elif idRegistrador == 3 and idRegistrador2 == 5:
            registrador_bx += registrador_dx
        elif idRegistrador == 4 and idRegistrador2 == 2:
            registrador_cx += registrador_ax
        elif idRegistrador == 4 and idRegistrador2 == 3:
            registrador_cx += registrador_bx
        elif idRegistrador == 4 and idRegistrador2 == 5:
            registrador_cx += registrador_dx
        elif idRegistrador == 5 and idRegistrador2 == 2:
            registrador_dx += registrador_ax
        elif idRegistrador == 5 and idRegistrador2 == 3:
            registrador_dx += registrador_bx
        elif idRegistrador == 5 and idRegistrador2 == 4:
            registrador_dx += registrador_cx
    elif idInstrucao == 2:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        if idRegistrador == 2:
            registrador_ax += 1
        elif idRegistrador == 3:
            registrador_bx += 1
        elif idRegistrador == 4:
            registrador_cx += 1
        elif idRegistrador == 5:
            registrador_dx += 1
    elif idInstrucao == 3:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        if idRegistrador == 2:
            registrador_ax -= 1
        elif idRegistrador == 3:
            registrador_bx -= 1
        elif idRegistrador == 4:
            registrador_cx -= 1
        elif idRegistrador == 5:
            registrador_dx -= 1
    elif idInstrucao == 4:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax = registrador_ax - valor
        elif idRegistrador == 3:
            registrador_bx = registrador_bx - valor
        elif idRegistrador == 4:
            registrador_cx = registrador_cx - valor
        elif idRegistrador == 5:
            registrador_dx = registrador_dx - valor
    elif idInstrucao == 5:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2 and idRegistrador2 == 3:
            registrador_ax -= registrador_bx 
        elif idRegistrador == 2 and idRegistrador2 == 4:
            registrador_ax -=  registrador_cx
        elif idRegistrador == 2 and idRegistrador2 == 5:
            registrador_ax -=  registrador_dx
        elif idRegistrador == 3 and idRegistrador2 == 2:
            registrador_bx -=  registrador_ax
        elif idRegistrador == 3 and idRegistrador2 == 4:
            registrador_bx -=  registrador_cx
        elif idRegistrador == 3 and idRegistrador2 == 5:
            registrador_bx -=  registrador_dx
        elif idRegistrador == 4 and idRegistrador2 == 2:
            registrador_cx -=  registrador_ax
        elif idRegistrador == 4 and idRegistrador2 == 3:
            registrador_cx -=  registrador_bx
        elif idRegistrador == 4 and idRegistrador2 == 5:
            registrador_cx -=  registrador_dx
        elif idRegistrador == 5 and idRegistrador2 == 2:
            registrador_dx -=  registrador_ax
        elif idRegistrador == 5 and idRegistrador2 == 3:
            registrador_dx -=  registrador_bx
        elif idRegistrador == 5 and idRegistrador2 == 4:
            registrador_dx -=  registrador_cx
    elif idInstrucao == 6:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        valor = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2:
            registrador_ax = valor
        elif idRegistrador == 3:
            registrador_bx = valor
        elif idRegistrador == 4:
            registrador_cx = valor
        elif idRegistrador == 5:
            registrador_dx = valor
    elif idInstrucao == 7:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2 and idRegistrador2 == 3:
            registrador_ax = registrador_bx
        elif idRegistrador == 2 and idRegistrador2 == 4:
            registrador_ax = registrador_cx
        elif idRegistrador == 2 and idRegistrador2 == 5:
            registrador_ax = registrador_dx
        elif idRegistrador == 3 and idRegistrador2 == 2:
            registrador_bx = registrador_ax
        elif idRegistrador == 3 and idRegistrador2 == 4:
            registrador_bx = registrador_cx
        elif idRegistrador == 3 and idRegistrador2 == 5:
            registrador_bx = registrador_dx
        elif idRegistrador == 4 and idRegistrador2 == 2:
            registrador_cx = registrador_ax
        elif idRegistrador == 4 and idRegistrador2 == 3:
            registrador_cx = registrador_bx
        elif idRegistrador == 4 and idRegistrador2 == 5:
            registrador_cx = registrador_dx
        elif idRegistrador == 5 and idRegistrador2 == 2:
            registrador_dx = registrador_ax
        elif idRegistrador == 5 and idRegistrador2 == 3:
            registrador_dx = registrador_bx
        elif idRegistrador == 5 and idRegistrador2 == 4:
            registrador_dx = registrador_cx
    elif idInstrucao == 8:
        byte = memoria.getValorMemoria(registrador_cp + 1)
        registrador_cp = byte
    elif idInstrucao == 9:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        byte = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2 and registrador_ax == byte:
            flag_zero = True
        elif idRegistrador == 3 and registrador_bx == byte:
            flag_zero = True
        elif idRegistrador == 4 and registrador_cx == byte:
            flag_zero = True
        elif idRegistrador == 5 and registrador_dx == byte:
            flag_zero = True
    elif idInstrucao == 10:
        idRegistrador = memoria.getValorMemoria(registrador_cp + 1)
        idRegistrador2 = memoria.getValorMemoria(registrador_cp + 2)
        if idRegistrador == 2 and idRegistrador2 == 3:
            if registrador_ax == registrador_bx:
                flag_zero = True
        elif idRegistrador == 2 and idRegistrador2 == 4:
            if registrador_ax == registrador_cx:
                flag_zero = True
        elif idRegistrador == 2 and idRegistrador2 == 5:
            if registrador_ax == registrador_dx:
                flag_zero = True
        elif idRegistrador == 3 and idRegistrador2 == 2:
            if registrador_bx == registrador_ax:
                flag_zero = True
        elif idRegistrador == 3 and idRegistrador2 == 4:
            if registrador_bx == registrador_cx:
                flag_zero = True
        elif idRegistrador == 3 and idRegistrador2 == 5:
            if registrador_bx == registrador_dx:
                flag_zero = True
        elif idRegistrador == 4 and idRegistrador2 == 2:
            if registrador_cx == registrador_ax:
                flag_zero = True
        elif idRegistrador == 4 and idRegistrador2 == 3:
            if registrador_cx == registrador_bx:
                flag_zero = True
        elif idRegistrador == 4 and idRegistrador2 == 5:
            if registrador_cx == registrador_dx:
                flag_zero = True
        elif idRegistrador == 5 and idRegistrador2 == 2:
            if registrador_dx == registrador_ax:
                flag_zero = True
        elif idRegistrador == 5 and idRegistrador2 == 3:
            if registrador_dx == registrador_bx:
                flag_zero = True
        elif idRegistrador == 5 and idRegistrador2 == 4:
            if registrador_dx == registrador_cx:
                flag_zero = True
    elif idInstrucao == 11:
        byte = memoria.getValorMemoria(registrador_cp + 1)
        if flag_zero == True:
            registrador_cp = byte
    #print ('Implementar a lerOperadoresExecutarInstrucao')

def calcularProximaInstrucao(idInstrucao):
    global registrador_cp, flag_zero

    if idInstrucao == 0 or idInstrucao == 1:
        registrador_cp += 3
        print("Mudando Regitrador_CP para", registrador_cp)
    elif idInstrucao == 2 or idInstrucao == 3:
        registrador_cp += 2
        print("Mudando Regitrador_CP para", registrador_cp)
    elif idInstrucao == 4 or idInstrucao == 5:
        registrador_cp += 3
        print("Mudando Regitrador_CP para", registrador_cp)
    elif idInstrucao == 6 or idInstrucao == 7:
        registrador_cp += 3
        print("Mudando Regitrador_CP para", registrador_cp)   
    elif idInstrucao == 8:
        print("Mudando Regitrador_CP para", registrador_cp)
    elif idInstrucao == 9 or idInstrucao == 10:
        registrador_cp += 3
        print("Mudando Regitrador_CP para", registrador_cp)
    elif idInstrucao == 11:
        if flag_zero == True:
            0
        else:
            registrador_cp += 2
        print("Mudando Regitrador_CP para", registrador_cp)

    #print ('Implementar a calcularProximaInstrucao')

def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)