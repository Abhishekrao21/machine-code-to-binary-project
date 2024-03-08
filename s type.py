f = open('name.txt', 'r')
j = open('trial.txt', 'a')

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
       #make sublist inside the 
   
    s_type = ['lw', 'addi', 'sltiu', 'jalr']
    if line[0] in s_type:
        if line[0] == 'lw':
            sublist = list(line[1].split(','))
            rd = sublist[0] 
            
            k = 0  # Corrected the index
            for i in sublist[1]:
                k+=1
                if (i == '('):
                    break
            rs = sublist[1][k:-1] 
            
            if int(sublist[1][0:k-1])>(2**11)-1 or int(sublist[1][0:k-1])<(-2**11):
                j.write('imm out of range\n')
                break
            else:
                imm = inttob(int(sublist[1][0:k-1]),12) 
                if rs not in abi_mapping:
                    j.write("register not founds\n")
                    break
                else:
                    if rd not in abi_mapping:
                        j.write("register not found\n")
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
            imm = inttob(int(sublist[2]),12)
            n = int(sublist[2])
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range\n')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found\n')
                    break
                else:
                    if rs not in abi_mapping:
                        j.write('register not found\n')
                        break
                    else:
                        j.write(imm)
                        j.write(abi_mapping[rs])
                        j.write('000')
                        j.write(abi_mapping[rd])
                        j.write('0010011\n')

        if line[0] == 'sltiu':
            sublist = list(line[1].split(','))
            rd = sublist[0]
            rs = sublist[1]
            imm = inttob(int(sublist[2]),12)
            n = int(sublist[2])
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range\n')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found\n')
                    break
                else:
                    if rs not in abi_mapping:
                        j.write('register not found\n')
                        break
                    else:
                        j.write(imm)
                        j.write(abi_mapping[rs])
                        j.write('011')
                        j.write(abi_mapping[rd])
                        j.write('0010011\n')

        if line[0] == 'jalr':
            sublist = list(line[1].split(','))
            n = sublist[2]
            rd = sublist[0]
            x6 = '00110'
            imm = inttob(int(sublist[2]),12)
            
            n = int(sublist[2])
            if n>(2**11-1) or n<-2**11:
                j.write('imm out of range\n')
                break
            else:
                if rd not in abi_mapping:
                    j.write('register not found\n')
                    break
                else:
                    j.write(imm)
                    j.write(x6)
                    j.write('010')
                    j.write(abi_mapping[rd])
                    j.write('0000011\n')


            
    line = f.readline()  # Corrected the function call

f.close()
j.close()
