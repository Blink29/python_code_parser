import ast

with open("webscapy.py") as f:
    source_code =f.read()

def parse_class(source_code):
    tree = ast.parse(source_code)
    classes = []
    functions = []  
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.FunctionDef): 
            arguments = [arg.arg for arg in node.args.args]
            code = ast.get_source_segment(source_code, node)
            functions.append({
            "name": node.name,
            "arguments": arguments,
            "code": code 
            })

    return classes, functions

found_classes , found_functions = parse_class()

for function in found_functions:
    print("Function name:", function["name"])
    print("Arguments:", function["arguments"])
    print("Code:")
    print(function["code"])
    print()




