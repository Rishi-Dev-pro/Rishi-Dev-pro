import os

os.makedirs('assets/README-decorative/timeline', exist_ok=True)

for i in range(1, 9):
    num = f"{i:02d}"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 260" width="80" height="260" role="img" aria-label="Timeline Node {num}">
  <title>Project {num} Node</title>
  <defs>
    <radialGradient id="tn-glow-{num}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#00F0FF" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#00F0FF" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="tn-line-{num}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#EC4899" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="tn-border-{num}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#8B5CF6" />
    </linearGradient>
    <filter id="glow-filter-{num}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Continuous vertical glowing line -->
  <line x1="40" y1="0" x2="40" y2="260" stroke="url(#tn-line-{num})" stroke-width="4" filter="url(#glow-filter-{num})" />
  <line x1="40" y1="0" x2="40" y2="260" stroke="#FFFFFF" stroke-width="1" stroke-opacity="0.7" />

  <!-- Outer Luminous Aura (diameter ~64px) -->
  <circle cx="40" cy="130" r="38" fill="url(#tn-glow-{num})" />

  <!-- Outer Border Ring (60px diameter) -->
  <circle cx="40" cy="130" r="30" fill="#070B16" stroke="url(#tn-border-{num})" stroke-width="2.5" filter="url(#glow-filter-{num})" />

  <!-- Inner Subtle Ring -->
  <circle cx="40" cy="130" r="24" fill="#0A0F1D" stroke="#00F0FF" stroke-width="1" stroke-opacity="0.35" />

  <!-- Bold Number Display -->
  <text x="40" y="136" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">{num}</text>
</svg>"""
    with open(f'assets/README-decorative/timeline/timeline-node-{num}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

print("Regenerated all 8 timeline nodes with 60px diameter and glowing spines!")
