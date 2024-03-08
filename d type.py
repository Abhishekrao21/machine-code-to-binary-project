f = open("bot.txt", "r")
j = open("big.txt", "a")

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

line = f.readline()
while line != "":
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
    abi_mapping== {
    'zero': '00000','ra': '00001','sp': '00010','gp': '00011','tp': '00100','t0':'00101',
    't1': '00110','t2': '00111','s0':'01000','fp':'01000','s1': '01001',
    'a0': '01010','a1': '01011','a2': '01100','a3': '01101',
    'a4': '01110','a5': '01111','a6': '10000','a7': '10001','s2': '10010',
    's3': '10011','s4': '10100','s5': '10101','s6': '10110','s7': '10111',
    's8': '11000','s9': '11001','s10': '11010','s11': '11011','t3': '11100',
    't4': '11101','t5': '11110','t6': '11111',
    }
    b_type = ('beq','bne','bge','bgeu','blt','bltu')
    

    line = list(line.split(" "))

    print(sublist)
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
                        
    line = f.readline()

f.close()
j.close()
