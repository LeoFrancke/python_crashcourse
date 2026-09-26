import printing_functions as pf

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot arm', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.display_models(completed_models)

