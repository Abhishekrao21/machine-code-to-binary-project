# def inttob(n):
#     if n>=0:
#         base=2
#         binary=""
#         q=n
#         while q !=0 :
#             rem=q%2
#             q=q//2
#             binary=str(rem)+binary
#         while len(binary) != 12:
#             binary='0'+binary
#         return binary
#     else:
#         n=4096+n
#         binary=""
#         q=n
#         while q !=0 :
#             rem=q%2
#             q=q//2
#             binary=str(rem)+binary
#         while len(binary) != 12:
#             binary='1'+binary
#         return inttob(n)
def inttob(n,size):
    if n>=0:
        base=2
        binary=""
        q=n
        while q !=0 :
            rem=q%2
            q=q//2
            binary=str(rem)+binary
        while len(binary) != size:
            binary='0'+binary
        return binary
    else:
        n=(2**size)+n
        binary=""
        q=n
        while q !=0 :
            rem=q%2
            q=q//2
            binary=str(rem)+binary
        return binary

#so we need 6 different if 1 for r type ,i type ,s type ...
# like this for r type
f = open("/Users/abhishekrao/Documents/vscode/python/read.txt", "r")
j = open("/Users/abhishekrao/Documents/vscode/python/write.txt", "a")
line_no=0
Visual_Halt=False
for line in f:
    if Visual_Halt==True:
        print('Error: Visual Halt at line',line_no)
        Visual_Halt=False
    line_no=line_no+1
    if line == '':
        continue
    if line =="beq zero,zero,0x00000000":
        Visual_Halt==True
        continue
    # Example of a line is (sltu rd, rs1, rs2)
    registers = {
        'x0': '00000', 'x1': '00001', 'x2': '00010', 'x3': '00011', 'x4': '00100',
        'x5': '00101', 'x6': '00110', 'x7': '00111', 'x8': '01000', 'x9': '01001',
        'x10': '01010', 'x11': '01011', 'x12': '01100', 'x13': '01101', 'x14': '01110',
        'x15': '01111', 'x16': '10000', 'x17': '10001', 'x18': '10010', 'x19': '10011',
        'x20': '10100', 'x21': '10101', 'x22': '10110', 'x23': '10111', 'x24': '11000',
        'x25': '11001', 'x26': '11010', 'x27': '11011', 'x28': '11100', 'x29': '11101',
        'x30': '11110', 'x31': '11111'
    }
    abi_mapping = {
    'zero': '00000','ra': '00001','sp': '00010','gp': '00011','tp': '00100','t0':'00101',
    't1': '00110','t2': '00111','s0':'01000','fp':'01000','s1': '01001',
    'a0': '01010','a1': '01011','a2': '01100','a3': '01101',
    'a4': '01110','a5': '01111','a6': '10000','a7': '10001','s2': '10010',
    's3': '10011','s4': '10100','s5': '10101','s6': '10110','s7': '10111',
    's8': '11000','s9': '11001','s10': '11010','s11': '11011','t3': '11100',
    't4': '11101','t5': '11110','t6': '11111',
    }

    line = list(line.split(" "))

    #r type
    R_type = ['add', 'sub', 'sll', 'slt', 'sltu', 'xor', 'srl', 'or', 'and']
    if line[0] in R_type:
        if line[0] =='add':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('000')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='sub':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:# so 
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0100000')
            j.write(abi_mapping[rs2])
            if sublist[1] == 'x0':
                j.write(registers[rs1])
            elif sublist[1] in abi_mapping:
                j.write(abi_mapping[rs1])
            else:
                print("Error: reg not found")
            j.write('000')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='slt':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('010')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='sltu':
            sublist=list(line[1].split(",")) 
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('011')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='xor': 
            sublist=list(line[1].split(",")) 
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('100')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')
            
        elif line[0]=='sll':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('001')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='srl':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('101')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='or':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('110')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='and':
            sublist=list(line[1].split(","))
            rd = sublist[0]
            rs1 = sublist[1]
            if sublist[2][0:-1] in abi_mapping:
                rs2 = sublist[2][0:-1]
            elif sublist[2] in abi_mapping:
                rs2 = sublist[2]
            else:
                print("Error: reg  not found",line_no)
            j.write('0000000')
            j.write(abi_mapping[rs2])
            j.write(abi_mapping[rs1])
            j.write('111')
            j.write(abi_mapping[rd])
            j.write('0110011')
            j.write('\n')
    #i type
    s_type = ['lw', 'addi', 'stliu', 'jalr']
    if line[0] in s_type:
        if line[0] == 'lw':
            sublist = list(line[1].split(','))
            rd = sublist[0] 
            k = 0  # Corrected the index
            for i in sublist[1]:
                k+=1
                if (i == '('):
                    break
            rs = sublist[1][k:-2]  
            if n>(2**11)-1 or n<(-2**11):
                j.write('imm out of range')
                berak
            else:
                imm = inttob(int(sublist[1][0:k-1]),11) 
                if rs not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rd not in abi_mapping:
                        j.write("register not found")
                        break
                    else:
                    
                        j.write(imm)
                        j.write(abi_mapping[rs])
                        j.write('010')
                        j.write(abi_mapping[rd])
                        j.write('0000011\n')  # Corrected the index
            
        if line[0] == 'addi':
            sublist = list(line[1].split(','))
            rd = sublist[0]
            rs = sublist[1]
            imm = inttob(int(sublist[2]),11)
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found')
                    break
                else:
                    if rs not in abi_mapping:
                        j.write('register not found')
                        break
                    else:
                        j.write(imm)
                        j.write(abi_mapping[rs])
                        j.write('000')
                        j.write(abi_mapping[rd])
                        j.write('0010011\n')

        if line[0] == 'stliu':
            sublist = list(line[1].split(','))
            rd = sublist[0]
            rs = line[1]
            imm = inttob(int(sublist[2]),11)
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found')
                    break
                else:
                    if rs not in abi_mapping:
                        j.write('register not found')
                        break
                    else:
                        j.write(imm)
                        j.write(registers[rs])
                        j.write('011')
                        j.write(registers[rd])
                        j.write('0010011\n')

        if line[0] == 'jalr':
            sublist = list(line[1].split(','))
            rd = sublist[0]
            x6 = '00110'
            imm = inttob(int(sublist[2]),11)
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found')
                    break
                else:
                    j.write(imm)
                    j.write(x6)
                    j.write('010')
                    j.write(registers[rd])
                    j.write('0000011\n')


    #S-type
    elif line[0] == 'sw':
        sublist=list(line[1].split(","))
        rs2=sublist[0]
        sublist=list(sublist[1].split("("))
        imm=int(sublist[0])
        rs1=sublist[1][0:-1]
        if rs2 in abi_mapping and rs1 in abi_mapping:
            if -2048<=imm<2048:
                imm=inttob(imm,12)
                rs2=abi_mapping[rs2]
                rs1=abi_mapping[rs1]
                print(imm)
                j.write(imm[0:7])
                j.write(rs2)
                j.write(rs1)
                j.write('010')
                j.write(imm[7:])
                j.write('0100011')
                j.write('\n')
            else:
                print('Error: imm out of range ',line_no)
                break
        else:
            print('Error: rs1 or rs2 not found in abi_mapping', line_no)
            break
    # b type
    b_type = ('beq','bne','bge','bgeu','blt','bltu')
    if line[0] in b_type:
        if line[0] == 'blt':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                        j.write(imm[0])
                        j.write(imm[1:7])
                        j.write(abi_mapping[rs2])
                        j.write(abi_mapping[rs1])
                        j.write('100')
                        j.write(imm[7:11])
                        j.write(imm[1])
                        j.write('1100011\n')
            

        if line[0] == 'beq':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                            j.write(imm[0])
                            j.write(imm[1:7])
                            j.write(abi_mapping[rs2])
                            j.write(abi_mapping[rs1])
                            j.write('000')
                            j.write(imm[7:11])
                            j.write(imm[1])
                            j.write('1100011\n')
                           

        if line[0] == 'bne':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                            j.write(imm[0])
                            j.write(imm[1:7])
                            j.write(abi_mapping[rs2])
                            j.write(abi_mapping[rs1])
                            j.write('001')
                            j.write(imm[7:11])
                            j.write(imm[1])
                            j.write('1100011\n')
                            
                        
        if line[0] == 'bge':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                        j.write(imm[0])
                        j.write(imm[1:7])
                        j.write(abi_mapping[rs2])
                        j.write(abi_mapping[rs1])
                        j.write('101')
                        j.write(imm[7:11])
                        j.write(imm[1])
                        j.write('1100011\n')
                      
                            
        if line[0] == 'bltu':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                        j.write(imm[0])
                        j.write(imm[1:7])
                        j.write(abi_mapping[rs2])
                        j.write(abi_mapping[rs1])
                        j.write('110')
                        j.write(imm[7:11])
                        j.write(imm[1])
                        j.write('1100011\n')
                       

        if line[0] == 'bgeu':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[0]),12)
            if n>2**11-1 or n<-2**11:
                j.write('imm out of range')
                break
            else:
                if rs1 not in abi_mapping:
                    j.write("register not found")
                    break
                else:
                    if rs2 not in abi_mapping:
                        j.wite("register not found")
                        break
                    else:
                        j.write(imm[0])
                        j.write(imm[1:7])
                        j.write(abi_mapping[rs2])
                        j.write(abi_mapping[rs1])
                        j.write('111')
                        j.write(imm[7:11])
                        j.write(imm[1])
                        j.write('1100011\n')
    
    # U type
    elif line[0]=='lui':
        sublist=list(line[1].split(","))
        rd=sublist[0]
        imm=int(sublist[1][0:-1])
        if rd in abi_mapping:
            rd=abi_mapping[rd]
            if -2147483648<=imm<2147483648:
                imm=inttob(imm,32)
                j.write(imm[0:20])
                j.write(rd)
                j.write('0110111')
                j.write('\n')
            else:
                print('Error: imm not in range',line_no)
        else:
            print("Error: rd not found",line_no)
        

    elif line[0]=='auipc':
        sublist=list(line[1].split(","))
        rd=sublist[0]
        imm=int(sublist[1][0:-1])
        if rd in abi_mapping:
            rd=abi_mapping[rd]
            if -2147483648<=imm<2147483648:
                imm=inttob(imm,32)
                j.write(imm[0:20])
                j.write(rd)
                j.write('0010111')
                j.write('\n')
            else:
                print('Error: imm not in range',line_no)
        else:
            print("Error: rd not found",line_no)
    else:
        print('error not found', line_no)
        break
    #j type


    
if Visual_Halt==False:
    print('Error: visual halt not found')
# Close the files after processing
f.close()
j.close()
