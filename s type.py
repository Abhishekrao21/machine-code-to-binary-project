f = open('read.txt', 'r')
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
    
def sinttob(n, size):
    if n >= 0:
        binary = ""
        q = n
        while q != 0:
            rem = q % 2
            q = q // 2
            binary = str(rem) + binary
        while len(binary) != size:
            binary = '0' + binary
        return binary
    else:
        n = (2 ** size) + n
        binary = ""
        q = n
        while q != 0:
            rem = q % 2
            q = q // 2
            binary = str(rem) + binary
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
    abi_mapping=

    line = list(line.split(" "))
    sublist = list(line[1].split(','))   #make sublist inside the 
    print(line)
    s_type = ['lw', 'addi', 'stliu', 'jalr']
    if line[0] in s_type:
        if line[0] == 'lw':
            rd = sublist[0]
            print(sublist)
            
            
            k = 0  # Corrected the index
            for i in sublist[1]:
                k+=1
                if (i == '('):
                    break
            imm = inttob(int(sublist[1][0:k-1]),11)   # error when imm out of range 
            rs = sublist[1][k:-2]      #error
            print(sublist[1][0:k-1])
            print(rs)
            j.write(imm)
            j.write(registers[rs])
            j.write('010')
            j.write(registers[rd])
            j.write('0000011\n')  # Corrected the index
            
        if line[0] == 'addi':
            rd = sublist[0]
            rs = sublist[1]
            imm = inttob(int(sublist[2]),11)
            j.write(imm)
            j.write(registers[rs])
            j.write('000')
            j.write(registers[rd])
            j.write('0010011\n')

        if line[0] == 'stliu':
            rd = sublist[0]
            rs = line[1]
            imm = inttob(int(sublist[2]),11)
            j.write(imm)
            j.write(registers[rs])
            j.write('011')
            j.write(registers[rd])
            j.write('0010011\n')

        if line[0] == 'jalr':
            rd = sublist[0]
            rs = sublist[1]
            imm = sinttob(int(sublist[2]),11)
            
            j.write(imm)
            j.write(registers[rs])
            j.write('010')
            j.write(registers[rd])
            j.write('0000011\n')


            
    line = f.readline()  # Corrected the function call

f.close()
j.close()
