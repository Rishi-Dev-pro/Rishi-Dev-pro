import base64
import os
import xml.etree.ElementTree as ET

os.makedirs('assets/profile-svgs', exist_ok=True)

def to_base64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return None

# Load available PNG screenshots
aether_b64 = to_base64('assets/screenshots/aether-os.png')
callbuddy_b64 = to_base64('assets/screenshots/callbuddy-ai-1.png')
fourpillars_b64 = to_base64('assets/screenshots/the-four-pillars.png')

print(f"Loaded aether: {bool(aether_b64)}, callbuddy: {bool(callbuddy_b64)}, fourpillars: {bool(fourpillars_b64)}")
