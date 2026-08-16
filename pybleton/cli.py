import sys
from fastmcp import FastMCP
from .mcp.server import mcp
from .installer import install_remote_script, configure_claude

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "mcp":
            mcp.run()
        elif cmd == "install":
            install_remote_script()
        elif cmd == "configure-claude":
            configure_claude()
        else:
            print("Usage: pybleton [mcp|install|configure-claude]")
            sys.exit(1)
    else:
        print("Usage: pybleton [mcp|install|configure-claude]")
        sys.exit(1)

if __name__ == "__main__":
    main()
