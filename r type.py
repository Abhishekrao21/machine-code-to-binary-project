#so we need 6 different if 1 for r type ,i type ,s type ...
# like this for r type
f = open("/Users/abhishekrao/Documents/vscode/python/read.txt", "r")
j = open("/Users/abhishekrao/Documents/vscode/python/write.txt", "a")

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

    line = list(line.split(" "))
    print(line)
    R_type = ['add', 'sub', 'sll', 'slt', 'sltu', 'xor', 'srl', 'or', 'and']
    
    if line[0] in R_type:
        if line[0] =='add':
            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('000')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='sub':

            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0100000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('000')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='slt':
             
            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('010')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='sltu':
             
            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('011')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='xor': 
             
            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('100')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='sll':

            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('001')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='srl':

            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('101')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='or':

            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('110')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')

        elif line[0]=='and':

            rd = line[1][0:-1]
            rs1 = line[2][0:-1]
            rs2 = line[3][0:-2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('111')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')


    line = f.readline()

# Close the files after processing
f.close()
j.close()
