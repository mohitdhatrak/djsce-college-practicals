DATA SEGMENT 
    MSG DB "Hello World$"
DATA ENDS

CODE SEGMENT
    ASSUME CS: CODE, DS: DATA

    START:
        MOV AX, DATA
        MOV DS, AX
        LEA DX, MSG
        
        ; interrupt to display string ending with $
        MOV AH, 09H
        INT 21H
        
        ; interrupt to input single char with echo
        MOV AH, 01H
        INT 21H
        
        ; interrupt to display a single char
        MOV DL, AL
        MOV AH, 02H
        INT 21H
        
        ; interrupt to terminate program
        MOV AH, 4CH
        INT 21H 
    END START
CODE ENDS