import os

os.makedirs('assets/profile-svgs', exist_ok=True)

# ════════════════════════════════════════════════════════════════
# 1. HEADER NAV SVG (1200 x 64)
# ════════════════════════════════════════════════════════════════
header_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 64" width="100%" height="64">
  <defs>
    <linearGradient id="nav-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.4" />
    </linearGradient>
    <filter id="cyan-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Nav Pill Container -->
  <rect x="2" y="2" width="1196" height="60" rx="30" fill="#080D1A" fill-opacity="0.85" stroke="url(#nav-border)" stroke-width="1.5" />

  <!-- Left: Terminal Prompt -->
  <g transform="translate(36, 37)">
    <text font-family="'JetBrains Mono', monospace, sans-serif" font-size="16" font-weight="700" fill="#00F0FF" filter="url(#cyan-glow)">Rishi@github:~$</text>
  </g>

  <!-- Center: Nav Items -->
  <g transform="translate(420, 20)">
    <!-- Active 'Home' Pill -->
    <rect x="0" y="0" width="76" height="32" rx="16" fill="#38BDF8" fill-opacity="0.18" stroke="#38BDF8" stroke-opacity="0.6" stroke-width="1.2" />
    <text x="38" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8" text-anchor="middle">Home</text>
    
    <!-- Other Nav Items -->
    <text x="120" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94A3B8">About</text>
    <text x="195" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94A3B8">Projects</text>
    <text x="285" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94A3B8">Tech Stack</text>
    <text x="385" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94A3B8">Stats</text>
    <text x="455" y="21" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="500" fill="#94A3B8">Contact</text>
  </g>

  <!-- Right: Let's Connect Button -->
  <g transform="translate(1030, 14)">
    <rect x="0" y="0" width="134" height="36" rx="18" fill="#8B5CF6" fill-opacity="0.22" stroke="#A855F7" stroke-width="1.4" />
    <!-- Paper Airplane Icon -->
    <path d="M 22 18 L 14 14 L 30 9 L 26 25 L 20 20 L 20 25 Z" fill="none" stroke="#C084FC" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" />
    <text x="40" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="600" fill="#C084FC">Let's Connect</text>
  </g>
</svg>"""

with open('assets/profile-svgs/header-nav.svg', 'w', encoding='utf-8') as f:
    f.write(header_svg)


# ════════════════════════════════════════════════════════════════
# 2. HERO SECTION SVG (1200 x 360)
# ════════════════════════════════════════════════════════════════
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="360">
  <defs>
    <!-- Cyan / Purple Halo Ring Gradient -->
    <linearGradient id="halo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="40%" stop-color="#3B82F6" />
      <stop offset="80%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>

    <!-- Name Gradient -->
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <!-- Card Background & Border -->
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.35" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.3" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="hero-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="avatar-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <clipPath id="avatar-clip">
      <circle cx="110" cy="130" r="75" />
    </clipPath>
  </defs>

  <!-- ── Left: Profile Avatar ── -->
  <g>
    <!-- Outer Luminous Ring -->
    <circle cx="110" cy="130" r="82" fill="none" stroke="url(#halo-grad)" stroke-width="3.5" filter="url(#avatar-glow)" />
    <circle cx="110" cy="130" r="78" fill="#0A0F1E" />

    <!-- Sunset Silhouette Inside Avatar -->
    <g clip-path="url(#avatar-clip)">
      <!-- Twilight Sky Gradient -->
      <rect x="30" y="50" width="160" height="160" fill="#1E293B" />
      <!-- Horizon Warm Gradient -->
      <path d="M 30 150 Q 110 135 190 150 L 190 210 L 30 210 Z" fill="#F97316" fill-opacity="0.45" />
      <path d="M 30 165 Q 110 150 190 165 L 190 210 L 30 210 Z" fill="#E11D48" fill-opacity="0.4" />
      <!-- Silhouette Person -->
      <path d="M 110 95 C 98 95 90 105 90 120 C 90 132 98 140 108 143 C 95 148 75 155 70 200 L 150 200 C 145 155 125 148 112 143 C 122 140 130 132 130 120 C 130 105 122 95 110 95 Z" fill="#060911" />
      <!-- Soft Cyan Rim Light -->
      <path d="M 98 100 Q 110 96 122 100" stroke="#00F0FF" stroke-width="2" fill="none" opacity="0.8" />
    </g>

    <!-- Available for Opportunities Status Pill -->
    <g transform="translate(25, 235)">
      <rect x="0" y="0" width="170" height="28" rx="14" fill="#090E1B" stroke="#334155" stroke-width="1.2" />
      <circle cx="16" cy="14" r="4.5" fill="#10B981" filter="url(#hero-glow)" />
      <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600" fill="#94A3B8">Available for opportunities</text>
    </g>
  </g>

  <!-- ── Center: Hero Text & Actions ── -->
  <g transform="translate(240, 50)">
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="500" fill="#94A3B8">Hi, I'm</text>
    
    <!-- Big Name -->
    <text x="0" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="56" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Rishi <tspan fill="url(#name-grad)">Shaw</tspan></text>
    
    <!-- Subtitle Role -->
    <text x="0" y="116" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15.5" font-weight="600" fill="#94A3B8" letter-spacing="0.3">AI Engineer &nbsp;•&nbsp; Full Stack Developer &nbsp;•&nbsp; Computer Vision Developer</text>

    <!-- Bio paragraph (multiline) -->
    <text x="0" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8" line-height="1.6">
      <tspan x="0" dy="0">Building useful AI products, scalable web applications, and</tspan>
      <tspan x="0" dy="22">computer vision solutions. I enjoy turning ideas into real-world</tspan>
      <tspan x="0" dy="22">systems that create impact.</tspan>
    </text>

    <!-- Action Buttons -->
    <g transform="translate(0, 225)">
      <!-- View My Work Button -->
      <rect x="0" y="0" width="165" height="44" rx="12" fill="#6366F1" stroke="#818CF8" stroke-width="1.2" filter="url(#hero-glow)" />
      <!-- Octocat Icon -->
      <path d="M 28 22 C 28 17 32 13 37 13 C 42 13 46 17 46 22 C 46 26 43 29 40 30 C 40 29 40 28 40 27 C 37 28 36 26 36 26 C 35 24 34 24 34 24 C 33 23 34 23 34 23 C 35 23 36 25 36 25 C 37 27 39 26 40 25 C 40 24 41 23 41 23 C 39 23 36 22 36 18 C 36 17 37 16 37 15 C 37 15 37 14 37 13 C 37 13 38 13 40 14 C 41 14 42 14 43 14 C 44 14 45 14 46 14 C 48 13 49 13 49 13 C 49 14 49 15 49 15 C 49 16 50 17 50 18 C 50 22 47 23 45 23 C 45 23 46 24 46 25 C 46 27 46 29 46 30 C 43 29 40 26 40 22 Z" fill="#FFFFFF" transform="translate(-10, -5)" />
      <text x="64" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#FFFFFF">View My Work</text>

      <!-- Contact Me Button -->
      <g transform="translate(180, 0)">
        <rect x="0" y="0" width="150" height="44" rx="12" fill="#0B1120" stroke="#334155" stroke-width="1.2" />
        <!-- Mail Icon -->
        <rect x="22" y="14" width="18" height="14" rx="2" fill="none" stroke="#CBD5E1" stroke-width="1.6" />
        <path d="M 22 15 L 31 22 L 40 15" fill="none" stroke="#CBD5E1" stroke-width="1.6" />
        <text x="50" y="27" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#F8FAFC">Contact Me</text>
      </g>
    </g>
  </g>

  <!-- ── Right: Quote & Stats Card ── -->
  <g transform="translate(740, 25)">
    <!-- Card Frame -->
    <rect x="0" y="0" width="440" height="300" rx="18" fill="#0B1122" fill-opacity="0.85" stroke="url(#card-border)" stroke-width="1.5" />
    
    <!-- Quote Icon -->
    <text x="32" y="55" font-family="serif" font-size="44" fill="#38BDF8" filter="url(#hero-glow)">“</text>
    
    <!-- Quote Body -->
    <text x="62" y="50" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" fill="#E2E8F0" line-height="1.5">
      <tspan x="62" dy="0">Engineering is not just</tspan>
      <tspan x="62" dy="24">about writing code, it's about</tspan>
      <tspan x="62" dy="24">solving real problems.</tspan>
    </text>
    <text x="390" y="130" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#64748B" text-anchor="end">— Rishi Shaw</text>

    <!-- Divider Line -->
    <line x1="32" y1="160" x2="408" y2="160" stroke="#1E293B" stroke-width="1.2" />

    <!-- 3 Metrics Columns -->
    <g transform="translate(32, 185)">
      <!-- 8+ Projects -->
      <text x="50" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="800" fill="#38BDF8" text-anchor="middle" filter="url(#hero-glow)">8+</text>
      <text x="50" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Projects</text>

      <!-- 3+ Tech Domains -->
      <text x="188" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="800" fill="#38BDF8" text-anchor="middle" filter="url(#hero-glow)">3+</text>
      <text x="188" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Tech Domains</text>

      <!-- ∞ Learning -->
      <text x="326" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="38" font-weight="800" fill="#C084FC" text-anchor="middle" filter="url(#hero-glow)">∞</text>
      <text x="326" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Learning</text>
    </g>
  </g>
</svg>"""

with open('assets/profile-svgs/hero-section.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)


# ════════════════════════════════════════════════════════════════
# 3. ABOUT ME SECTION SVG (1200 x 230)
# ════════════════════════════════════════════════════════════════
about_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="100%" height="230">
  <defs>
    <linearGradient id="about-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.35" />
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0.3" />
    </linearGradient>
    <linearGradient id="sig-glow-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>
    <filter id="sig-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Large Glass Card Container -->
  <rect x="2" y="2" width="1196" height="226" rx="20" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#about-border)" stroke-width="1.5" />

  <!-- Header: Purple Icon + Title -->
  <g transform="translate(36, 26)">
    <rect x="0" y="0" width="34" height="34" rx="8" fill="#8B5CF6" fill-opacity="0.2" stroke="#A855F7" stroke-width="1.2" />
    <!-- User Icon -->
    <path d="M 17 10 C 14.5 10 12.5 12 12.5 14.5 C 12.5 17 14.5 19 17 19 C 19.5 19 21.5 17 21.5 14.5 C 21.5 12 19.5 10 17 10 Z M 10 25 C 10 21.5 13 20 17 20 C 21 20 24 21.5 24 25 Z" fill="#C084FC" />
    <text x="46" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="700" fill="#FFFFFF">About Me</text>
  </g>

  <!-- Left: Bio Text -->
  <g transform="translate(36, 75)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#94A3B8" line-height="1.7">
      <tspan x="0" dy="0">I am a Computer Science enthusiast passionate about Artificial Intelligence,</tspan>
      <tspan x="0" dy="24">Computer Vision, and Full Stack Development. I love exploring new technologies,</tspan>
      <tspan x="0" dy="24">building projects, and continuously learning. My goal is to create intelligent systems</tspan>
      <tspan x="0" dy="24">that are practical, scalable, and impactful.</tspan>
    </text>

    <!-- Bottom Metadata Pills -->
    <g transform="translate(0, 105)">
      <!-- India -->
      <g>
        <path d="M 8 0 C 4.5 0 2 2.5 2 6 C 2 10.5 8 15 8 15 C 8 15 14 10.5 14 6 C 14 2.5 11.5 0 8 0 Z" fill="none" stroke="#38BDF8" stroke-width="1.3" />
        <circle cx="8" cy="6" r="1.5" fill="#38BDF8" />
        <text x="20" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#CBD5E1">India</text>
      </g>

      <!-- B.Tech (CSE) -->
      <g transform="translate(90, 0)">
        <polygon points="12 2 2 7 12 12 22 7 12 2" fill="none" stroke="#818CF8" stroke-width="1.3" />
        <path d="M 6 9.5 L 6 15 C 6 17 12 19 12 19 C 12 19 18 17 18 15 L 18 9.5" fill="none" stroke="#818CF8" stroke-width="1.3" />
        <text x="28" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#CBD5E1">B.Tech (CSE)</text>
      </g>

      <!-- Always learning -->
      <g transform="translate(230, 0)">
        <polyline points="5 4 1 8 5 12" fill="none" stroke="#C084FC" stroke-width="1.3" />
        <polyline points="11 4 15 8 11 12" fill="none" stroke="#C084FC" stroke-width="1.3" />
        <text x="22" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#CBD5E1">Always learning</text>
      </g>

      <!-- Open to collaboration -->
      <g transform="translate(370, 0)">
        <path d="M 8 13 L 2 7 C 0 5 0 2 3 1 C 5 0 7 2 8 3 C 9 2 11 0 13 1 C 16 2 16 5 14 7 Z" fill="none" stroke="#F43F5E" stroke-width="1.3" />
        <text x="20" y="11" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#CBD5E1">Open to collaboration</text>
      </g>
    </g>
  </g>

  <!-- Right: Rishi Shaw Neon Signature -->
  <g transform="translate(860, 60)">
    <!-- Signature Script -->
    <path d="M 28 65 C 28 35, 32 15, 35 12 C 40 8, 56 6, 60 20 C 63 32, 50 42, 34 44 C 42 46, 54 58, 62 68 M 64 52 C 67 44, 70 42, 73 53 C 75 58, 77 44, 82 43 C 86 42, 85 54, 88 53 C 92 48, 95 30, 96 22 C 96 22, 95 54, 98 52 C 102 44, 106 42, 109 52 M 125 58 C 122 55, 126 30, 138 20 C 146 12, 154 18, 146 32 C 138 46, 126 50, 138 56 C 145 60, 156 54, 160 48 M 162 48 C 164 36, 166 22, 167 18 C 167 18, 166 48, 172 46 C 176 40, 180 39, 183 48 C 185 50, 188 42, 194 43 C 198 44, 201 48, 205 42 C 210 44, 214 43, 220 50 C 228 42, 240 38, 252 46 C 265 55, 230 76, 175 75 C 105 73, 50 68, 20 74 C -5 79, 35 78, 120 76 C 200 74, 260 72, 280 70" 
          fill="none" stroke="url(#sig-glow-grad)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" filter="url(#sig-glow)" />
    <circle cx="83" cy="44" r="1.5" fill="#E879F9" filter="url(#sig-glow)" />
    <circle cx="118" cy="44" r="1.5" fill="#E879F9" filter="url(#sig-glow)" />
    
    <!-- BUILD • LEARN • IMPACT -->
    <text x="140" y="105" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#94A3B8" letter-spacing="4" text-anchor="middle">
      BUILD <tspan fill="#38BDF8">•</tspan> LEARN <tspan fill="#A855F7">•</tspan> IMPACT
    </text>
  </g>
</svg>"""

with open('assets/profile-svgs/about-me-section.svg', 'w', encoding='utf-8') as f:
    f.write(about_svg)


# ════════════════════════════════════════════════════════════════
# 4. TECH STACK SECTION SVG (1200 x 210)
# ════════════════════════════════════════════════════════════════
tech_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 210" width="100%" height="210">
  <defs>
    <linearGradient id="tech-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.3" />
    </linearGradient>
  </defs>

  <!-- Large Glass Card Container -->
  <rect x="2" y="2" width="1196" height="206" rx="20" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#tech-card-border)" stroke-width="1.5" />

  <!-- Header: Blue Icon + Title + View All Skills -->
  <g transform="translate(36, 24)">
    <rect x="0" y="0" width="34" height="34" rx="8" fill="#3B82F6" fill-opacity="0.2" stroke="#60A5FA" stroke-width="1.2" />
    <!-- Layers Icon -->
    <polygon points="17 9 7 14 17 19 27 14 17 9" fill="none" stroke="#38BDF8" stroke-width="1.4" />
    <polyline points="7 18 17 23 27 18" fill="none" stroke="#38BDF8" stroke-width="1.4" />
    <text x="46" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="700" fill="#FFFFFF">Tech Stack</text>

    <!-- View All Skills Link -->
    <text x="1120" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8" text-anchor="end">View All Skills →</text>
  </g>

  <!-- 10 Tech Cards in Horizontal Row -->
  <g transform="translate(36, 75)">
    <!-- 1. Python -->
    <g transform="translate(0, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <path d="M 49 22 C 40 22 41 26 41 26 L 41 30 L 50 30 L 50 31 L 31 31 C 31 31 24 31 24 40 C 24 49 30 49 30 49 L 34 49 L 34 44 C 34 44 34 38 40 38 L 50 38 C 50 38 56 38 56 32 L 56 28 C 56 28 57 22 49 22 Z" fill="#38BDF8" transform="translate(1, 0)" />
      <path d="M 50 58 C 59 58 58 54 58 54 L 58 50 L 49 50 L 49 49 L 68 49 C 68 49 75 49 75 40 C 75 31 69 31 69 31 L 65 31 L 65 36 C 65 36 65 42 59 42 L 49 42 C 49 42 43 42 43 48 L 43 52 C 43 52 42 58 50 58 Z" fill="#FACC15" transform="translate(-1, 0)" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">Python</text>
    </g>

    <!-- 2. JavaScript -->
    <g transform="translate(114, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <rect x="33" y="24" width="32" height="32" rx="4" fill="#FACC15" />
      <text x="49" y="47" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="900" fill="#000000" text-anchor="middle">JS</text>
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">JavaScript</text>
    </g>

    <!-- 3. React -->
    <g transform="translate(228, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <circle cx="49" cy="40" r="3" fill="#00F0FF" />
      <ellipse cx="49" cy="40" rx="16" ry="6" fill="none" stroke="#00F0FF" stroke-width="1.4" />
      <ellipse cx="49" cy="40" rx="16" ry="6" fill="none" stroke="#00F0FF" stroke-width="1.4" transform="rotate(60 49 40)" />
      <ellipse cx="49" cy="40" rx="16" ry="6" fill="none" stroke="#00F0FF" stroke-width="1.4" transform="rotate(120 49 40)" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">React</text>
    </g>

    <!-- 4. Node.js -->
    <g transform="translate(342, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <path d="M 49 24 L 64 32 L 64 48 L 49 56 L 34 48 L 34 32 Z" fill="none" stroke="#22C55E" stroke-width="2" />
      <text x="49" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="800" fill="#22C55E" text-anchor="middle">JS</text>
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">Node.js</text>
    </g>

    <!-- 5. Laravel -->
    <g transform="translate(456, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <path d="M 36 34 L 46 28 L 56 34 L 56 46 L 46 52 L 36 46 Z M 46 36 L 56 30 L 66 36 L 66 48 L 56 54 L 46 48 Z" fill="none" stroke="#EF4444" stroke-width="1.8" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">Laravel</text>
    </g>

    <!-- 6. MySQL -->
    <g transform="translate(570, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <path d="M 64 36 C 60 30 50 28 44 32 C 38 36 36 44 40 50 C 44 54 52 54 58 48 C 62 44 66 40 64 36 Z" fill="none" stroke="#00758F" stroke-width="2.2" />
      <path d="M 40 46 C 36 46 32 44 30 40 C 30 40 34 38 38 40" fill="none" stroke="#F29111" stroke-width="2" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">MySQL</text>
    </g>

    <!-- 7. OpenCV -->
    <g transform="translate(684, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <circle cx="49" cy="33" r="7" fill="none" stroke="#EF4444" stroke-width="3" />
      <circle cx="41" cy="47" r="7" fill="none" stroke="#22C55E" stroke-width="3" />
      <circle cx="57" cy="47" r="7" fill="none" stroke="#3B82F6" stroke-width="3" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">OpenCV</text>
    </g>

    <!-- 8. YOLO -->
    <g transform="translate(798, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <rect x="33" y="27" width="32" height="24" rx="4" fill="#061224" stroke="#00F0FF" stroke-width="1.4" />
      <text x="49" y="44" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#00F0FF" text-anchor="middle">YOLO</text>
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">YOLO</text>
    </g>

    <!-- 9. Git -->
    <g transform="translate(912, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <rect x="37" y="28" width="24" height="24" rx="4" fill="#F05032" transform="rotate(45 49 40)" />
      <circle cx="44" cy="35" r="2.5" fill="#FFFFFF" />
      <circle cx="54" cy="45" r="2.5" fill="#FFFFFF" />
      <line x1="44" y1="35" x2="54" y2="45" stroke="#FFFFFF" stroke-width="1.8" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">Git</text>
    </g>

    <!-- 10. VS Code -->
    <g transform="translate(1026, 0)">
      <rect width="98" height="100" rx="12" fill="#0E1528" stroke="#1E293B" stroke-width="1" />
      <path d="M 58 24 L 43 36 L 43 44 L 58 56 L 65 52 L 65 28 Z M 48 40 L 37 32 L 33 34 L 42 40 L 33 46 L 37 48 Z" fill="#007ACC" />
      <text x="49" y="82" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">VS Code</text>
    </g>
  </g>
</svg>"""

with open('assets/profile-svgs/tech-stack-section.svg', 'w', encoding='utf-8') as f:
    f.write(tech_svg)


# ════════════════════════════════════════════════════════════════
# 5. PROJECTS HEADER SVG (1200 x 130)
# ════════════════════════════════════════════════════════════════
projects_header_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 130" width="100%" height="130">
  <defs>
    <linearGradient id="journey-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
    <filter id="p-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <g transform="translate(600, 30)">
    <!-- Pretitle -->
    <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#00F0FF" letter-spacing="3" text-anchor="middle" filter="url(#p-glow)">// MY WORK</text>
    
    <!-- Title -->
    <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="middle">
      Projects <tspan fill="url(#journey-grad)">Journey</tspan>
    </text>

    <!-- Subtitle -->
    <text x="0" y="78" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" fill="#94A3B8" text-anchor="middle">
      A collection of projects that reflect my learning, skills and passion.
    </text>
  </g>

  <!-- Central Spine Start -->
  <line x1="600" y1="105" x2="600" y2="130" stroke="#00F0FF" stroke-width="4" filter="url(#p-glow)" />
</svg>"""

with open('assets/profile-svgs/projects-header.svg', 'w', encoding='utf-8') as f:
    f.write(projects_header_svg)


# ════════════════════════════════════════════════════════════════
# 6. PROJECTS ROWS 01 to 08 SVGs (1200 x 340 each)
# Strict Alternating Layout:
# 01: Screenshot LEFT | Node CENTER | Description RIGHT
# 02: Description LEFT | Node CENTER | Screenshot RIGHT
# ...
# ════════════════════════════════════════════════════════════════
projects_data = [
    (
        1, 'AETHER OS', 'AI-Powered Operating System', 
        'Natural language interface for file management, app control, and automation. A futuristic OS that brings AI into everyday computing.',
        ['React', 'TypeScript', 'Python', 'OpenCV'],
        'PROJECT_SCREENSHOT_01', '#00F0FF', '#3B82F6', 'left'
    ),
    (
        2, 'CallBuddy AI', 'Real-Time AI Voice Assistant', 
        'Live voice communication platform with real-time transcription, AI responses and natural conversation.',
        ['React', 'Socket.IO', 'WebRTC', 'Python'],
        'PROJECT_SCREENSHOT_02', '#38BDF8', '#818CF8', 'right'
    ),
    (
        3, 'Mochi', 'AI Companion & Smart Assistant', 
        'Sleek futuristic AI robot companion featuring autonomous ambient interaction, contextual intelligence, and real-time voice and vision synthesis.',
        ['Python', 'PyTorch', 'React', 'FastAPI'],
        'PROJECT_SCREENSHOT_03', '#EC4899', '#A855F7', 'left'
    ),
    (
        4, 'VN Media', 'Social Media & Content Platform', 
        'A full-stack social media platform with real-time features, content feeds, user profiles and interactive media distribution.',
        ['JavaScript', 'Node.js', 'Express', 'MongoDB'],
        'PROJECT_SCREENSHOT_04', '#00F0FF', '#10B981', 'right'
    ),
    (
        5, 'S-PPT Maker', 'AI-Powered Presentation Generator', 
        'Automated presentation creation system streamlining slide composition, structured content templates, and seamless web export workflows.',
        ['JavaScript', 'React', 'Node.js', 'HTML5'],
        'PROJECT_SCREENSHOT_05', '#F59E0B', '#3B82F6', 'left'
    ),
    (
        6, 'Pirate Civ', 'Procedural Strategy & Simulation Game', 
        'Interactive civilization and naval strategy simulation game with procedural generation, resource economies, and immersive canvas rendering.',
        ['JavaScript', 'Canvas API', 'WebAudio', 'Vite'],
        'PROJECT_SCREENSHOT_06', '#10B981', '#00F0FF', 'right'
    ),
    (
        7, 'Rishi Cosmic Portfolio', 'Immersive 3D Space Portfolio', 
        'Space-themed personal showcase built with interactive 3D particle shaders, smooth scroll choreography, and celestial visual effects.',
        ['TypeScript', 'Three.js', 'React', 'GSAP'],
        'PROJECT_SCREENSHOT_07', '#A855F7', '#00F0FF', 'left'
    ),
    (
        8, 'The Four Pillars', 'Interactive 3D Showcase', 
        'High-performance creative web showcase with 3D animations, custom design tokens, fluid glassmorphism, and smooth responsive UI.',
        ['React', 'Three.js', 'Vite', 'TailwindCSS'],
        'PROJECT_SCREENSHOT_08', '#38BDF8', '#C084FC', 'right'
    )
]

for idx, title, category, desc, badges, placeholder_id, c1, c2, orientation in projects_data:
    num = f"{idx:02d}"
    
    # Coordinates based on alternating orientation:
    if orientation == 'left':
        # Screenshot on Left (x=40), Description on Right (x=670)
        screenshot_x = 40
        desc_x = 670
        text_align = 'left'
    else:
        # Description on Left (x=50), Screenshot on Right (x=680)
        desc_x = 50
        screenshot_x = 680
        text_align = 'right'

    badges_xml = ""
    bx = 0
    for b in badges:
        bw = len(b) * 9 + 20
        badges_xml += f"""
        <g transform="translate({bx}, 0)">
          <rect width="{bw}" height="26" rx="13" fill="#0B1325" stroke="#1E293B" stroke-width="1" />
          <text x="{bw//2}" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">{b}</text>
        </g>
        """
        bx += bw + 8

    # Wrap description into 2-3 clean lines
    words = desc.split(' ')
    line1 = ' '.join(words[: len(words)//2])
    line2 = ' '.join(words[len(words)//2 :])

    row_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="100%" height="340">
  <defs>
    <!-- Continuous Vertical Glowing Spine -->
    <linearGradient id="spine-grad-{num}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="50%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>

    <!-- Glowing Node Filter -->
    <filter id="node-glow-{num}" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Screenshot Border Gradient -->
    <linearGradient id="ss-border-{num}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.7" />
      <stop offset="50%" stop-color="{c2}" stop-opacity="0.3" />
      <stop offset="100%" stop-color="{c1}" stop-opacity="0.6" />
    </linearGradient>

    <filter id="card-shadow-{num}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#000000" flood-opacity="0.8" />
      <feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="{c1}" flood-opacity="0.15" />
    </filter>
  </defs>

  <!-- ── 1. Central Vertical Spine (Continuous through 340px) ── -->
  <line x1="600" y1="0" x2="600" y2="340" stroke="url(#spine-grad-{num})" stroke-width="4" filter="url(#node-glow-{num})" />
  <line x1="600" y1="0" x2="600" y2="340" stroke="#FFFFFF" stroke-width="1.2" stroke-opacity="0.6" />

  <!-- ── 2. Center Numbered Glowing Node (60px diameter) ── -->
  <g transform="translate(600, 170)">
    <!-- Outer Glow Halo -->
    <circle cx="0" cy="0" r="38" fill="{c2}" fill-opacity="0.45" filter="url(#node-glow-{num})" />
    <!-- Outer Ring -->
    <circle cx="0" cy="0" r="30" fill="#070B16" stroke="{c1}" stroke-width="2.5" />
    <!-- Inner Ring -->
    <circle cx="0" cy="0" r="24" fill="#0A0F1D" stroke="{c2}" stroke-width="1" stroke-opacity="0.5" />
    <!-- Bold Number -->
    <text x="0" y="6" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">{num}</text>
  </g>

  <!-- ── 3. Big Screenshot Card (480px x 270px, 16:9 ratio) ── -->
  <g transform="translate({screenshot_x}, 35)" filter="url(#card-shadow-{num})">
    <!-- Card Frame -->
    <rect width="480" height="270" rx="16" fill="#0A0F1E" stroke="url(#ss-border-{num})" stroke-width="1.8" />
    
    <!-- Window Bar -->
    <rect width="480" height="32" rx="16" fill="#0F172A" fill-opacity="0.7" />
    <circle cx="20" cy="16" r="4.5" fill="#EF4444" opacity="0.8" />
    <circle cx="34" cy="16" r="4.5" fill="#F59E0B" opacity="0.8" />
    <circle cx="48" cy="16" r="4.5" fill="#10B981" opacity="0.8" />
    <text x="68" y="20" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748B">{title.lower().replace(' ', '-')}.system</text>

    <!-- Preview HUD Artwork -->
    <g transform="translate(250, 60)">
      <rect width="200" height="180" rx="10" fill="#070C18" stroke="{c2}" stroke-opacity="0.3" stroke-width="1" />
      <circle cx="100" cy="90" r="50" fill="none" stroke="{c1}" stroke-width="1" stroke-dasharray="4 6" opacity="0.5" />
      <circle cx="100" cy="90" r="24" fill="{c1}" fill-opacity="0.2" stroke="{c1}" stroke-width="1.5" />
      <circle cx="100" cy="90" r="8" fill="{c1}" />
    </g>

    <!-- Left Project Typography & Replacement Badge -->
    <g transform="translate(32, 70)">
      <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="#F8FAFC">{title}</text>
      <text x="0" y="48" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="{c1}">{category}</text>
      
      <!-- Replacement Indicator Pill -->
      <g transform="translate(0, 85)">
        <rect width="200" height="36" rx="8" fill="#060A14" stroke="{c1}" stroke-width="1.2" />
        <text x="100" y="23" font-family="'JetBrains Mono', monospace" font-size="11.5" font-weight="700" fill="{c1}" text-anchor="middle" letter-spacing="1">{placeholder_id}</text>
      </g>
    </g>
  </g>

  <!-- ── 4. Project Description Card ── -->
  <g transform="translate({desc_x}, 50)">
    <!-- Title -->
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="{c1}">{title}</text>
    
    <!-- Category -->
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="600" fill="#94A3B8">{category}</text>
    
    <!-- Description Paragraph -->
    <text x="0" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#CBD5E1" line-height="1.6">
      <tspan x="0" dy="0">{line1}</tspan>
      <tspan x="0" dy="24">{line2}</tspan>
    </text>

    <!-- Technology Badges -->
    <g transform="translate(0, 155)">
      {badges_xml}
    </g>

    <!-- Action Links -->
    <g transform="translate(0, 215)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8">
        Live Demo ↗ &nbsp;&nbsp;<tspan fill="#64748B">|</tspan>&nbsp;&nbsp; GitHub ↗
      </text>
    </g>
  </g>
</svg>"""

    with open(f'assets/profile-svgs/project-row-{num}.svg', 'w', encoding='utf-8') as f:
        f.write(row_svg)


# ════════════════════════════════════════════════════════════════
# 7. STATS SECTION SVG (1200 x 120)
# ════════════════════════════════════════════════════════════════
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="100%" height="120">
  <defs>
    <linearGradient id="stat-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.35" />
    </linearGradient>
  </defs>

  <g transform="translate(36, 10)">
    <!-- 1. Total Repositories -->
    <g transform="translate(0, 0)">
      <rect width="265" height="96" rx="16" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#stat-border)" stroke-width="1.3" />
      <!-- Icon -->
      <rect x="20" y="24" width="48" height="48" rx="12" fill="#8B5CF6" fill-opacity="0.18" stroke="#A855F7" stroke-width="1.2" />
      <rect x="34" y="36" width="20" height="24" rx="2" fill="none" stroke="#C084FC" stroke-width="2" />
      <line x1="38" y1="42" x2="50" y2="42" stroke="#C084FC" stroke-width="1.8" />
      <line x1="38" y1="48" x2="46" y2="48" stroke="#C084FC" stroke-width="1.8" />
      <!-- Text -->
      <text x="82" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Total Repositories</text>
      <text x="82" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="#FFFFFF">20+</text>
    </g>

    <!-- 2. Total Stars -->
    <g transform="translate(288, 0)">
      <rect width="265" height="96" rx="16" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#stat-border)" stroke-width="1.3" />
      <rect x="20" y="24" width="48" height="48" rx="12" fill="#FACC15" fill-opacity="0.18" stroke="#FACC15" stroke-width="1.2" />
      <polygon points="44 34 47 43 56 44 49 50 51 59 44 54 37 59 39 50 32 44 41 43 44 34" fill="#FACC15" />
      <text x="82" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Total Stars</text>
      <text x="82" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="#FFFFFF">50+</text>
    </g>

    <!-- 3. Total Commits -->
    <g transform="translate(576, 0)">
      <rect width="265" height="96" rx="16" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#stat-border)" stroke-width="1.3" />
      <rect x="20" y="24" width="48" height="48" rx="12" fill="#38BDF8" fill-opacity="0.18" stroke="#38BDF8" stroke-width="1.2" />
      <circle cx="50" cy="44" r="3.5" fill="none" stroke="#38BDF8" stroke-width="2" />
      <circle cx="38" cy="54" r="3.5" fill="none" stroke="#38BDF8" stroke-width="2" />
      <line x1="38" y1="36" x2="38" y2="50" stroke="#38BDF8" stroke-width="2" />
      <text x="82" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Total Commits</text>
      <text x="82" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="#FFFFFF">500+</text>
    </g>

    <!-- 4. Current Streak -->
    <g transform="translate(864, 0)">
      <rect width="265" height="96" rx="16" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#stat-border)" stroke-width="1.3" />
      <rect x="20" y="24" width="48" height="48" rx="12" fill="#FB923C" fill-opacity="0.18" stroke="#FB923C" stroke-width="1.2" />
      <path d="M 44 34 C 44 38 41 40 41 43 C 41 46 44 47 44 50 C 44 54 41 56 38 56 C 35 56 32 53 32 50 C 32 44 38 38 44 34 Z" fill="#FB923C" />
      <path d="M 46 42 C 48 45 48 47 47 49 C 48 51 49 53 48 55 C 47 57 45 58 43 58 C 45 56 46 54 45 52 C 44 50 44 48 45 46 C 45 44 46 43 46 42 Z" fill="#F87171" />
      <text x="82" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Current Streak</text>
      <text x="82" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="#FFFFFF">30+ days</text>
    </g>
  </g>
</svg>"""

with open('assets/profile-svgs/stats-section.svg', 'w', encoding='utf-8') as f:
    f.write(stats_svg)


# ════════════════════════════════════════════════════════════════
# 8. FOOTER SECTION SVG (1200 x 90)
# ════════════════════════════════════════════════════════════════
footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 90" width="100%" height="90">
  <defs>
    <linearGradient id="footer-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.35" />
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="1196" height="86" rx="16" fill="#0A0F1E" fill-opacity="0.85" stroke="url(#footer-border)" stroke-width="1.3" />

  <!-- Left: Handwritten Quote -->
  <g transform="translate(36, 50)">
    <text font-family="'Caveat', cursive, -apple-system, sans-serif" font-size="26" font-weight="600" fill="#F8FAFC" letter-spacing="0.5">
      “A better tomorrow is built by what we do today.” <tspan font-family="-apple-system, sans-serif" font-size="13" font-weight="400" fill="#64748B">— Rishi Shaw</tspan>
    </text>
  </g>

  <!-- Right: Social Icons -->
  <g transform="translate(980, 24)">
    <!-- GitHub -->
    <g transform="translate(0, 0)">
      <circle cx="20" cy="20" r="19" fill="#0F172A" stroke="#334155" stroke-width="1.2" />
      <path d="M 15 28 C 15 25 17 23 20 23 C 23 23 25 25 25 28" fill="none" stroke="#94A3B8" stroke-width="1.5" />
      <circle cx="20" cy="17" r="4.5" fill="none" stroke="#94A3B8" stroke-width="1.5" />
    </g>
    <!-- LinkedIn -->
    <g transform="translate(50, 0)">
      <circle cx="20" cy="20" r="19" fill="#0F172A" stroke="#334155" stroke-width="1.2" />
      <rect x="13" y="13" width="14" height="14" rx="2" fill="none" stroke="#94A3B8" stroke-width="1.5" />
      <text x="20" y="24" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#94A3B8" text-anchor="middle">in</text>
    </g>
    <!-- Email -->
    <g transform="translate(100, 0)">
      <circle cx="20" cy="20" r="19" fill="#0F172A" stroke="#334155" stroke-width="1.2" />
      <rect x="12" y="14" width="16" height="12" rx="2" fill="none" stroke="#94A3B8" stroke-width="1.5" />
      <path d="M 12 15 L 20 21 L 28 15" fill="none" stroke="#94A3B8" stroke-width="1.5" />
    </g>
    <!-- Instagram -->
    <g transform="translate(150, 0)">
      <circle cx="20" cy="20" r="19" fill="#0F172A" stroke="#334155" stroke-width="1.2" />
      <rect x="13" y="13" width="14" height="14" rx="4" fill="none" stroke="#94A3B8" stroke-width="1.5" />
      <circle cx="20" cy="20" r="3.5" fill="none" stroke="#94A3B8" stroke-width="1.4" />
      <circle cx="24.5" cy="15.5" r="1" fill="#94A3B8" />
    </g>
  </g>
</svg>"""

with open('assets/profile-svgs/footer-section.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)

print("All profile SVGs generated successfully in assets/profile-svgs/!")
