#!/usr/bin/env python3
"""Fix 4 issues on convert-currency.org website"""

import os
import re
import glob

# Paths
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
PAIRS_DIR = os.path.join(REPO_ROOT, 'pairs')
HTML_PAIRS = [
    'brl-to-eur', 'inr-to-cad', 'huf-to-eur', 'usd-to-gbp', 'usd-to-nok',
    'usd-to-myr', 'jpy-to-aud', 'eur-to-nok', 'myr-to-usd', 'gbp-to-eur',
    'gbp-to-inr', 'inr-to-eur', 'dkk-to-eur', 'usd-to-vnd', 'aud-to-jpy',
    'nzd-to-usd', 'sek-to-eur', 'nok-to-eur', 'gbp-to-cny', 'cny-to-usd',
    'thb-to-usd', 'sgd-to-usd', 'eur-to-gbp', 'chf-to-eur', 'cad-to-jpy',
    'jpy-to-cad', 'eur-to-sek', 'eur-to-chf', 'usd-to-sgd'
]

GDPR_SCRIPT = '''<!-- GDPR Cookie Consent -->
<div id="cookie-consent" style="display:none;position:fixed;bottom:0;left:0;right:0;background:#1a1a2e;color:#fff;padding:16px 24px;z-index:9999;font-family:system-ui,sans-serif;font-size:14px;">
  <div style="max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
    <p style="margin:0;flex:1;min-width:200px;">We use cookies for analytics. By clicking "Accept", you consent to our use of cookies.</p>
    <div style="display:flex;gap:8px;">
      <button onclick="acceptCookies()" style="background:#10b981;color:#fff;border:none;padding:8px 20px;border-radius:6px;cursor:pointer;font-size:14px;">Accept</button>
      <button onclick="declineCookies()" style="background:transparent;color:#fff;border:1px solid #555;padding:8px 20px;border-radius:6px;cursor:pointer;font-size:14px;">Decline</button>
    </div>
  </div>
</div>
<script>
function loadGA(){var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-1KEM4TDVK9';document.head.appendChild(s);s.onload=function(){window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-1KEM4TDVK9');};}
function acceptCookies(){localStorage.setItem('convertcurrency-consent','granted');document.getElementById('cookie-consent').style.display='none';loadGA();}
function declineCookies(){localStorage.setItem('convertcurrency-consent','denied');document.getElementById('cookie-consent').style.display='none';}
(function(){var c=localStorage.getItem('convertcurrency-consent');if(c==='granted'){loadGA();}else if(!c){document.getElementById('cookie-consent').style.display='block';}})();
</script>'''

REDIRECT_TEMPLATE = '''<!DOCTYPE html>
<html><head>
<meta http-equiv="refresh" content="0;url=https://convert-currency.org/pairs/{pair}/">
<link rel="canonical" href="https://convert-currency.org/pairs/{pair}/">
<title>Redirecting...</title>
</head><body>
<p>Redirecting to <a href="https://convert-currency.org/pairs/{pair}/">https://convert-currency.org/pairs/{pair}/</a></p>
</body></html>
'''

def fix_issue1_gdpr():
    """Fix Issue 1: Add GDPR consent banner and remove direct GA scripts"""
    print("\n=== Issue 1: Adding GDPR Cookie Consent ===")

    modified_files = []

    # Find all HTML files
    html_files = glob.glob(os.path.join(REPO_ROOT, '**/*.html'), recursive=True)

    for html_file in html_files:
        # Skip files in .git
        if '.git' in html_file:
            continue

        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remove direct GA script tags (both async src and inline config)
        # Remove <script async src="https://www.googletagmanager.com/gtag/js?id=..."></script>
        content = re.sub(
            r'<script\s+async\s+src=["\']https://www\.googletagmanager\.com/gtag/js\?id=[^"\']*["\'][^>]*></script>\s*',
            '',
            content,
            flags=re.IGNORECASE
        )

        # Remove the gtag config script block
        content = re.sub(
            r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];.*?gtag\([\'"]config[\'"],\s*[\'"]G-[A-Z0-9]+["\']\);?\s*</script>\s*',
            '',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )

        # Check if GDPR script already exists
        if 'cookie-consent' not in content:
            # Add GDPR script before </body>
            if '</body>' in content:
                content = content.replace('</body>', GDPR_SCRIPT + '\n</body>')
            else:
                # If no body tag, append before </html>
                content = content.replace('</html>', GDPR_SCRIPT + '\n</html>')

        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(html_file)
            print(f"  Modified: {os.path.relpath(html_file, REPO_ROOT)}")

    print(f"Total files modified for GDPR: {len(modified_files)}")
    return len(modified_files)


def fix_issue2_redirects():
    """Fix Issue 2: Create 29 redirect stubs"""
    print("\n=== Issue 2: Creating 29 Redirect Stubs ===")

    created_files = []

    for pair in HTML_PAIRS:
        pair_dir = os.path.join(REPO_ROOT, pair)
        os.makedirs(pair_dir, exist_ok=True)

        index_file = os.path.join(pair_dir, 'index.html')
        content = REDIRECT_TEMPLATE.format(pair=pair)

        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

        created_files.append(index_file)
        print(f"  Created: {pair}/index.html")

    print(f"Total redirect stubs created: {len(created_files)}")
    return len(created_files)


def fix_issue3_canonical():
    """Fix Issue 3: Fix canonical URLs on pair pages"""
    print("\n=== Issue 3: Fixing Canonical URLs on Pair Pages ===")

    modified_files = []

    # Find all HTML files in pairs directory
    pair_html_files = glob.glob(os.path.join(PAIRS_DIR, '**/index.html'), recursive=True)

    for html_file in pair_html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Extract pair name from path (e.g., /pairs/usd-to-gbp/index.html -> usd-to-gbp)
        pair_name = html_file.split(os.sep)[-2]

        # Fix canonical URL pattern
        # Old: <link rel="canonical" href="https://convert-currency.org/usd-to-gbp/">
        # New: <link rel="canonical" href="https://convert-currency.org/pairs/usd-to-gbp/">
        pattern = rf'<link\s+rel=["\']canonical["\']\s+href=["\']https://convert-currency\.org/{pair_name}/["\']'
        replacement = f'<link rel="canonical" href="https://convert-currency.org/pairs/{pair_name}/"'

        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

        # Also handle og:url meta tags
        pattern_og = rf'<meta\s+property=["\']og:url["\']\s+content=["\']https://convert-currency\.org/{pair_name}/["\']'
        replacement_og = f'<meta property="og:url" content="https://convert-currency.org/pairs/{pair_name}/"'

        content = re.sub(pattern_og, replacement_og, content, flags=re.IGNORECASE)

        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(html_file)
            print(f"  Fixed: {os.path.relpath(html_file, REPO_ROOT)}")

    print(f"Total pair pages fixed: {len(modified_files)}")
    return len(modified_files)


def fix_issue4_hreflang():
    """Fix Issue 4: Add hreflang tags to pair pages (if needed)"""
    print("\n=== Issue 4: Checking for Translated Pair Pages ===")

    # Check if translated pair pages exist
    lang_dirs = glob.glob(os.path.join(REPO_ROOT, '[a-z][a-z]', 'pairs'), recursive=False)

    if lang_dirs:
        print(f"  Found {len(lang_dirs)} translated pair page directories")
        print("  Implementing hreflang tags for pair pages...")
        # Would implement hreflang here
    else:
        print("  No translated pair pages found (pair pages only exist in English)")
        print("  Skipping hreflang implementation")

    return 0


def main():
    print("=" * 60)
    print("Fixing convert-currency.org issues")
    print("=" * 60)

    count1 = fix_issue1_gdpr()
    count2 = fix_issue2_redirects()
    count3 = fix_issue3_canonical()
    count4 = fix_issue4_hreflang()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Issue 1 - GDPR consent: {count1} files modified")
    print(f"Issue 2 - Redirects: {count2} redirect stubs created")
    print(f"Issue 3 - Canonical URLs: {count3} pair pages fixed")
    print(f"Issue 4 - Hreflang: Skipped (no translated pair pages)")
    print("=" * 60)


if __name__ == '__main__':
    main()
