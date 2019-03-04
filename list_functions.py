import ast

class FuncLister(ast.NodeVisitor):
    #fxns = []
    def visit_FunctionDef(self, node):
        #fxns.append(node.name)
        print(node.name)
        self.generic_visit(node)


with open('astpp.py', 'r') as f:
    code = f.read()

tree = ast.parse(code)
FuncLister().visit(tree)


# Using the `.walk()` method will also work, but order is not guaranteed.
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(node.name)


# Additionally, we can use the `.iter_child_nodes()` method, which will iterate 
# through all child nodes of the specified parent.  

# `ast.iter_fields()`
# `ast.get_docstring()`
# `ast.dump()`


# Following will rewrite name lookups, so `foo` becomes `data['foo']`
class RewriteName(ast.NodeTransformer):

    def visit_Name(self, node):
        return ast.copy_location(ast.Subscript(
            value=ast.Name(id='data', ctx=axt.Load()),
            slice=ast.Index(value=ast.Str(s=node.id)),
            ctx=node.ctx
            ), node)

tree = RewriteName().visit(tree)


# Each node must have `lineno` and `col_offset` attributes in order to compile.  For nodes
# that are created programmatically, you need to set these attributes.
# `ast.fix_missing_locations()` will recursively fill any missing locations by copying from the parent node.
# `ast.copy_location()` will copy the `lineno` and `col_offset` values from one node to another.  
# `ast.increment_lineno()` will increment the `lineno` for a node and its children.

