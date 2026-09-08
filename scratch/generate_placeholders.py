import os

projects = [
    ('project-01.svg', 'Aether-OS', 'AI-Powered Operating System', 'PROJECT_SCREENSHOT_01', '#00f0ff', '#3b82f6'),
    ('project-02.svg', 'Callbuddy-AI', 'Real-Time AI Voice Assistant', 'PROJECT_SCREENSHOT_02', '#3b82f6', '#8b5cf6'),
    ('project-03.svg', 'Mochi', 'AI Companion & Smart Assistant', 'PROJECT_SCREENSHOT_03', '#ec4899', '#8b5cf6'),
    ('project-04.svg', 'VN-media', 'Social Media & Content Platform', 'PROJECT_SCREENSHOT_04', '#00f0ff', '#10b981'),
    ('project-05.svg', 'S-PPT-maker', 'AI-Powered Presentation Generator', 'PROJECT_SCREENSHOT_05', '#f59e0b', '#3b82f6'),
    ('project-06.svg', 'pirate-civ', 'Procedural Strategy & Simulation Game', 'PROJECT_SCREENSHOT_06', '#10b981', '#00f0ff'),
    ('project-07.svg', 'Rishi-cosmic-protfolio', 'Immersive 3D Space Portfolio', 'PROJECT_SCREENSHOT_07', '#a855f7', '#00f0ff'),
    ('project-08.svg', 'The-Four-Pillars', 'Interactive 3D Architectural Showcase', 'PROJECT_SCREENSHOT_08', '#38bdf8', '#c084fc')
]

os.makedirs('assets/placeholders', exist_ok=True)

for fname, title, category, placeholder_id, c1, c2 in projects:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-{placeholder_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080a12" />
      <stop offset="50%" stop-color="#0e1526" />
      <stop offset="100%" stop-color="#060810" />
    </linearGradient>
    <linearGradient id="border-{placeholder_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.6" />
      <stop offset="50%" stop-color="{c2}" stop-opacity="0.3" />
      <stop offset="100%" stop-color="{c1}" stop-opacity="0.5" />
    </linearGradient>
    <radialGradient id="glow-{placeholder_id}" cx="65%" cy="45%" r="50%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.2" />
      <stop offset="100%" stop-color="{c1}" stop-opacity="0" />
    </radialGradient>
    <pattern id="grid-{placeholder_id}" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#1e293b" stroke-width="0.8" opacity="0.4" />
    </pattern>
  </defs>

  <rect width="800" height="450" rx="14" fill="url(#bg-{placeholder_id})" />
  <rect width="800" height="450" rx="14" fill="url(#grid-{placeholder_id})" />
  <rect width="800" height="450" rx="14" fill="url(#glow-{placeholder_id})" />
  <rect width="800" height="450" rx="14" fill="none" stroke="url(#border-{placeholder_id})" stroke-width="1.5" />

  <!-- Window Header -->
  <circle cx="28" cy="24" r="5" fill="#ef4444" opacity="0.7" />
  <circle cx="44" cy="24" r="5" fill="#f59e0b" opacity="0.7" />
  <circle cx="60" cy="24" r="5" fill="#10b981" opacity="0.7" />
  <text x="82" y="28" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b">project // {title.lower()}</text>

  <!-- Futuristic Tech Wireframe Card Preview -->
  <g transform="translate(460, 120)">
    <rect x="0" y="0" width="280" height="190" rx="10" fill="#0b0f19" fill-opacity="0.8" stroke="{c2}" stroke-width="1" />
    <!-- HUD Lines -->
    <path d="M 20 40 L 90 40 L 120 70 L 260 70" fill="none" stroke="{c1}" stroke-width="1.5" opacity="0.7" />
    <circle cx="20" cy="40" r="3" fill="{c1}" />
    <circle cx="120" cy="70" r="3" fill="{c2}" />
    <circle cx="260" cy="70" r="3" fill="{c1}" />
    
    <rect x="25" y="95" width="130" height="10" rx="4" fill="#1e293b" />
    <rect x="25" y="115" width="220" height="8" rx="4" fill="#141e30" />
    <rect x="25" y="130" width="180" height="8" rx="4" fill="#141e30" />
    <rect x="25" y="145" width="100" height="8" rx="4" fill="#141e30" />

    <!-- Mini glowing node -->
    <circle cx="220" cy="125" r="22" fill="{c1}" fill-opacity="0.1" stroke="{c1}" stroke-width="1" stroke-dasharray="3 3" />
    <circle cx="220" cy="125" r="8" fill="{c1}" fill-opacity="0.6" />
  </g>

  <!-- Project Info & Identifiable Replacement Badge -->
  <g transform="translate(45, 140)">
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="28" font-weight="700" fill="#f8fafc" letter-spacing="0.5">{title}</text>
    <text x="0" y="62" font-family="'JetBrains Mono', monospace" font-size="13" fill="{c1}">{category}</text>
    
    <rect x="0" y="96" width="300" height="38" rx="8" fill="#070b14" fill-opacity="0.95" stroke="{c1}" stroke-width="1.2" />
    <text x="150" y="120" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="{c1}" text-anchor="middle" letter-spacing="1.5">{placeholder_id}</text>
  </g>
</svg>"""
    with open(f'assets/placeholders/{fname}', 'w', encoding='utf-8') as f:
        f.write(svg)

print("Generated all placeholders successfully!")
