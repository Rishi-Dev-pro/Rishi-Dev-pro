import os
import xml.etree.ElementTree as ET
import base64
from PIL import Image
import io

print("=== BUILDING UPDATED HIGH-RES PROFILE ROW SVGs ===")

def get_compressed_b64(img_path):
    if not os.path.exists(img_path):
        print(f"Warning: {img_path} not found!")
        return None
    with Image.open(img_path) as im:
        im = im.convert('RGB')
        im.thumbnail((960, 540), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format='JPEG', quality=82, optimize=True)
        raw = buf.getvalue()
        b64 = base64.b64encode(raw).decode('utf-8')
        print(f"Loaded {img_path}: {len(raw)//1024} KB JPEG")
        return f"data:image/jpeg;base64,{b64}"

aether_img = get_compressed_b64('assets/screenshots/aether-os.png')
callbuddy_img = get_compressed_b64('assets/screenshots/callbuddy-ai-1.png')
fourpillars_img = get_compressed_b64('assets/screenshots/the-four-pillars.png')

projects_spec = [
    {
        'num': '01',
        'title': 'AETHER OS',
        'category': 'AI-Powered Operating System',
        'desc_1': 'Natural language interface for file management, app control,',
        'desc_2': 'and automation. A futuristic OS that brings AI into everyday computing.',
        'badges': ['React', 'TypeScript', 'Python', 'OpenCV'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'demo_url': 'https://github.com/Rishi-Dev-pro/AETHER-OS',
        'repo_url': 'https://github.com/Rishi-Dev-pro/AETHER-OS',
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
        'demo_url': 'https://github.com/Rishi-Dev-pro/CallBuddy-AI',
        'repo_url': 'https://github.com/Rishi-Dev-pro/CallBuddy-AI',
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
        'demo_url': 'https://the-four-pillars.vercel.app/',
        'repo_url': 'https://github.com/Rishi-Dev-pro/The-Four-Pillars',
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
        'demo_url': 'https://github.com/Rishi-Dev-pro/VN-media',
        'repo_url': 'https://github.com/Rishi-Dev-pro/VN-media',
        'orientation': 'right',
        'c1': '#00F0FF', 'c2': '#10B981',
        'mock': 'vn_media'
    },
    {
        'num': '05',
        'title': 'pirate-civ',
        'category': 'Pirate-Themed E-Commerce Website',
        'desc_1': 'High-seas nautical themed e-commerce shop featuring pirate merchandise,',
        'desc_2': 'interactive treasure catalog, cart workflows, and custom skull-and-cannon UI.',
        'badges': ['React', 'TypeScript', 'TailwindCSS', 'Node.js'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'demo_url': 'https://github.com/Rishi-Dev-pro/pirate-civ',
        'repo_url': 'https://github.com/Rishi-Dev-pro/pirate-civ',
        'orientation': 'left',
        'c1': '#F59E0B', 'c2': '#10B981',
        'mock': 'pirate_civ'
    },
    {
        'num': '06',
        'title': 'S-PPT-maker',
        'category': 'Free No-Watermark PowerPoint Maker',
        'desc_1': 'Zero-watermark presentation engine empowering fast slide design,',
        'desc_2': 'dynamic content templates, automated typography, and instant PPTX export.',
        'badges': ['JavaScript', 'React', 'Node.js', 'HTML5'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'demo_url': 'https://github.com/Rishi-Dev-pro/S-PPT-maker',
        'repo_url': 'https://github.com/Rishi-Dev-pro/S-PPT-maker',
        'orientation': 'right',
        'c1': '#F59E0B', 'c2': '#3B82F6',
        'mock': 's_ppt_maker'
    },
    {
        'num': '07',
        'title': 'Rishi-cosmic-protfolio',
        'category': 'Galaxy-Themed 3D Portfolio',
        'desc_1': 'Space-themed personal showcase built with interactive 3D particle shaders,',
        'desc_2': 'cosmic nebula backdrops, smooth orbit controls, and celestial GSAP motion.',
        'badges': ['Three.js', 'TypeScript', 'React', 'GSAP'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'demo_url': 'https://github.com/Rishi-Dev-pro/rishi-cosmic-portfolio',
        'repo_url': 'https://github.com/Rishi-Dev-pro/rishi-cosmic-portfolio',
        'orientation': 'left',
        'c1': '#C084FC', 'c2': '#00F0FF',
        'mock': 'cosmic_portfolio'
    },
    {
        'num': '08',
        'title': 'Mochu',
        'category': 'AI Girl Companion',
        'desc_1': 'Empathetic conversational AI girl companion with real-time emotion engine,',
        'desc_2': 'interactive live 2D/3D anime avatar synthesis, and contextual memory.',
        'badges': ['Python', 'PyTorch', 'FastAPI', 'React'],
        'links': 'Live Demo ↗   |   GitHub ↗',
        'demo_url': 'https://github.com/Rishi-Dev-pro/Mochu',
        'repo_url': 'https://github.com/Rishi-Dev-pro/Mochu',
        'orientation': 'right',
        'c1': '#EC4899', 'c2': '#8B5CF6',
        'mock': 'mochu'
    }
]

def render_artwork(spec):
    if spec.get('b64'):
        return f'''
        <clipPath id="clip-{spec['num']}">
          <rect width="480" height="270" rx="14" />
        </clipPath>
        <image href="{spec['b64']}" width="480" height="270" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-{spec['num']})" />
        '''
    mock = spec.get('mock')
    if mock == 'vn_media':
        return f'''
        <rect width="480" height="270" rx="14" fill="#090E1A" />
        <rect width="480" height="28" fill="#0F172A" />
        <circle cx="16" cy="14" r="4" fill="#EF4444" />
        <circle cx="28" cy="14" r="4" fill="#F59E0B" />
        <circle cx="40" cy="14" r="4" fill="#10B981" />
        <text x="60" y="17" font-family="'JetBrains Mono', monospace" font-size="10" fill="#64748B">vn-media.app // feed</text>
        <rect x="0" y="28" width="80" height="242" fill="#070B14" />
        <line x1="20" y1="50" x2="60" y2="50" stroke="#334155" stroke-width="2" />
        <line x1="20" y1="70" x2="50" y2="70" stroke="#1E293B" stroke-width="2" />
        <line x1="20" y1="90" x2="60" y2="90" stroke="#1E293B" stroke-width="2" />
        <rect x="100" y="45" width="230" height="150" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
        <circle cx="120" cy="65" r="10" fill="#3B82F6" />
        <text x="140" y="65" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">Rishi Shaw</text>
        <text x="140" y="78" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B">@rishidev &#8226; 2h ago</text>
        <rect x="115" y="95" width="200" height="8" rx="4" fill="#1E293B" />
        <rect x="115" y="112" width="160" height="8" rx="4" fill="#1E293B" />
        <rect x="115" y="132" width="200" height="50" rx="6" fill="#162238" />
        <rect x="345" y="45" width="120" height="100" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
        <text x="355" y="62" font-family="-apple-system, sans-serif" font-size="10" font-weight="700" fill="#94A3B8">Suggested</text>
        <circle cx="365" cy="82" r="8" fill="#C084FC" />
        <circle cx="365" cy="110" r="8" fill="#10B981" />
        '''
    elif mock == 'pirate_civ':
        return f'''
        <rect width="480" height="270" rx="14" fill="#080D18" />
        <rect width="480" height="30" fill="#0E1726" />
        <circle cx="16" cy="15" r="4" fill="#EF4444" />
        <circle cx="28" cy="15" r="4" fill="#F59E0B" />
        <circle cx="40" cy="15" r="4" fill="#10B981" />
        <text x="60" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#F59E0B">&#9875; pirate-civ.shop // high-seas outfitters</text>
        <rect x="385" y="6" width="82" height="18" rx="4" fill="#1E293B" />
        <text x="426" y="19" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FDE047" text-anchor="middle">&#128722; Loot Chest (3)</text>
        
        <g transform="translate(18, 40)">
          <rect width="444" height="60" rx="8" fill="#111B2E" stroke="#1E293B" stroke-width="1" />
          <text x="18" y="25" font-family="-apple-system, sans-serif" font-size="13" font-weight="800" fill="#F8FAFC">&#9760; CAPTAIN'S TREASURE VAULT</text>
          <text x="18" y="44" font-family="-apple-system, sans-serif" font-size="9.5" fill="#94A3B8">Authentic Pirate Relics, Cursed Artifacts &amp; Nautical Gear</text>
          <rect x="340" y="18" width="85" height="24" rx="5" fill="#F59E0B" />
          <text x="382" y="34" font-family="-apple-system, sans-serif" font-size="9.5" font-weight="800" fill="#0F172A" text-anchor="middle">Shop Loot &#10140;</text>
        </g>
        
        <g transform="translate(18, 112)">
          <!-- Product 1 -->
          <rect x="0" y="0" width="138" height="142" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
          <circle cx="69" cy="42" r="23" fill="#162238" stroke="#F59E0B" stroke-width="1.5" />
          <text x="69" y="47" font-size="18" text-anchor="middle">&#129517;</text>
          <text x="69" y="82" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#F8FAFC" text-anchor="middle">Jack's Compass</text>
          <text x="69" y="99" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#F59E0B" text-anchor="middle">450 Gold</text>
          <rect x="19" y="110" width="100" height="22" rx="4" fill="#0284C7" />
          <text x="69" y="124" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Add to Chest</text>

          <!-- Product 2 -->
          <rect x="153" y="0" width="138" height="142" rx="8" fill="#0F172A" stroke="#10B981" stroke-opacity="0.5" stroke-width="1" />
          <circle cx="222" cy="42" r="23" fill="#162238" stroke="#10B981" stroke-width="1.5" />
          <text x="222" y="47" font-size="18" text-anchor="middle">&#9876;</text>
          <text x="222" y="82" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#F8FAFC" text-anchor="middle">Kraken Cutlass</text>
          <text x="222" y="99" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#10B981" text-anchor="middle">820 Gold</text>
          <rect x="172" y="110" width="100" height="22" rx="4" fill="#10B981" />
          <text x="222" y="124" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#052E16" text-anchor="middle">Add to Chest</text>

          <!-- Product 3 -->
          <rect x="306" y="0" width="138" height="142" rx="8" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
          <circle cx="375" cy="42" r="23" fill="#162238" stroke="#00F0FF" stroke-width="1.5" />
          <text x="375" y="47" font-size="18" text-anchor="middle">&#127866;</text>
          <text x="375" y="82" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#F8FAFC" text-anchor="middle">Aged Pirate Rum</text>
          <text x="375" y="99" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#00F0FF" text-anchor="middle">120 Gold</text>
          <rect x="325" y="110" width="100" height="22" rx="4" fill="#0284C7" />
          <text x="375" y="124" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Add to Chest</text>
        </g>
        '''
    elif mock == 's_ppt_maker':
        return f'''
        <rect width="480" height="270" rx="14" fill="#0A0F1D" />
        <rect width="480" height="34" fill="#141E33" stroke="#1E293B" stroke-width="1" />
        <rect x="14" y="8" width="18" height="18" rx="4" fill="#EA580C" />
        <text x="23" y="21" font-family="-apple-system, sans-serif" font-size="11" font-weight="900" fill="#FFFFFF" text-anchor="middle">P</text>
        <text x="40" y="21" font-family="-apple-system, sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">S-PPT-maker</text>
        <rect x="135" y="8" width="125" height="18" rx="4" fill="#1E293B" />
        <text x="197" y="20" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="600" fill="#10B981" text-anchor="middle">&#10003; 100% Free &#8226; No Watermark</text>
        <rect x="375" y="7" width="90" height="20" rx="5" fill="#3B82F6" />
        <text x="420" y="20" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">Export PPTX &#10515;</text>
        
        <g transform="translate(14, 44)">
          <rect x="0" y="0" width="75" height="46" rx="4" fill="#1E293B" stroke="#F59E0B" stroke-width="1.8" />
          <rect x="8" y="10" width="40" height="4" rx="2" fill="#F59E0B" />
          <rect x="8" y="18" width="55" height="3" rx="1.5" fill="#64748B" />
          <rect x="8" y="25" width="45" height="3" rx="1.5" fill="#64748B" />
          <rect x="0" y="54" width="75" height="46" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
          <circle cx="25" cy="77" r="10" fill="#334155" />
          <rect x="42" y="70" width="24" height="4" rx="2" fill="#64748B" />
          <rect x="42" y="78" width="20" height="3" rx="1.5" fill="#475569" />
          <rect x="0" y="108" width="75" height="46" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
          <rect x="8" y="118" width="30" height="4" rx="2" fill="#64748B" />
          <rect x="8" y="128" width="58" height="16" rx="2" fill="#1E293B" />
          <rect x="0" y="162" width="75" height="46" rx="4" fill="#0F172A" stroke="#1E293B" stroke-width="1" />
          <rect x="8" y="172" width="45" height="4" rx="2" fill="#64748B" />
        </g>
        
        <g transform="translate(102, 44)">
          <rect width="364" height="210" rx="8" fill="#0B132B" stroke="#1E293B" stroke-width="1.2" />
          <rect x="25" y="20" width="130" height="7" rx="3.5" fill="#F59E0B" />
          <text x="25" y="52" font-family="-apple-system, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">Next-Gen Presentation</text>
          <text x="25" y="72" font-family="-apple-system, sans-serif" font-size="10.5" fill="#94A3B8">Automated clean layout without annoying watermarks or limits.</text>
          
          <rect x="25" y="90" width="95" height="64" rx="6" fill="#131F3B" stroke="#1E293B" stroke-width="1" />
          <text x="35" y="112" font-size="14">&#9889;</text>
          <text x="35" y="128" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#F8FAFC">Instant Export</text>
          <text x="35" y="142" font-family="-apple-system, sans-serif" font-size="7.5" fill="#64748B">One-click PPTX</text>

          <rect x="130" y="90" width="95" height="64" rx="6" fill="#131F3B" stroke="#1E293B" stroke-width="1" />
          <text x="140" y="112" font-size="14">&#127912;</text>
          <text x="140" y="128" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#F8FAFC">Smart Themes</text>
          <text x="140" y="142" font-family="-apple-system, sans-serif" font-size="7.5" fill="#64748B">Curated palettes</text>

          <rect x="235" y="90" width="95" height="64" rx="6" fill="#131F3B" stroke="#1E293B" stroke-width="1" />
          <text x="245" y="112" font-size="14">&#128275;</text>
          <text x="245" y="128" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#F8FAFC">100% Free</text>
          <text x="245" y="142" font-family="-apple-system, sans-serif" font-size="7.5" fill="#64748B">No Watermark</text>

          <rect x="25" y="170" width="305" height="24" rx="5" fill="#1E293B" />
          <text x="177" y="185" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#38BDF8" text-anchor="middle">&#10024; Clean, professional slides ready for conferences &amp; pitches</text>
        </g>
        '''
    elif mock == 'cosmic_portfolio':
        return f'''
        <rect width="480" height="270" rx="14" fill="#04020C" />
        <rect width="480" height="28" fill="#090517" />
        <circle cx="16" cy="14" r="4" fill="#EF4444" />
        <circle cx="28" cy="14" r="4" fill="#F59E0B" />
        <circle cx="40" cy="14" r="4" fill="#10B981" />
        <text x="60" y="18" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#C084FC">&#10022; rishi-cosmic-portfolio.space // galaxy engine</text>
        
        <circle cx="90" cy="70" r="1.5" fill="#FFFFFF" opacity="0.9" />
        <circle cx="150" cy="120" r="1" fill="#00F0FF" opacity="0.8" />
        <circle cx="230" cy="60" r="2" fill="#FFFFFF" opacity="0.8" />
        <circle cx="380" cy="80" r="1.5" fill="#EC4899" opacity="0.9" />
        <circle cx="420" cy="140" r="1" fill="#FFFFFF" opacity="0.7" />
        <circle cx="80" cy="190" r="1.5" fill="#A855F7" opacity="0.8" />
        <circle cx="340" cy="220" r="1.5" fill="#00F0FF" opacity="0.9" />
        <circle cx="450" cy="240" r="2" fill="#FFFFFF" opacity="0.8" />
        
        <ellipse cx="240" cy="145" rx="140" ry="55" fill="#7C3AED" fill-opacity="0.18" filter="url(#node-glow-07)" />
        <ellipse cx="240" cy="145" rx="90" ry="32" fill="#00F0FF" fill-opacity="0.22" filter="url(#node-glow-07)" />
        <ellipse cx="240" cy="145" rx="45" ry="16" fill="#F8FAFC" fill-opacity="0.4" />
        
        <ellipse cx="240" cy="145" rx="190" ry="70" fill="none" stroke="#C084FC" stroke-width="1.2" stroke-dasharray="6 8" opacity="0.5" />
        <ellipse cx="240" cy="145" rx="130" ry="45" fill="none" stroke="#00F0FF" stroke-width="1.5" opacity="0.7" />
        
        <circle cx="330" cy="120" r="12" fill="#EC4899" />
        <circle cx="330" cy="120" r="16" fill="none" stroke="#EC4899" stroke-width="1" opacity="0.6" />
        
        <g transform="translate(110, 75)">
          <rect width="260" height="120" rx="12" fill="#0B081C" fill-opacity="0.85" stroke="#A855F7" stroke-opacity="0.5" stroke-width="1.5" />
          <circle cx="40" cy="40" r="20" fill="#1A1238" stroke="#00F0FF" stroke-width="1.5" />
          <text x="40" y="46" font-size="16" text-anchor="middle">&#129680;</text>
          <text x="72" y="34" font-family="-apple-system, sans-serif" font-size="14" font-weight="800" fill="#F8FAFC">Rishi Shaw</text>
          <text x="72" y="49" font-family="-apple-system, sans-serif" font-size="9" fill="#C084FC">COSMIC ODYSSEY &#8226; 3D PORTFOLIO</text>
          <text x="25" y="76" font-family="-apple-system, sans-serif" font-size="9" fill="#CBD5E1">Interactive WebGL nebula shaders with real-time</text>
          <text x="25" y="90" font-family="-apple-system, sans-serif" font-size="9" fill="#CBD5E1">particle constellations &amp; Three.js physics.</text>
          <rect x="25" y="104" width="80" height="4" rx="2" fill="#00F0FF" />
          <rect x="110" y="104" width="50" height="4" rx="2" fill="#EC4899" />
        </g>
        
        <text x="20" y="255" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748B">RA: 18h 36m &#8226; DEC: +38&#176; 47' &#8226; Three.js Particle Engine</text>
        '''
    elif mock == 'mochu':
        return f'''
        <rect width="480" height="270" rx="14" fill="#0E0916" />
        <rect width="480" height="30" fill="#181124" />
        <circle cx="16" cy="15" r="4" fill="#EF4444" />
        <circle cx="28" cy="15" r="4" fill="#F59E0B" />
        <circle cx="40" cy="15" r="4" fill="#10B981" />
        <text x="60" y="19" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#EC4899">&#9829; Mochu // AI Girl Companion v2.0</text>
        <rect x="380" y="7" width="85" height="18" rx="9" fill="#2E1030" stroke="#EC4899" stroke-width="0.8" />
        <circle cx="390" cy="16" r="3.5" fill="#10B981" />
        <text x="424" y="19" font-family="-apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#F472B6" text-anchor="middle">ONLINE</text>

        <g transform="translate(18, 44)">
          <rect width="140" height="210" rx="10" fill="#1A1028" stroke="#EC4899" stroke-opacity="0.4" stroke-width="1.2" />
          <circle cx="70" cy="65" r="38" fill="#EC4899" fill-opacity="0.15" />
          <circle cx="70" cy="65" r="30" fill="#28163E" stroke="#EC4899" stroke-width="2" />
          <text x="70" y="72" font-size="24" text-anchor="middle">&#129498;</text>
          <text x="70" y="114" font-family="-apple-system, sans-serif" font-size="12" font-weight="800" fill="#F8FAFC" text-anchor="middle">Mochu &#9829;</text>
          <text x="70" y="128" font-family="-apple-system, sans-serif" font-size="8.5" fill="#F472B6" text-anchor="middle">Virtual AI Companion</text>
          
          <rect x="14" y="142" width="112" height="22" rx="6" fill="#110A1B" />
          <text x="22" y="156" font-family="-apple-system, sans-serif" font-size="8" fill="#94A3B8">Affinity: <tspan fill="#EC4899" font-weight="700">99.4%</tspan></text>
          <circle cx="114" cy="153" r="5" fill="#EC4899" />

          <rect x="14" y="170" width="112" height="22" rx="6" fill="#110A1B" />
          <text x="22" y="184" font-family="-apple-system, sans-serif" font-size="8" fill="#94A3B8">Mood: <tspan fill="#A855F7" font-weight="700">Cheerful &#10024;</tspan></text>
        </g>

        <g transform="translate(170, 44)">
          <rect width="292" height="210" rx="10" fill="#140E20" stroke="#1E293B" stroke-width="1" />
          <g transform="translate(14, 16)">
            <rect width="264" height="52" rx="8" fill="#241436" stroke="#EC4899" stroke-opacity="0.3" stroke-width="1" />
            <text x="12" y="20" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#F472B6">Mochu</text>
            <text x="12" y="38" font-family="-apple-system, sans-serif" font-size="9.5" fill="#F8FAFC">"Hey Rishi! How did your project go? I'm</text>
            <text x="12" y="50" font-family="-apple-system, sans-serif" font-size="9.5" fill="#F8FAFC">super excited to build something together! &#10024;"</text>
          </g>
          <g transform="translate(44, 78)">
            <rect width="234" height="34" rx="8" fill="#3B1D54" />
            <text x="12" y="16" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#C084FC">Rishi</text>
            <text x="12" y="28" font-family="-apple-system, sans-serif" font-size="9.5" fill="#FFFFFF">Updating my GitHub profile right now!</text>
          </g>
          <g transform="translate(14, 122)">
            <rect width="264" height="36" rx="8" fill="#241436" stroke="#EC4899" stroke-opacity="0.3" stroke-width="1" />
            <text x="12" y="16" font-family="-apple-system, sans-serif" font-size="9" font-weight="700" fill="#F472B6">Mochu</text>
            <text x="12" y="29" font-family="-apple-system, sans-serif" font-size="9.5" fill="#F8FAFC">"Yay! It's going to look stunning! &#128151;"</text>
          </g>
          <g transform="translate(14, 168)">
            <rect width="264" height="30" rx="6" fill="#0C0714" stroke="#332448" stroke-width="1" />
            <text x="12" y="19" font-family="-apple-system, sans-serif" font-size="9" fill="#64748B">Type a message to Mochu...</text>
            <rect x="226" y="6" width="30" height="18" rx="4" fill="#EC4899" />
            <text x="241" y="18" font-size="10" fill="#FFFFFF" text-anchor="middle">&#10148;</text>
          </g>
        </g>
        '''
    return ''

for spec in projects_spec:
    num = spec['num']
    orientation = spec['orientation']
    title = spec['title']
    category = spec['category']
    desc_1 = spec['desc_1']
    desc_2 = spec['desc_2']
    badges = spec['badges']
    demo_url = spec.get('demo_url', 'https://github.com/Rishi-Dev-pro')
    repo_url = spec.get('repo_url', 'https://github.com/Rishi-Dev-pro')
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

    row_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 340" width="100%" height="340">
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
  <a href="{demo_url}" xlink:href="{demo_url}" target="_blank" style="cursor: pointer;">
    <g transform="translate({screenshot_x}, 35)" filter="url(#card-shadow-{num})">
      <rect width="480" height="270" rx="16" fill="#0A0F1E" stroke="url(#ss-border-{num})" stroke-width="1.8" />
      {artwork}
    </g>
  </a>

  <!-- Project Description Card -->
  <g transform="translate({desc_x}, 50)">
    <a href="{repo_url}" xlink:href="{repo_url}" target="_blank" style="cursor: pointer;">
      <text x="0" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" fill="{c1}">{title}</text>
    </a>
    <text x="0" y="60" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" font-weight="600" fill="#94A3B8">{category}</text>
    
    <text x="0" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14.5" fill="#CBD5E1">
      <tspan x="0" dy="0">{desc_1}</tspan>
      <tspan x="0" dy="24">{desc_2}</tspan>
    </text>

    <!-- Badges -->
    <g transform="translate(0, 155)">
      {badges_xml}
    </g>

    <!-- Action Links (Individually clickable buttons) -->
    <g transform="translate(0, 215)">
      <a href="{demo_url}" xlink:href="{demo_url}" target="_blank" style="cursor: pointer;">
        <rect x="0" y="-18" width="95" height="26" fill="#000000" fill-opacity="0.01" />
        <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8">Live Demo ↗</text>
      </a>
      <text x="96" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#64748B">   |   </text>
      <a href="{repo_url}" xlink:href="{repo_url}" target="_blank" style="cursor: pointer;">
        <rect x="125" y="-18" width="80" height="26" fill="#000000" fill-opacity="0.01" />
        <text x="135" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#38BDF8">GitHub ↗</text>
      </a>
    </g>
  </g>
</svg>"""

    out_path = f'assets/profile-svgs/project-row-{num}.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(row_svg)

    ET.fromstring(row_svg)
    print(f"Project row {num} ({title}): VALID XML!")

print("\nALL SVGs generated and validated successfully!")
