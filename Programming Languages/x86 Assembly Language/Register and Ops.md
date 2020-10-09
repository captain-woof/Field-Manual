# Registers and Ops

### Available registers:
- General Purpose:
  **EAX, EBX, ECX, EDX**
- Reserved:
  **ESP** (stack head pointer), **EIP** (pointer to address of next instruction), **EBP** (stack base pointer)

  **NOTE: All registers are 4 bytes (32-bits) in size**

### Operations:
  - ADD:
  `add eax, ebx ; eax+=ebx`
  - SUB:
  `sub eax, ecx ; eax-=ecx`
  - MUL:
  `mul ebx; eax*=ebx (lower half of product) and edx*=ebx (higher half of the product)`
  - DIV:
  `div ecx; eax/=ecx and edx=remainder`
  - INC:
  `inc eax; eax+=1`
  - DEC:
  `dec eax; eax-=1`
  -----------------  
  - `int 0x80 ; interrupts and makes system calls, eax holds the code for which system function`
  ---------
  - `jmp addr ; Unconditional jump to addr`
  - `cmp ebx, 40 ; Compares ebx with 40, sets the appropriate result flags in flag registers`
  - `je addr ; if previous comparison was set equals flag, execution jumps to addr`
  - `jne addr ; Jump if not equal to`
  - `jg addr ; Jump if greater than`
  - `jge addr ; Jump if greater than or equal to`
  - `jl addr ; Jump if less than`
  - `jle addr ; Jump if less than or equal to`
  ----------------------
  - `call func ; pushes current eip to stack, then jumps to func address`
  - `ret ; returns from function to the previous function by moving the previous function's eip value (that was pushed on stack) back to eip, thus, transferring control to the previous function.`
