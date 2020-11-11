# Cheatsheet
*All of these are commands for the Radare2 shell*

To open radare2 , and have it open a binary in debug mode, use command:

`$ r2 -d vuln_binary`

### Help
Simply type `?`

Radare2 commands use abbreviations for commands, where each alphabet progressively says the category into which the command fits. As an example, `i` command shows the basic **i**nfo of the binary, and `ii` shows basic **i**nfo about the **i**mports.

To see a list of all available commands under one category, append a `?` after the category's representative alphabet. For example, to get all commands that comes under 'show info' category, run `i?`

### Gathering information
    a[aa] – Analyze the binary
    i – Program binary info
    ii – Imports
    il — Linked libraries    
    ie — Get address of Entrypoint
    iS — Show sections with permissions (r/x/w)
    ? \<some value> — Decodes the value in all possible forms, so that you can find out if it corresponds to something meaningful.
    pdf @ addr — Print the assembly of a function in the given offset
    ?v sym.imp.func_name — Get address of func_name@PLT
    ?v reloc.func_name — Get address of func_name@GOT
    pxl n addr – Print hex dump for 'n' lines from address 'addr'

### Memory
    dm — Show memory maps
    dmm — List modules (libraries, binaries loaded in memory)
    dmi [addr|libname] [symname] — List symbols of target lib
    dr [reg] — Look at contents of a register.

### Searching
    e search.* — Edit searching configuration
    *[To search in all memory locations, use `e search.in = dbg.maps`]*
    /? — List search subcommands
    / string — Search string in memory/binary
    /R [?] — Search for ROP gadgets
    /R/ — Search for ROP gadgets with a regular expressions

### Debugging
    dc — Continue execution
    dcu addr – Continue execution until address
    dcr — Continue until ret (uses step over)
    dbt [?] — Display backtrace based on dbg.btdepth and dbg.btalgo
    doo [args] — Reopen in debugger mode with args
    ds — Step one instruction
    dso — Step over

### Visual Modes    
    V — Visual mode, use p/P to toggle between different modes
    VV — Visual Graph mode, navigating through ASCII graphs
    V! — Visual panels mode. Very useful for exploitation

### Miscellaneous
    eco <theme name> — Changes the terminal theme

