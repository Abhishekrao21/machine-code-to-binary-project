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
    'zero': '00000','ra': '00001','sp': '00010','gp': '00011','t0': '00100',
    't1': '00101','s0': '00110','fp':'00110','s1': '00111','a0': '01000',
    'a1': '01001','a2': '01010','a3': '01011','a4': '01100','a5': '01101',
    'a6': '01110','a7': '01111','s2': '10000','s3': '10001','s4': '10010',
    's5': '10011','s6': '10100','s7': '10101','s8': '10110','s9': '10111',
    's10': '11000','s11': '11001','t3': '11010','t4': '11011','t5': '11100',
    't6': '11101','t7': '11110','t8': '11111',
    }

    line = list(line.split(" "))
    print(line)
    R_type = ['add', 'sub', 'sll', 'slt', 'sltu', 'xor', 'srl', 'or', 'and']
    
    if line[0] in R_type:
        if line[0] =='add':
            subline=list(line[1].split(","))
            rd = subline[0]
            rs1 = subline[1]
            rs2 = subline[2]
            j.write('0000000')
            j.write(registers[rs2])
            j.write(registers[rs1])
            j.write('000')
            j.write(registers[rd])
            j.write('0110011')
            j.write('\n')
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
if Visual_Halt==False:
    print('Error: visual halt not found')
# Close the files after processing
f.close()
j.close()
