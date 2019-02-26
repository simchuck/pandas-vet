import ast

from pandas_vet import VetPlugin

def AST_explorer(statement):
    """
    Return the AST node attribute corresponding to the code statement.


    """
    tree = ast.parse(statement)
    ### need to parse appropriate substring of interest from the statement ???
    result = list(VetPlugin(tree))
    ### I think I want to recurse through the statement to and check the `type` on each recursion until it returns a string ???
    ### then return this string as the attribute of interest
    ### How can we distinguish between a function or method call, a built-in (or keyword?) statement, or other node types ???
    return attribute
