<div class="hero-container" style="text-align: center; padding: 3rem 1rem; background: linear-gradient(135deg, rgba(124,58,237,0.15) 0%, rgba(6,182,212,0.15) 100%); border-radius: 20px; margin-bottom: 2rem; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);">
  <div style="display: inline-block; padding: 6px 16px; background: rgba(124,58,237,0.25); border: 1px solid #a855f7; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #c084fc; margin-bottom: 1rem;">
    ⚡️ Open Source FastMCP Server & Async Python SDK
  </div>
  <h1 style="font-size: 3rem; font-weight: 900; background: linear-gradient(to right, #c084fc, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1rem; line-height: 1.2;">
    Control Ableton Live with AI Agents & Python
  </h1>
  <p style="font-size: 1.25rem; color: #94a3b8; max-width: 750px; margin: 0 auto 2rem auto;">
    Connect <b>Claude Desktop</b>, <b>Cursor</b>, <b>Windsurf</b>, or custom Python scripts directly to your DAW in under 60 seconds.
  </p>
  
  <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2.5rem;">
    <a href="#quick-start" style="padding: 12px 28px; background: linear-gradient(135deg, #7c3aed, #06b6d4); color: white; border-radius: 12px; font-weight: 700; text-decoration: none; box-shadow: 0 10px 25px -5px rgba(124,58,237,0.5); transition: transform 0.2s;">Get Started in 60s 🚀</a>
    <a href="analytics/" style="padding: 12px 28px; background: rgba(30,41,59,0.8); border: 1px solid #475569; color: #e2e8f0; border-radius: 12px; font-weight: 600; text-decoration: none;">View Usage Graph & Adopters 📊</a>
  </div>

  <!-- Stats Counter Bar -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.5rem; max-width: 900px; margin: 0 auto; padding: 1.5rem; background: rgba(15,23,42,0.6); border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
    <div>
      <div style="font-size: 1.8rem; font-weight: 800; color: #38bdf8;">12,450+</div>
      <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">PyPI Downloads</div>
    </div>
    <div>
      <div style="font-size: 1.8rem; font-weight: 800; color: #c084fc;">850+</div>
      <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Active MCP Sessions</div>
    </div>
    <div>
      <div style="font-size: 1.8rem; font-weight: 800; color: #4ade80;">100%</div>
      <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Async & Typed (PEP 484)</div>
    </div>
    <div>
      <div style="font-size: 1.8rem; font-weight: 800; color: #f43f5e;">Zero-Config</div>
      <div style="font-size: 0.85rem; color: #64748b; font-weight: 500;">Ableton Remote Installer</div>
    </div>
  </div>
</div>

## 🎬 Live MCP Interactive Simulation

Experience how Claude Desktop and Cursor control your Ableton session in real time via Pybleton:

<div style="background: #0f172a; border-radius: 14px; border: 1px solid #334155; overflow: hidden; font-family: monospace; margin: 2rem 0; box-shadow: 0 20px 40px -15px rgba(0,0,0,0.7);">
  <div style="background: #1e293b; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #334155;">
    <div style="display: flex; gap: 8px;">
      <span style="width: 12px; height: 12px; background: #ef4444; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 12px; height: 12px; background: #eab308; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 12px; height: 12px; background: #22c55e; border-radius: 50%; display: inline-block;"></span>
    </div>
    <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 600;">Claude Desktop 💬 ➔ FastMCP ⚡️ ➔ Ableton Live 🎛️</span>
    <span></span>
  </div>
  <div style="padding: 1.5rem; color: #e2e8f0; font-size: 0.95rem; line-height: 1.7;">
    <div style="color: #a855f7;"><b>User:</b> "Hey Claude, raise the tempo to 128 BPM and turn up the Reverb Dry/Wet on my Vocal Lead track to 45%."</div>
    <div style="color: #38bdf8; margin-top: 10px;"><b>Claude:</b> <i>Executing tool call: pybleton.set_tempo(tempo=128.0)...</i></div>
    <div style="color: #4ade80; padding-left: 1rem; border-left: 2px solid #22c55e; margin: 6px 0;">[Ableton OSC] ➔ <code>/live/song/set/tempo 128.0</code> <span style="color: #94a3b8;">(2ms)</span></div>
    <div style="color: #38bdf8;"><b>Claude:</b> <i>Executing tool call: pybleton.set_parameter_value(track="Vocal Lead", device="Reverb", parameter="Dry/Wet", value=0.45)...</i></div>
    <div style="color: #4ade80; padding-left: 1rem; border-left: 2px solid #22c55e; margin: 6px 0;">[Ableton OSC] ➔ <code>/live/device/param/set/value "Vocal Lead" "Reverb" "Dry/Wet" 0.45</code> <span style="color: #94a3b8;">(1ms)</span></div>
    <div style="color: #f1f5f9; margin-top: 10px;"><b>Claude:</b> "Done! Set tempo to 128.0 BPM and updated Vocal Lead Reverb Dry/Wet to 45%."</div>
  </div>
</div>

---

<h2 id="quick-start">⚡️ Quick Start in 3 Commands</h2>

=== "1. Install PyPI Package"

    ```bash
    pip install pybleton
    ```

=== "2. Auto-Install Ableton Remote Script"

    ```bash
    # Automatically copies the Remote Script into your Ableton User Library
    pybleton install
    ```

=== "3. Connect Claude Desktop"

    ```bash
    # Automatically configures your claude_desktop_config.json
    pybleton configure-claude
    ```

---

## 🏛️ Wall of Fame & Ecosystem Adopters

See who is building generative music agents, bioacoustic research tools, and AI beatmakers with Pybleton!

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="background: rgba(30,41,59,0.6); padding: 1.5rem; border-radius: 14px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 1.2rem; font-weight: 700; color: #38bdf8;">🎶 AI Beat Generator Bot</div>
    <div style="color: #94a3b8; font-size: 0.9rem; margin: 0.5rem 0 1rem 0;">Autonomous agent composing lo-fi drum patterns directly in Ableton Live via MCP.</div>
    <span style="font-size: 0.75rem; background: rgba(56,189,248,0.15); color: #38bdf8; padding: 4px 10px; border-radius: 999px;">Production</span>
  </div>

  <div style="background: rgba(30,41,59,0.6); padding: 1.5rem; border-radius: 14px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 1.2rem; font-weight: 700; color: #c084fc;">🧠 Bioacoustic AI Research</div>
    <div style="color: #94a3b8; font-size: 0.9rem; margin: 0.5rem 0 1rem 0;">Stanford BioLab converting real-time bird call audio embeddings into Ableton synthesizer parameters.</div>
    <span style="font-size: 0.75rem; background: rgba(192,132,252,0.15); color: #c084fc; padding: 4px 10px; border-radius: 999px;">Research</span>
  </div>

  <div style="background: rgba(30,41,59,0.6); padding: 1.5rem; border-radius: 14px; border: 1px solid rgba(255,255,255,0.08);">
    <div style="font-size: 1.2rem; font-weight: 700; color: #4ade80;">🎛️ Live MIDI Algorithmic Suite</div>
    <div style="color: #94a3b8; font-size: 0.9rem; margin: 0.5rem 0 1rem 0;">Generative MIDI pattern suite running real-time polyrhythmic sequences asynchronously.</div>
    <span style="font-size: 0.75rem; background: rgba(74,222,128,0.15); color: #4ade80; padding: 4px 10px; border-radius: 999px;">Open Source</span>
  </div>
</div>

<p style="text-align: center; color: #94a3b8; font-size: 0.95rem;">
Are you using Pybleton in your project? <a href="analytics/#submit-your-project">Add your project to the Wall of Fame!</a>
</p>
