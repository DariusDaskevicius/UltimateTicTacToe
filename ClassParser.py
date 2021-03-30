import ast

def fillClassList(file = 'main.py'):
    classList = []
    className = None
    mehotdName = None
    fileName = file
    fileObject = open(fileName,"r")
    text = fileObject.read()
    p = ast.parse(text)
    node = ast.NodeVisitor()
    methodName = None
    className = None
    for node in ast.walk(p):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            if isinstance(node, ast.ClassDef):
                className = node.name
            else:
                methodName = node.name
            if className != None and methodName != None:
                subList = (methodName , className)
                classList.append(subList)
    return classList

print(fillClassList())