import re

with open('index.html', 'r') as f:
    html = f.read()

def rb(old, new):
    global html
    html = html.replace(old, new)


# --- 1. Nav & Headers ---
# Utility bar
rb('<div class="bg-[#0D1B14] h-[45px] text-white flex items-center justify-between px-6 text-[13px]">', 
   '<div class="bg-[#0D1B14] h-auto min-h-[45px] text-white flex items-center justify-between px-6 text-[13px] py-2 lg:py-0 hidden lg:flex">')
# Menu (hide on mobile)
rb('<ul class="flex items-center gap-10 font-bold text-[15px] text-[#141414] h-full">',
   '<ul class="hidden lg:flex items-center gap-10 font-bold text-[15px] text-[#141414] h-full">')
# CTA Button in Nav
rb('<a href="#" class="bg-[#D89A18] text-white font-[600] flex items-center gap-2 px-7 py-3.5 rounded-lg hover:bg-[#c28815] transition-all shadow-md tracking-wide">',
   '<a href="#" class="hidden lg:flex bg-[#D89A18] text-white font-[600] items-center gap-2 px-7 py-3.5 rounded-lg hover:bg-[#c28815] transition-all shadow-md tracking-wide">')
# Mobile Menu Icon
rb('</nav>', 
   '  <button class="block lg:hidden absolute right-6 top-[35px] text-[#141414]"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>\n</nav>')
   
# --- 2. Hero Section ---
rb('<!-- Hero Section -->\n    <div class="relative bg-[#FDFBF7]" style="height: 860px;">',
   '<!-- Hero Section -->\n    <div class="relative bg-[#FDFBF7] min-h-screen lg:min-h-0 lg:h-[860px] py-16 lg:py-0">')
rb('<div class="absolute top-0 right-0 w-[58%] h-full z-0 overflow-hidden">',
   '<div class="absolute top-0 right-0 w-full lg:w-[58%] h-full z-0 overflow-hidden opacity-10 lg:opacity-100">')
rb('<h1 class="text-[74px] leading-[1.05] font-[800] text-[#141414] mb-8 tracking-[-0.02em]">',
   '<h1 class="text-[48px] lg:text-[74px] leading-[1.05] font-[800] text-[#141414] mb-8 tracking-[-0.02em]">')
rb('<div class="flex items-center gap-6 mb-12">',
   '<div class="flex flex-col sm:flex-row items-center sm:items-start gap-4 sm:gap-6 mb-12">')
# Trust strip
rb('<div class="absolute -bottom-16 left-0 w-full z-20 px-8">',
   '<div class="relative lg:absolute mt-12 lg:mt-0 -bottom-16 left-0 w-full z-20 px-4 lg:px-8">')
rb('<div class="bg-[#0D1B14] rounded-[20px] py-[44px] px-[48px] text-white shadow-2xl flex items-center justify-between">',
   '<div class="bg-[#0D1B14] rounded-[20px] py-8 lg:py-[44px] px-8 lg:px-[48px] text-white shadow-2xl flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8 lg:gap-0">')
rb('<div class="w-px h-14 bg-gray-800/80 mx-2"></div>',
   '<div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>')

# --- 3. Section 1 (Why SinghRJ) ---
rb('<div class="pt-[220px] pb-[120px] relative bg-[#FDFBF7] overflow-hidden">',
   '<div class="pt-24 lg:pt-[220px] pb-16 lg:pb-[120px] relative bg-[#FDFBF7] overflow-hidden">')
rb('<h2 class="text-[52px] leading-[1.1] font-[800] text-[#141414] mb-12 tracking-[-0.02em]">',
   '<h2 class="text-[36px] lg:text-[52px] leading-[1.1] font-[800] text-[#141414] mb-8 lg:mb-12 tracking-[-0.02em]">')
rb('<div class="w-full lg:w-[52%] relative pl-12 h-full flex flex-col justify-center">',
   '<div class="w-full lg:w-[52%] relative pl-0 lg:pl-12 h-full flex flex-col justify-center mt-12 lg:mt-0">')
rb('<div class="absolute -bottom-8 left-4 bg-[#D89A18]',
   '<div class="absolute bottom-4 left-4 lg:-bottom-8 lg:left-4 bg-[#D89A18]')

# --- 4. Section 2 (Process) ---
rb('<h2 class="text-[44px] leading-[1.1] font-[800] text-[#141414] mb-5 tracking-[-0.02em]">',
   '<h2 class="text-[32px] lg:text-[44px] leading-[1.1] font-[800] text-[#141414] mb-5 tracking-[-0.02em]">')
rb('<div class="absolute top-[52px] left-[10%] right-[10%] h-[2px] bg-[#D89A18]/30 z-0"></div>',
   '<div class="hidden lg:block absolute top-[52px] left-[10%] right-[10%] h-[2px] bg-[#D89A18]/30 z-0"></div>')
rb('<div class="grid grid-cols-4 gap-6 relative z-10">',
   '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-6 relative z-10">')
rb('class="absolute top-[46px]', 'class="hidden lg:block absolute top-[46px]')

# --- 5. Services Section ---
rb('<div class="bg-[#FDFBF7] pt-[120px] pb-[120px]">',
   '<div class="bg-[#FDFBF7] pt-16 lg:pt-[120px] pb-16 lg:pb-[120px]">')
rb('<div class="grid grid-cols-12 gap-12 items-start">',
   '<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">')
rb('<div class="col-span-3 pr-2 position-relative pt-4">',
   '<div class="col-span-1 lg:col-span-3 pr-0 lg:pr-2 position-relative pt-4 text-center lg:text-left">')
rb('<div class="col-span-9">',
   '<div class="col-span-1 lg:col-span-9">')
rb('<div class="grid grid-cols-4 gap-6">',
   '<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6">')

# --- 6. Metrics Bar ---
rb('<div class="content-container flex items-center justify-between px-16">',
   '<div class="content-container flex flex-wrap items-center justify-between gap-8 px-4 lg:px-16">')
rb('<div class="w-px h-16 bg-gray-200"></div>',
   '<div class="hidden lg:block w-px h-16 bg-gray-200"></div>')

# --- 7. Testimonials ---
rb('<h2 class="text-[44px] leading-[1.1] font-[800] text-[#141414] mb-3 tracking-[-0.02em] text-center">',
   '<h2 class="text-[32px] lg:text-[44px] leading-[1.1] font-[800] text-[#141414] mb-3 tracking-[-0.02em] text-center">')
rb('w-[420px]', 'w-[320px] sm:w-[420px]')
rb('<div class="swiper-button-prev !w-[50px] !h-[50px]', '<div class="hidden lg:flex swiper-button-prev !w-[50px] !h-[50px]')
rb('<div class="swiper-button-next !w-[50px] !h-[50px]', '<div class="hidden lg:flex swiper-button-next !w-[50px] !h-[50px]')


# --- 8. CTA Section ---
rb('<div class="bg-[#FCFBF8] pb-[120px]">',
   '<div class="bg-[#FCFBF8] pb-16 lg:pb-[120px]">')
rb('<div class="relative bg-[#0E1B14] rounded-[30px] overflow-hidden p-16 lg:px-24 lg:py-20',
   '<div class="relative bg-[#0E1B14] rounded-[24px] lg:rounded-[30px] overflow-hidden p-8 py-16 lg:px-24 lg:py-20')
rb('<h2 class="text-[52px] leading-[1.1] font-[800] text-white mb-6 tracking-tight">',
   '<h2 class="text-[36px] lg:text-[52px] leading-[1.1] font-[800] text-white mb-6 tracking-tight">')
rb('<div class="flex flex-col sm:flex-row items-center justify-center gap-6">',
   '<div class="flex flex-col w-full sm:w-auto sm:flex-row items-center justify-center gap-4 lg:gap-6">')
rb('min-w-[240px]', 'w-full lg:w-auto min-w-[240px]')

# Footer grid already responsive


with open('index.html', 'w') as f:
    f.write(html)
print("Made responsive!")
