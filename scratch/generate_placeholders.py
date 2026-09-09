import os

projects = [
    (
        'project-01.svg', 'AETHER OS', 'AI-Powered Operating System', 'PROJECT_SCREENSHOT_01', 
        '#00F0FF', '#3B82F6', '#8B5CF6',
        'Spatial AI Browser HUD • Voice & Vision Integration • Neural Reticle'
    ),
    (
        'project-02.svg', 'CallBuddy AI', 'Real-Time AI Voice Assistant', 'PROJECT_SCREENSHOT_02', 
        '#38BDF8', '#818CF8', '#C084FC',
        'Real-Time WebRTC Audio • Neural Speech Pipeline • Active Turn-Taking'
    ),
    (
        'project-03.svg', 'The Four Pillars', 'Interactive 3D Showcase', 'PROJECT_SCREENSHOT_03', 
        '#38BDF8', '#C084FC', '#3B82F6',
        'Creative Engineering Showcase • 60FPS Glassmorphism • Design Tokens'
    ),
    (
        'project-04.svg', 'VN Media', 'Social Media & Content Platform', 'PROJECT_SCREENSHOT_04', 
        '#00F0FF', '#10B981', '#3B82F6',
        'Full-Stack Content Feeds • Real-Time Websockets • Interactive Media'
    ),
    (
        'project-05.svg', 'Pirate Civ', 'Pirate-Themed E-Commerce Website', 'PROJECT_SCREENSHOT_05', 
        '#F59E0B', '#10B981', '#00F0FF',
        'Treasure Loot Store • Custom Skull & Cutlass Theme • Seamless Checkout'
    ),
    (
        'project-06.svg', 'S-PPT Maker', 'Free No-Watermark PowerPoint Maker', 'PROJECT_SCREENSHOT_06', 
        '#F59E0B', '#3B82F6', '#00F0FF',
        'Automated Slide Composition • 100% Free Zero Watermark • Instant PPTX'
    ),
    (
        'project-07.svg', 'Rishi Cosmic Portfolio', 'Galaxy-Themed 3D Portfolio', 'PROJECT_SCREENSHOT_07', 
        '#C084FC', '#00F0FF', '#EC4899',
        'Three.js Particle Galaxy • Dynamic Celestial Shaders • Smooth GSAP'
    ),
    (
        'project-08.svg', 'Mochu', 'AI Girl Companion', 'PROJECT_SCREENSHOT_08', 
        '#EC4899', '#8B5CF6', '#3B82F6',
        'Virtual AI Girl Companion • Emotion Engine • Real-Time Voice Synthesis'
    )
]

os.makedirs('assets/placeholders', exist_ok=True)

for fname, title, category, placeholder_id, c1, c2, c3, subtext in projects:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-{placeholder_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060913" />
      <stop offset="50%" stop-color="#0A1020" />
      <stop offset="100%" stop-color="#05070D" />
    </linearGradient>

    <!-- Neon Rim Border Gradient -->
    <linearGradient id="border-{placeholder_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.8" />
      <stop offset="40%" stop-color="{c2}" stop-opacity="0.3" />
      <stop offset="100%" stop-color="{c3}" stop-opacity="0.7" />
    </linearGradient>

    <!-- Radial Luminous Glow -->
    <radialGradient id="glow-{placeholder_id}" cx="70%" cy="40%" r="55%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.28" />
      <stop offset="50%" stop-color="{c2}" stop-opacity="0.1" />
      <stop offset="100%" stop-color="{c1}" stop-opacity="0" />
    </radialGradient>

    <!-- Cyber Grid Pattern -->
    <pattern id="grid-{placeholder_id}" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#1E293B" stroke-width="0.8" opacity="0.35" />
    </pattern>

    <!-- Filter for Luminous Accents -->
    <filter id="neon-glow-{placeholder_id}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Base Card -->
  <rect width="960" height="540" rx="16" fill="url(#bg-{placeholder_id})" />
  <rect width="960" height="540" rx="16" fill="url(#grid-{placeholder_id})" />
  <rect width="960" height="540" rx="16" fill="url(#glow-{placeholder_id})" />

  <!-- Top Glass Bar with macOS Controls -->
  <rect x="0" y="0" width="960" height="46" rx="16" fill="#0B1120" fill-opacity="0.7" />
  <line x1="0" y1="46" x2="960" y2="46" stroke="#1E293B" stroke-width="1" />
  <circle cx="34" cy="23" r="6" fill="#EF4444" opacity="0.8" />
  <circle cx="54" cy="23" r="6" fill="#F59E0B" opacity="0.8" />
  <circle cx="74" cy="23" r="6" fill="#10B981" opacity="0.8" />
  <text x="100" y="27" font-family="'JetBrains Mono', monospace" font-size="12" fill="#64748B" font-weight="600">system://workspaces/{title.lower().replace(' ', '-')}</text>

  <!-- Futuristic Visual Centerpiece / HUD Graphic -->
  <g transform="translate(540, 100)">
    <!-- Outer Translucent HUD Frame -->
    <rect x="0" y="0" width="360" height="350" rx="14" fill="#080E1C" fill-opacity="0.85" stroke="{c2}" stroke-opacity="0.4" stroke-width="1.2" />
    
    <!-- Reticle Circles & Telemetry -->
    <circle cx="180" cy="160" r="100" fill="none" stroke="{c1}" stroke-width="1" stroke-dasharray="6 8" opacity="0.4" />
    <circle cx="180" cy="160" r="70" fill="none" stroke="{c2}" stroke-width="1.5" stroke-dasharray="14 10" opacity="0.6" />
    <circle cx="180" cy="160" r="40" fill="{c1}" fill-opacity="0.12" stroke="{c1}" stroke-width="2" filter="url(#neon-glow-{placeholder_id})" />
    <circle cx="180" cy="160" r="12" fill="{c1}" opacity="0.85" />

    <!-- Waveform / HUD metrics -->
    <path d="M 40 290 Q 90 260 140 290 T 240 290 T 320 290" fill="none" stroke="{c1}" stroke-width="2" opacity="0.8" />
    <circle cx="140" cy="290" r="3.5" fill="{c1}" />
    <circle cx="240" cy="290" r="3.5" fill="{c3}" />
    
    <!-- Diagnostic Bars -->
    <rect x="40" y="40" width="120" height="6" rx="3" fill="#1E293B" />
    <rect x="40" y="40" width="85" height="6" rx="3" fill="{c1}" opacity="0.8" />
    <rect x="40" y="55" width="180" height="6" rx="3" fill="#1E293B" />
    <rect x="40" y="55" width="130" height="6" rx="3" fill="{c2}" opacity="0.8" />
  </g>

  <!-- Left Side: Large Project Typography & Placeholder Indicator -->
  <g transform="translate(60, 160)">
    <!-- Subtitle category tag -->
    <rect x="0" y="0" width="auto" height="26" rx="6" fill="{c1}" fill-opacity="0.12" />
    <text x="12" y="17" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="{c1}" letter-spacing="1">{category.upper()}</text>

    <!-- Main Project Name -->
    <text x="0" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="36" font-weight="800" fill="#F8FAFC" letter-spacing="-0.5">{title}</text>
    
    <!-- Secondary Features Subtext -->
    <text x="0" y="105" font-family="'JetBrains Mono', monospace" font-size="13" fill="#94A3B8">{subtext}</text>

    <!-- Identifiable Replaceable Badge Pill -->
    <g transform="translate(0, 160)">
      <rect x="0" y="0" width="340" height="46" rx="10" fill="#060A14" fill-opacity="0.95" stroke="{c1}" stroke-width="1.5" filter="url(#neon-glow-{placeholder_id})" />
      <circle cx="24" cy="23" r="5" fill="{c1}" />
      <text x="42" y="28" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="{c1}" letter-spacing="1.5">{placeholder_id}</text>
    </g>
  </g>

  <!-- Outer Neon Border Frame -->
  <rect width="960" height="540" rx="16" fill="none" stroke="url(#border-{placeholder_id})" stroke-width="2" />
</svg>"""
    with open(f'assets/placeholders/{fname}', 'w', encoding='utf-8') as f:
        f.write(svg)

print("Regenerated all 8 screenshot placeholders with cinematic visuals!")
