import ast

with open("webscapy.py") as f:
    source_code =f.read()

tree = ast.parse(source_code)

classes = []
functions = []

def get_classes_and_functions_def():
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

found_classes , found_functions = get_classes_and_functions_def()

for function in found_functions:
    print("Function name:", function["name"])
    print("Arguments:", function["arguments"])
    print("Code:")
    print(function["code"])
    print()




