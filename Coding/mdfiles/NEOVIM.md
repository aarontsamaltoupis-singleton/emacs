# keymaps
gd: go to definition

]n [n 

0: go to start of line 	

**commenting out multiple lines**:
- Ctrl -v to block select
- select the desired lines
- shift-I, insert #
- escape

## luasnip

Ctrl l to jump forward



# commands
:Mason to see all installed and available lsps
:TSInstall {language}

# vimwiki
- <C-x><C-f>
	- complete links
	
# Markdown Preview
- <leader>mp

# Vimtex
\lc to clear auxiliary files
dse
	- to delete surrounding environment
cse 
	- change environment

dsc
	- delete latex command, while preserving arguments
dsd
	- delte delimiter (e.g. (), []) 
	  
csd
	- change delimiter (and \left\right, etc variants)
	- preserves \left\right modifiers
tsd
	- toggle delimiter \right{\left}

ds$
	- delte suurounding math environment
cs$
	- change suurounding math environment
tsc
	- make environment starred (*) environment
ts$
	- toggle between inline and display math
tsf
	- toggle between a/b and \frac{a}{b}
[[

	  
# luasnip
- advanced snippets
- store_selection_keys = "<Tab>",
pressing <Tab> in visual mode will store the selected text in luaSnip variable
