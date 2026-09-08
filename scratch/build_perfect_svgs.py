import os
import base64
from io import BytesIO
from PIL import Image
import xml.etree.ElementTree as ET

os.makedirs('assets/profile-svgs', exist_ok=True)

def get_compressed_b64(path, max_width=800):
    if not os.path.exists(path):
        return None
    try:
        img = Image.open(path).convert('RGB')
        w, h = img.size
        if w > max_width:
            new_h = int(h * (max_width / w))
            img = img.resize((max_width, new_h), Image.Resampling.LANCZOS)
        buf = BytesIO()
        img.save(buf, format='JPEG', quality=85)
        return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return None

aether_img = get_compressed_b64('assets/screenshots/aether-os.png')
callbuddy_img = get_compressed_b64('assets/screenshots/callbuddy-ai-1.png')
fourpillars_img = get_compressed_b64('assets/screenshots/the-four-pillars.png')

# ════════════════════════════════════════════════════════════════
# 1. FIXED HERO SECTION SVG (1200 x 360) - 100% VALID XML
# ════════════════════════════════════════════════════════════════
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="360">
  <defs>
    <linearGradient id="halo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="40%" stop-color="#3B82F6" />
      <stop offset="80%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.35" />
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.3" />
    </linearGradient>

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

  <!-- Left: Profile Avatar -->
  <g>
    <!-- Outer Luminous Ring -->
    <circle cx="110" cy="130" r="82" fill="none" stroke="url(#halo-grad)" stroke-width="3.5" filter="url(#avatar-glow)" />
    <circle cx="110" cy="130" r="78" fill="#0A0F1E" />

    <!-- Sunset Silhouette Inside Avatar -->
    <g clip-path="url(#avatar-clip)">
      <rect x="30" y="50" width="160" height="160" fill="#1E293B" />
      <path d="M 30 150 Q 110 135 190 150 L 190 210 L 30 210 Z" fill="#F97316" fill-opacity="0.45" />
      <path d="M 30 165 Q 110 150 190 165 L 190 210 L 30 210 Z" fill="#E11D48" fill-opacity="0.4" />
      <path d="M 110 95 C 98 95 90 105 90 120 C 90 132 98 140 108 143 C 95 148 75 155 70 200 L 150 200 C 145 155 125 148 112 143 C 122 140 130 132 130 120 C 130 105 122 95 110 95 Z" fill="#060911" />
      <path d="M 98 100 Q 110 96 122 100" stroke="#00F0FF" stroke-width="2" fill="none" opacity="0.8" />
    </g>

    <!-- Available for Opportunities Status Pill -->
    <g transform="translate(25, 235)">
      <rect x="0" y="0" width="170" height="28" rx="14" fill="#090E1B" stroke="#334155" stroke-width="1.2" />
      <circle cx="16" cy="14" r="4.5" fill="#10B981" filter="url(#hero-glow)" />
      <text x="28" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600" fill="#94A3B8">Available for opportunities</text>
    </g>
  </g>

  <!-- Center: Hero Text and Actions -->
  <g transform="translate(240, 50)">
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="500" fill="#94A3B8">Hi, I'm</text>
    
    <!-- Big Name -->
    <text x="0" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="56" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">Rishi <tspan fill="url(#name-grad)">Shaw</tspan></text>
    
    <!-- Subtitle Role -->
    <text x="0" y="116" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15.5" font-weight="600" fill="#94A3B8" letter-spacing="0.3">AI Engineer &#8226; Full Stack Developer &#8226; Computer Vision Developer</text>

    <!-- Bio paragraph -->
    <text x="0" y="150" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" fill="#94A3B8">
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

  <!-- Right: Quote and Stats Card -->
  <g transform="translate(740, 25)">
    <rect x="0" y="0" width="440" height="300" rx="18" fill="#0B1122" fill-opacity="0.85" stroke="url(#card-border)" stroke-width="1.5" />
    
    <!-- Quote Icon -->
    <text x="32" y="55" font-family="serif" font-size="44" fill="#38BDF8" filter="url(#hero-glow)">“</text>
    
    <!-- Quote Body -->
    <text x="62" y="50" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" fill="#E2E8F0">
      <tspan x="62" dy="0">Engineering is not just</tspan>
      <tspan x="62" dy="24">about writing code, it's about</tspan>
      <tspan x="62" dy="24">solving real problems.</tspan>
    </text>
    <text x="390" y="130" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" fill="#64748B" text-anchor="end">&#8212; Rishi Shaw</text>

    <!-- Divider Line -->
    <line x1="32" y1="160" x2="408" y2="160" stroke="#1E293B" stroke-width="1.2" />

    <!-- 3 Metrics Columns -->
    <g transform="translate(32, 185)">
      <text x="50" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="800" fill="#38BDF8" text-anchor="middle" filter="url(#hero-glow)">8+</text>
      <text x="50" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Projects</text>

      <text x="188" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="800" fill="#38BDF8" text-anchor="middle" filter="url(#hero-glow)">3+</text>
      <text x="188" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Tech Domains</text>

      <text x="326" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="38" font-weight="800" fill="#C084FC" text-anchor="middle" filter="url(#hero-glow)">&#8734;</text>
      <text x="326" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#94A3B8" text-anchor="middle">Learning</text>
    </g>
  </g>
</svg>"""

with open('assets/profile-svgs/hero-section.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

ET.fromstring(hero_svg)
print("Hero SVG generated & valid XML!")

# ════════════════════════════════════════════════════════════════
# 2. GENERATE ALL 8 PROJECT ROW SVGs MATCHING REFERENCE IMAGE
# ════════════════════════════════════════════════════════════════
projects_spec = [
    {
        'num': '01',
        'title': 'AETHER OS',
        'category': 'AI-Powered Operating System',
        'desc_1': 'Natural language interface for file management, app control,',
        'desc_2': 'and automation. A futuristic OS that brings AI into everyday computing.',
        'badges': ['React', 'TypeScript', 'Python', 'OpenCV'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'left',
        'c1': '#00F0FF', 'c2': '#3B82F6',
        'b64': aether_img
    },
    {
        'num': '02',
        'title': 'CallBuddy AI',
        'category': 'Real-Time AI Voice Assistant',
        'desc_1': 'Live voice communication platform with real-time',
        'desc_2': 'transcription, AI responses and natural conversation.',
        'badges': ['React', 'Socket.IO', 'WebRTC', 'Python'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'right',
        'c1': '#38BDF8', 'c2': '#818CF8',
        'b64': callbuddy_img
    },
    {
        'num': '03',
        'title': 'The Four Pillars',
        'category': 'Interactive 3D Showcase',
        'desc_1': 'High-performance creative web showcase with 3D',
        'desc_2': 'animations, custom designs and smooth UI.',
        'badges': ['React', 'Three.js', 'Vite', 'TailwindCSS'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'left',
        'c1': '#38BDF8', 'c2': '#C084FC',
        'b64': fourpillars_img
    },
    {
        'num': '04',
        'title': 'VN Media',
        'category': 'Social Media &amp; Content Platform',
        'desc_1': 'A full-stack social media platform with real-time',
        'desc_2': 'features, content feeds, user profiles and more.',
        'badges': ['JavaScript', 'Node.js', 'Express', 'MongoDB'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'right',
        'c1': '#00F0FF', 'c2': '#10B981',
        'mock': 'vn_media'
    },
    {
        'num': '05',
        'title': 'Hospital Management System',
        'category': 'Web Application',
        'desc_1': 'Manage patients, doctors, appointments, wards and',
        'desc_2': 'billing. Built with Laravel and MySQL.',
        'badges': ['Laravel', 'MySQL', 'Bootstrap', 'JavaScript'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'left',
        'c1': '#38BDF8', 'c2': '#3B82F6',
        'mock': 'hospital'
    },
    {
        'num': '06',
        'title': 'FreqSFA-Net',
        'category': 'Low-Light Enhancement &amp; Object Detection',
        'desc_1': 'Research project on low-light image enhancement',
        'desc_2': 'and object detection using YOLOv8.',
        'badges': ['Python', 'PyTorch', 'YOLOv8', 'OpenCV'],
        'links': 'Documentation ↗   |   GitHub ↗',
        'orientation': 'right',
        'c1': '#00F0FF', 'c2': '#8B5CF6',
        'mock': 'freqsfa'
    },
    {
        'num': '07',
        'title': 'Portfolio Website',
        'category': 'Personal Portfolio',
        'desc_1': 'A modern, responsive portfolio to showcase my',
        'desc_2': 'projects, skills and journey.',
        'badges': ['HTML', 'CSS', 'JavaScript', 'GSAP'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'orientation': 'left',
        'c1': '#38BDF8', 'c2': '#C084FC',
        'mock': 'portfolio'
    },
    {
        'num': '08',
        'title': 'C Programming Lab',
        'category': 'Practical Programs Collection',
        'desc_1': 'A collection of C programs and lab assignments',
        'desc_2': 'with proper documentation and explanations.',
        'badges': ['C', 'Data Structures', 'Algorithms'],
        'links': 'View Docs ↗   |   GitHub ↗',
        'orientation': 'right',
        'c1': '#38BDF8', 'c2': '#00F0FF',
        'mock': 'clab'
    }
]

def render_artwork(spec):
    c1 = spec['c1']
    c2 = spec['c2']
    # If base64 image available, embed it clipped with rounded corners!
    if spec.get('b64'):
        return f'''
        <clipPath id="clip-{spec['num']}">
          <rect width="480" height="270" rx="14" />
        </clipPath>
        <image href="{spec['b64']}" width="480" height="270" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-{spec['num']})" />
        '''
    mock = spec.get('mock')
    if mock == 'vn_media':
        # Dark sleek social dashboard mockup
        return f'''
        <rect width="480" height="270" rx="14" fill="#090E1A" />
        <!-- Top bar -->
        <rect width="480" height="28" fill="#0F172A" />
        <circle cx="16" cy="14" r="4" fill="#EF4444" />
        <circle cx="28" cy="14" r="4" fill="#F59E0B" />
        <circle cx="40" cy="14" r="4" fill="#10B981" />
        <text x="60" y="17" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B">vn-media.app // feed</text>
        <!-- Sidebar -->
        <rect x="0" y="28" width="80" height="242" fill="#070B14" />
        <line x1="20" y1="50" x2="60" y2="50" stroke="#334155" stroke-width="2" />
        <line x1="20" y1="70" x2="50" y2="70" stroke="#1E293B" stroke-width="2" />
        <line x1="20" y1="90" x2="60" y2="90" stroke="#1E293B" stroke-width="2" />
        <!-- Central Post Card -->
        <rect x="100" y="45" width="230" height="150" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
        <circle cx="120" cy="65" r="10" fill="#3B82F6" />
        <text x="140" y="65" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">Rishi Shaw</text>
        <text x="140" y="78" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B">@rishidev &#8226; 2h ago</text>
        <rect x="115" y="95" width="200" height="8" rx="4" fill="#1E293B" />
        <rect x="115" y="112" width="160" height="8" rx="4" fill="#1E293B" />
        <rect x="115" y="132" width="200" height="50" rx="6" fill="#162238" />
        <!-- Right side widgets -->
        <rect x="345" y="45" width="120" height="100" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
        <text x="355" y="62" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#94A3B8">Suggested</text>
        <circle cx="365" cy="82" r="8" fill="#C084FC" />
        <circle cx="365" cy="110" r="8" fill="#10B981" />
        '''
    elif mock == 'hospital':
        # Clean medical dashboard mockup matching reference row 05
        return f'''
        <rect width="480" height="270" rx="14" fill="#F1F5F9" />
        <!-- Top App Bar -->
        <rect width="480" height="32" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
        <circle cx="16" cy="16" r="4" fill="#EF4444" />
        <circle cx="28" cy="16" r="4" fill="#F59E0B" />
        <circle cx="40" cy="16" r="4" fill="#10B981" />
        <text x="60" y="20" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#0284C7">Hospital Management System</text>
        <!-- Sidebar -->
        <rect x="0" y="32" width="100" height="238" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
        <rect x="10" y="50" width="80" height="24" rx="4" fill="#0284C7" />
        <text x="20" y="66" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#FFFFFF">Dashboard</text>
        <text x="20" y="95" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">Patients</text>
        <text x="20" y="120" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">Doctors</text>
        <text x="20" y="145" font-family="-apple-system, sans-serif" font-size="10" fill="#64748B">Wards</text>
        <!-- Stat Cards -->
        <g transform="translate(115, 45)">
          <rect x="0" y="0" width="105" height="55" rx="8" fill="#0284C7" />
          <text x="12" y="22" font-family="-apple-system, sans-serif" font-size="10" fill="#E0F2FE">Total Patients</text>
          <text x="12" y="44" font-family="-apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">1,420</text>
          
          <rect x="120" y="0" width="105" height="55" rx="8" fill="#0D9488" />
          <text x="132" y="22" font-family="-apple-system, sans-serif" font-size="10" fill="#CCFBF1">Appointments</text>
          <text x="132" y="44" font-family="-apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">384</text>
          
          <rect x="240" y="0" width="105" height="55" rx="8" fill="#6366F1" />
          <text x="252" y="22" font-family="-apple-system, sans-serif" font-size="10" fill="#E0E7FF">Available Beds</text>
          <text x="252" y="44" font-family="-apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">56</text>
        </g>
        <!-- Table Mockup -->
        <rect x="115" y="115" width="345" height="135" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" />
        <rect x="115" y="115" width="345" height="28" fill="#F8FAFC" />
        <text x="130" y="133" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#64748B">Patient Name</text>
        <text x="240" y="133" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#64748B">Doctor</text>
        <text x="330" y="133" font-family="-apple-system, sans-serif" font-size="10" font-weight="600" fill="#64748B">Status</text>
        <line x1="115" y1="170" x2="460" y2="170" stroke="#F1F5F9" stroke-width="1" />
        <line x1="115" y1="200" x2="460" y2="200" stroke="#F1F5F9" stroke-width="1" />
        '''
    elif mock == 'freqsfa':
        # Dual-panel Night Enhancement Mockup (Low-Light Image vs Enhanced Output)
        return f'''
        <rect width="480" height="270" rx="14" fill="#0A0E1A" />
        <rect width="480" height="28" fill="#0F172A" />
        <text x="20" y="18" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#00F0FF">FreqSFA-Net // YOLOv8 Inference</text>
        <!-- Left Panel: Low Light -->
        <g transform="translate(18, 45)">
          <rect width="215" height="200" rx="8" fill="#05070D" stroke="#1E293B" stroke-width="1" />
          <text x="107" y="24" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B" text-anchor="middle">Low-Light Image</text>
          <!-- Dark road with faint headlamps -->
          <ellipse cx="107" cy="140" rx="40" ry="15" fill="#0B1322" />
          <circle cx="85" cy="135" r="4" fill="#FACC15" fill-opacity="0.5" />
          <circle cx="129" cy="135" r="4" fill="#FACC15" fill-opacity="0.5" />
        </g>
        <!-- Right Panel: Enhanced Output -->
        <g transform="translate(247, 45)">
          <rect width="215" height="200" rx="8" fill="#0F1E36" stroke="#00F0FF" stroke-opacity="0.4" stroke-width="1" />
          <text x="107" y="24" font-family="'JetBrains Mono', monospace" font-size="10" fill="#00F0FF" font-weight="600" text-anchor="middle">Enhanced Output</text>
          <!-- Vivid road with bright headlamps and bounding boxes -->
          <ellipse cx="107" cy="140" rx="60" ry="25" fill="#1E3A5F" />
          <circle cx="85" cy="135" r="7" fill="#FDE047" />
          <circle cx="129" cy="135" r="7" fill="#FDE047" />
          <!-- Green YOLO Bounding Box -->
          <rect x="70" y="115" width="75" height="50" fill="none" stroke="#22C55E" stroke-width="1.8" />
          <rect x="70" y="103" width="55" height="12" fill="#22C55E" />
          <text x="73" y="112" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="700" fill="#000000">car 0.94</text>
        </g>
        '''
    elif mock == 'portfolio':
        # Rishi Shaw Portfolio Website Preview Mockup
        return f'''
        <rect width="480" height="270" rx="14" fill="#070B14" />
        <rect width="480" height="28" fill="#0B1120" stroke="#1E293B" stroke-width="1" />
        <circle cx="16" cy="14" r="4" fill="#EF4444" />
        <circle cx="28" cy="14" r="4" fill="#F59E0B" />
        <circle cx="40" cy="14" r="4" fill="#10B981" />
        <text x="60" y="18" font-family="'JetBrains Mono', monospace" font-size="10" fill="#38BDF8">rishishaw.dev</text>
        <!-- Mini Hero Card inside -->
        <g transform="translate(30, 50)">
          <!-- Mini Avatar -->
          <circle cx="35" cy="45" r="28" fill="none" stroke="#00F0FF" stroke-width="2" />
          <circle cx="35" cy="45" r="24" fill="#1E293B" />
          <!-- Name & Role -->
          <text x="75" y="36" font-family="-apple-system, sans-serif" font-size="9" fill="#94A3B8">Hi, I'm</text>
          <text x="75" y="52" font-family="-apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF">Rishi <tspan fill="#C084FC">Shaw</tspan></text>
          <text x="75" y="66" font-family="-apple-system, sans-serif" font-size="8" fill="#64748B">AI Engineer &#8226; Full Stack Developer</text>
          <!-- Mini buttons -->
          <rect x="75" y="78" width="70" height="18" rx="6" fill="#6366F1" />
          <text x="110" y="90" font-family="-apple-system, sans-serif" font-size="7.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">View Work</text>
        </g>
        <!-- Mini Quote Card -->
        <rect x="250" y="55" width="200" height="85" rx="8" fill="#0B1122" stroke="#334155" stroke-width="1" />
        <text x="262" y="75" font-family="-apple-system, sans-serif" font-size="8.5" fill="#CBD5E1">Engineering is not just</text>
        <text x="262" y="88" font-family="-apple-system, sans-serif" font-size="8.5" fill="#CBD5E1">about writing code...</text>
        <text x="435" y="102" font-family="-apple-system, sans-serif" font-size="8" fill="#64748B" text-anchor="end">&#8212; Rishi Shaw</text>
        <!-- Mini Stats Bar -->
        <rect x="30" y="165" width="420" height="70" rx="10" fill="#0A1020" stroke="#1E293B" stroke-width="1" />
        <circle cx="60" cy="200" r="16" fill="#8B5CF6" fill-opacity="0.2" />
        <circle cx="170" cy="200" r="16" fill="#FACC15" fill-opacity="0.2" />
        <circle cx="280" cy="200" r="16" fill="#38BDF8" fill-opacity="0.2" />
        <circle cx="390" cy="200" r="16" fill="#FB923C" fill-opacity="0.2" />
        '''
    else:
        # C Programming Lab Mockup: IDE with file tree & main() code!
        return f'''
        <rect width="480" height="270" rx="14" fill="#080C16" />
        <!-- Top Bar -->
        <rect width="480" height="28" fill="#0F172A" />
        <circle cx="16" cy="14" r="4" fill="#EF4444" />
        <circle cx="28" cy="14" r="4" fill="#F59E0B" />
        <circle cx="40" cy="14" r="4" fill="#10B981" />
        <text x="60" y="18" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#94A3B8">01_hello.c &#8212; C-Programming-Lab</text>
        <!-- Sidebar File Tree -->
        <rect x="0" y="28" width="130" height="242" fill="#060910" />
        <text x="12" y="48" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#64748B">&#128193; c_programs</text>
        <text x="24" y="70" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#38BDF8">&#128196; 01_hello.c</text>
        <text x="24" y="90" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748B">&#128196; 02_fibonacci.c</text>
        <text x="24" y="110" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748B">&#128196; 03_prime.c</text>
        <text x="24" y="130" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748B">&#128196; 04_pointers.c</text>
        <text x="24" y="150" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#64748B">&#128196; 05_strings.c</text>
        <!-- Editor Code Content -->
        <g transform="translate(145, 45)">
          <text font-family="'JetBrains Mono', monospace" font-size="12" line-height="1.7">
            <tspan x="0" dy="0" fill="#64748B">1  </tspan><tspan fill="#EF4444">#include </tspan><tspan fill="#FACC15">&lt;stdio.h&gt;</tspan>
            <tspan x="0" dy="24" fill="#64748B">2  </tspan>
            <tspan x="0" dy="24" fill="#64748B">3  </tspan><tspan fill="#3B82F6">int </tspan><tspan fill="#F8FAFC">main() &#123;</tspan>
            <tspan x="0" dy="24" fill="#64748B">4  </tspan><tspan fill="#CBD5E1">    printf(</tspan><tspan fill="#22C55E">"Hello, World!\\n"</tspan><tspan fill="#CBD5E1">);</tspan>
            <tspan x="0" dy="24" fill="#64748B">5  </tspan><tspan fill="#3B82F6">    return </tspan><tspan fill="#C084FC">0</tspan><tspan fill="#CBD5E1">;</tspan>
            <tspan x="0" dy="24" fill="#64748B">6  </tspan><tspan fill="#F8FAFC">&#125;</tspan>
          </text>
        </g>
        '''

for spec in projects_spec:
    num = spec['num']
    orientation = spec['orientation']
    title = spec['title']
    category = spec['category']
    desc_1 = spec['desc_1']
    desc_2 = spec['desc_2']
    badges = spec['badges']
    links = spec['links']
    c1 = spec['c1']
    c2 = spec['c2']

    if orientation == 'left':
        screenshot_x = 40
        desc_x = 670
    else:
        desc_x = 50
        screenshot_x = 680

    badges_xml = ""
    bx = 0
    for b in badges:
        bw = len(b) * 9 + 22
        badges_xml += f"""
        <g transform="translate({bx}, 0)">
          <rect width="{bw}" height="26" rx="13" fill="#0B1325" stroke="#1E293B" stroke-width="1" />
          <text x="{bw//2}" y="17" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#94A3B8" text-anchor="middle">{b}</text>
        </g>
        """
        bx += bw + 8

    artwork = render_artwork(spec)

    row_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="100%" height="340">
  <defs>
    <linearGradient id="spine-grad-{num}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="50%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>

    <filter id="node-glow-{num}" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <linearGradient id="ss-border-{num}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.8" />
      <stop offset="50%" stop-color="{c2}" stop-opacity="0.3" />
      <stop offset="100%" stop-color="{c1}" stop-opacity="0.7" />
    </linearGradient>

    <filter id="card-shadow-{num}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#000000" flood-opacity="0.8" />
      <feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="{c1}" flood-opacity="0.18" />
    </filter>
  </defs>

  <!-- Central Vertical Spine (Continuous through 340px) -->
  <line x1="600" y1="0" x2="600" y2="340" stroke="url(#spine-grad-{num})" stroke-width="4" filter="url(#node-glow-{num})" />
  <line x1="600" y1="0" x2="600" y2="340" stroke="#FFFFFF" stroke-width="1.2" stroke-opacity="0.6" />

  <!-- Center Numbered Glowing Node (60px diameter) -->
  <g transform="translate(600, 170)">
    <circle cx="0" cy="0" r="38" fill="{c2}" fill-opacity="0.45" filter="url(#node-glow-{num})" />
    <circle cx="0" cy="0" r="30" fill="#070B16" stroke="{c1}" stroke-width="2.5" />
    <circle cx="0" cy="0" r="24" fill="#0A0F1D" stroke="{c2}" stroke-width="1" stroke-opacity="0.5" />
    <text x="0" y="6" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">{num}</text>
  </g>

  <!-- Big Screenshot Card (480px x 270px) -->
  <g transform="translate({screenshot_x}, 35)" filter="url(#card-shadow-{num})">
    <rect width="480" height="270" rx="16" fill="#0A0F1E" stroke="url(#ss-border-{num})" stroke-width="1.8" />
    {artwork}
  </g>

  <!-- Project Description Card -->
  <g transform="translate({desc_x}, 50)">
    <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="{c1}">{title}</text>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="600" fill="#94A3B8">{category}</text>
    
    <text x="0" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#CBD5E1">
      <tspan x="0" dy="0">{desc_1}</tspan>
      <tspan x="0" dy="24">{desc_2}</tspan>
    </text>

    <!-- Badges -->
    <g transform="translate(0, 155)">
      {badges_xml}
    </g>

    <!-- Action Links -->
    <g transform="translate(0, 215)">
      <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8">{links}</text>
    </g>
  </g>
</svg>"""

    with open(f'assets/profile-svgs/project-row-{num}.svg', 'w', encoding='utf-8') as f:
        f.write(row_svg)

    ET.fromstring(row_svg)
    print(f"Project row {num} ({title}): VALID XML!")

print("\nALL SVGs generated and validated successfully!")
