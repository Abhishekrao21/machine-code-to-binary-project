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
    b_type = ('beq','bne','bge','bgeu','blt','bltu')
    

    line = list(line.split(" "))

    print(sublist)
    if line[0] in b_type:
        if line[0] == 'blt':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('100')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            

        if line[0] == 'beq':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('000')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            print(imm[1:7])

        if line[0] == 'bne':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('001')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            print(imm[1:7])
        
        if line[0] == 'bge':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('101')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            print(imm[1:7])
                
        if line[0] == 'bltu':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[2]),12)
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('110')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            print(imm[1:7])

        if line[0] == 'bgeu':
            sublist = list(line[1].split(','))
            rs2 = sublist[1]
            rs1 = sublist[0]
            imm = inttob(int(sublist[0]),12)
            j.write(imm[0])
            j.write(imm[1:7])
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('111')
            j.write(imm[7:11])
            j.write(imm[1])
            j.write('1100011\n')
            print(imm[1:7])
    line = f.readline()

f.close()
j.close()