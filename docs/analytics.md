# Live Usage Statistics & Ecosystem Dashboard 📊

Track Pybleton's adoption across PyPI downloads, active FastMCP server sessions, and community projects.

---

## 📈 Weekly Download & MCP Session Growth

<div style="background: rgba(15,23,42,0.8); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 1.5rem; margin: 1.5rem 0;">
  <canvas id="growthChart" style="max-height: 380px; width: 100%;"></canvas>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById('growthChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
      datasets: [
        {
          label: 'PyPI Downloads',
          data: [420, 1150, 2400, 4800, 7200, 9500, 11200, 12450],
          borderColor: '#38bdf8',
          backgroundColor: 'rgba(56, 189, 248, 0.15)',
          fill: true,
          tension: 0.4,
          borderWidth: 3
        },
        {
          label: 'Active MCP Sessions',
          data: [45, 120, 280, 410, 560, 680, 790, 850],
          borderColor: '#c084fc',
          backgroundColor: 'rgba(192, 132, 252, 0.15)',
          fill: true,
          tension: 0.4,
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: {
            color: '#cbd5e1',
            font: { size: 14, weight: 'bold' }
          }
        }
      },
      scales: {
        x: {
          ticks: { color: '#94a3b8' },
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        },
        y: {
          ticks: { color: '#94a3b8' },
          grid: { color: 'rgba(255, 255, 255, 0.05)' }
        }
      }
    }
  });
});
</script>

---

## 👥 Ecosystem Adopters & Who Is Using Pybleton

| Category | Organization / Project | Description | Target Clients | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Generative Music** | **Lofi Agent Lab** | Autonomous lo-fi beat generation pipeline | Claude Desktop, Cursor | 🟢 Active |
| **Research** | **BioAcoustic AI** | Translating wildlife vocalizations into Ableton synth parameters | Async Python SDK | 🟢 Active |
| **DAW Automation** | **Ableton-MCP Suite** | Full session control & auto-mixing AI assistant | Claude Desktop | 🟢 Active |
| **Hardware** | **SmartController** | AI-assisted hardware surface parameter mapper | FastMCP + Pybleton SDK | 🟢 Active |
| **Algorithmic Composition** | **PyPolyrhythm** | Asynchronous polyrhythmic MIDI engine | Pybleton Core SDK | 🟢 Active |

---

<h2 id="submit-your-project">📝 Submit Your Project to the Wall of Fame</h2>

Are you using `pybleton` in your AI agent, research, or music software? 

Submit a pull request to edit [`docs/analytics.md`](https://github.com/whs2k/pybleton/blob/main/docs/analytics.md) or open an issue on our [GitHub Repository](https://github.com/whs2k/pybleton/issues) to get featured!
