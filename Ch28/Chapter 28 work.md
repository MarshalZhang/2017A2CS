# Chapter 28 work
# Marshal Zhang from S3C3 Marshal

Task 28.01
LDM #2 
STO A
LDM #10 
STO B

LDD A
ADD B
STO C

LDD B
XOR #&FF
INC ACC
ADD A
STO D


Task 28.02
 
      LDD A
      CMP #0
      JPE ELSE
THEN: STO B
      JMP ENDIF
ELSE: LDD B
      DEC ACC
      STO B


Task 28.03

      LDM #1
      STO Number
      LDM #0
      STO Total
      LDM #5
      STO Max
LOOP: LDD Total
      ADD Number
STO Total

      LDD Number
      INC ACC
      STO Number
UNTIL:CMP Max
      DEC ACC
      JPN LOOP
ENDLOOP:


Task 28.04

LDM #0
       STO Count
       LDM #78
 letter N
       STO Letter
 LOOP: LDD Count
       INC ACC
       STO Count
       IN
       CMP Letter
       JPN LOOP
ENDLOOP:

Task 28.05

LDM #0
        STO Count
        LDM #78
letter N
        STO Letter
LOOP:   LDD Count
        INC ACC
        STO Count
        IN
        CMP Letter
        JPN LOOP
ENDLOOP:LDM #48
        ADD Count
digit to ASCII
        OUT

End of chapter questions

1 a AND compares two bits in the same position and if both are 1 it puts a 1 in this position of the result word, otherwise it puts a 0 in this position of the result word

b AND MASK
MASK: #B00001111 // mask

2
Loop        LDR        #0 
            STI        STRING
            INC        IX
            CMP        #33
            JPN        LOOP
            END