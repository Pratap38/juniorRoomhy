import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Logo in footer
content = content.replace('<div class="flex items-end">\n                      <svg width="45" height="32" viewBox="0 0 50 40"', '<div class="flex items-end shrink-0">\n                      <svg class="shrink-0" width="50" height="40" viewBox="0 0 50 40"')

# Sometimes the formatter changed indentation, let's use regex
content = re.sub(
    r'<div class="flex items-end">\s*<svg width="45" height="32" viewBox="0 0 50 40"',
    r'<div class="flex items-end shrink-0">\n                      <svg class="shrink-0" width="50" height="40" viewBox="0 0 50 40"',
    content
)

# 2. Update Social Icons in Footer
facebook_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>'
linkedin_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>'
instagram_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'

content = re.sub(r'<i data-lucide="facebook" class="w-4 h-4"><\/i>', facebook_svg, content)
content = re.sub(r'<i data-lucide="linkedin" class="w-4 h-4"><\/i>', linkedin_svg, content)
content = re.sub(r'<i data-lucide="instagram" class="w-4 h-4"><\/i>', instagram_svg, content)


# 3. Clean Quick Links
# Remove the chevron-right icons in footer
# It may be over multiple lines due to formatting
content = re.sub(
    r'<i data-lucide="chevron-right"[^>]*></i>',
    '',
    content,
    flags=re.IGNORECASE | re.DOTALL
)

# 4. Add the world map texture in Footer
world_map_html = r'''<!-- Subtle Background Pattern -->
       <div class="absolute right-0 bottom-0 opacity-10 pointer-events-none w-[600px] h-[400px]" style="background-image: radial-gradient(circle at center, transparent, transparent 4px, #D89A18 4px, #D89A18 5px); background-size: 20px 20px; mask-image: radial-gradient(circle at 50% 50%, black, transparent 70%); -webkit-mask-image: radial-gradient(circle at 50% 50%, black, transparent 70%);"></div>
       <div class="absolute inset-0 bg-dotted opacity-[0.05] pointer-events-none"></div>'''
       
content = re.sub(
    r'<!-- Subtle Background Pattern -->\s*<div class="absolute inset-0 bg-dotted opacity-\[0.05\] pointer-events-none"></div>',
    world_map_html,
    content
)

with open('index.html', 'w') as f:
    f.write(content)
print("patched")
