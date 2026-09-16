import random
from fastmcp import FastMCP
mcp = FastMCP(name="BASIC_SERVER")
@mcp.tool
def add (a : int, b : int) -> int :
    "TAKES TWO NUMBERS AND ADDS TWO NUMBERS"
    return a +  b
def subtract(a:int, b : int) -> int :
    "Takes two numbers and subtracts two numbers"
    return a - b
if __name__ =="__main__":
    mcp.run()