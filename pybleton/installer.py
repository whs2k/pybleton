import os
import sys
import shutil
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def get_ableton_remote_scripts_path() -> Path:
    """Find the Ableton Live Remote Scripts folder based on OS."""
    if sys.platform == "darwin":
        return Path.home() / "Music" / "Ableton" / "User Library" / "Remote Scripts"
    elif sys.platform == "win32":
        return Path.home() / "Documents" / "Ableton" / "User Library" / "Remote Scripts"
    else:
        raise OSError("Unsupported operating system for Ableton Live.")

def get_claude_desktop_config_path() -> Path:
    """Find the Claude Desktop config file based on OS."""
    if sys.platform == "darwin":
        return Path("~/Library/Application Support/Claude/claude_desktop_config.json").expanduser()
    elif sys.platform == "win32":
        return Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json"
    else:
        raise OSError("Unsupported operating system for Claude Desktop.")

def install_remote_script():
    """Install the Pybleton Remote Script into Ableton's User Library."""
    print("🚀 Installing Pybleton Remote Script for Ableton Live...")
    try:
        dest_dir = get_ableton_remote_scripts_path() / "Pybleton"
        dest_dir.mkdir(parents=True, exist_ok=True)
        
        # In a real package, we would use importlib.resources to find the bundled script
        # For now, we mock the copy operation
        src_dir = Path(__file__).parent / "remote_script"
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
            print(f"✅ Successfully installed Remote Script to {dest_dir}")
            print("👉 Next: Open Ableton Live -> Preferences -> Link/Tempo/MIDI -> Select 'Pybleton' as a Control Surface.")
        else:
            print("❌ Source remote_script directory not found.")
    except Exception as e:
        print(f"❌ Failed to install Remote Script: {e}")

def configure_claude():
    """Inject Pybleton MCP server into Claude Desktop config."""
    print("🤖 Configuring Claude Desktop to use Pybleton...")
    try:
        config_path = get_claude_desktop_config_path()
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        if config_path.exists():
            with open(config_path, "r") as f:
                config = json.load(f)
        else:
            config = {"mcpServers": {}}
            
        if "mcpServers" not in config:
            config["mcpServers"] = {}
            
        # We need to find the uvx executable path. Assuming it's in PATH.
        config["mcpServers"]["pybleton"] = {
            "command": "uvx",
            "args": ["pybleton", "mcp"]
        }
        
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
            
        print(f"✅ Successfully configured Claude Desktop at {config_path}")
        print("👉 Next: Restart Claude Desktop to start controlling Ableton Live!")
    except Exception as e:
        print(f"❌ Failed to configure Claude Desktop: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "install":
            install_remote_script()
        elif sys.argv[1] == "configure-claude":
            configure_claude()
