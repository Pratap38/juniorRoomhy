import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def rb(old, new):
    global html
    html = html.replace(old, new)


# 1. Update Testimonials script specifically, as Swiper config needs breakpoints
old_swiper = """        const swiper = new Swiper('.testimonial-swiper', {
           slidesPerView: 'auto',
           spaceBetween: 30,
           centeredSlides: true,
           loop: true,
           speed: 5000,"""
new_swiper = """        const swiper = new Swiper('.testimonial-swiper', {
           slidesPerView: 1,
           spaceBetween: 20,
           breakpoints: {
              768: { slidesPerView: 2, spaceBetween: 30 },
              1200: { slidesPerView: 'auto', spaceBetween: 30 }
           },
           centeredSlides: true,
           loop: true,
           speed: 5000,"""
rb(old_swiper, new_swiper)

# 2. Add Mobile Menu markup right after <nav ...> ... </nav> block
# We need to find the closing </nav>
mobile_menu = """</nav>

    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-[#0D1B14]/90 backdrop-blur-lg z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
       <div class="flex justify-between items-center p-6 border-b border-white/10">
          <div class="text-white font-extrabold text-[22px]">SINGHRJ<span class="text-[#D89A18] text-[10px] uppercase ml-2 tracking-widest block">Transport</span></div>
          <button id="close-menu" class="text-white p-2">
             <i data-lucide="x" class="w-8 h-8"></i>
          </button>
       </div>
       <ul class="flex flex-col gap-6 text-white text-[22px] font-[600] p-8">
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Home</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">About Us</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Services</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Why Us</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Pricing Plan</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Tracking</a></li>
          <li><a href="#" class="hover:text-[#D89A18] transition-colors">Contact Us</a></li>
       </ul>
       <div class="mt-auto p-8 border-t border-white/10">
          <a href="#" class="bg-[#D89A18] text-white font-[600] flex items-center justify-center gap-2 w-full py-4 rounded-xl shadow-lg">
             Get a Quote <i data-lucide="arrow-right" class="w-5 h-5"></i>
          </a>
       </div>
    </div>
"""
rb('</nav>', mobile_menu)

# 3. Add Mobile Menu Toggle logic to scripts
old_scripts = """    <script>
        lucide.createIcons();"""
new_scripts = """    <script>
        lucide.createIcons();

        // Mobile Menu Logic
        const mobileMenu = document.getElementById('mobile-menu');
        const openMenuBtn = document.getElementById('open-menu');
        const closeMenuBtn = document.getElementById('close-menu');
        
        if(openMenuBtn) {
            openMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-full');
                document.body.style.overflow = 'hidden';
            });
        }
        if(closeMenuBtn) {
            closeMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
                document.body.style.overflow = '';
            });
        }
"""
rb(old_scripts, new_scripts)

# Note: We need to assign ID to the hamburger button added in previous step
rb('<button class="block lg:hidden absolute right-6 top-[35px] text-[#141414]">',
   '<button id="open-menu" class="block lg:hidden absolute right-6 top-[35px] text-[#141414] p-2 -mr-2">')

# 4. Enhance typography & padding scaling deeper

# Hero Text
rb('<h1 class="text-[48px] lg:text-[74px] leading-[1.05] font-[800] text-[#141414] mb-8 tracking-[-0.02em]">',
   '<h1 class="text-[40px] md:text-[56px] lg:text-[74px] leading-[1.1] lg:leading-[1.05] font-[800] text-[#141414] mb-6 lg:mb-8 tracking-[-0.02em]">')
rb('<p class="text-[#666666] font-[450] text-[19px] mb-12 text-balance leading-[1.6]">',
   '<p class="text-[#666666] font-[450] text-[16px] md:text-[19px] mb-8 lg:mb-12 text-balance leading-[1.6]">')
rb('<div class="flex flex-col sm:flex-row items-center sm:items-start gap-4 sm:gap-6 mb-12">',
   '<div class="flex flex-col w-full sm:w-auto sm:flex-row items-stretch sm:items-start gap-4 sm:gap-6 mb-12">')
rb('<a href="#" class="bg-[#D89A18] text-white font-[600] flex items-center gap-3 px-8 py-4 rounded-[10px]',
   '<a href="#" class="bg-[#D89A18] text-white font-[600] flex items-center justify-center gap-3 px-8 py-4 rounded-[10px] w-full sm:w-auto')
rb('<a href="#" class="bg-white border-[1.5px] border-gray-200 text-[#141414] font-[600] flex items-center gap-2 px-8 py-4 rounded-[10px]',
   '<a href="#" class="bg-white border-[1.5px] border-gray-200 text-[#141414] font-[600] flex items-center justify-center gap-2 px-8 py-4 rounded-[10px] w-full sm:w-auto')

# Trust Strip content on mobile
rb('<div class="bg-[#0D1B14] rounded-[20px] py-8 lg:py-[44px] px-8 lg:px-[48px] text-white shadow-2xl flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8 lg:gap-0">',
   '<div class="bg-[#0D1B14] rounded-[20px] py-10 lg:py-[44px] px-6 lg:px-[48px] text-white shadow-2xl flex flex-col md:flex-row md:flex-wrap lg:flex-nowrap items-start lg:items-center justify-between gap-8 lg:gap-0">')
rb('<div class="flex items-start gap-4 flex-1">',
   '<div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1">')
rb('<div class="flex items-start gap-4 flex-1 pl-4">',
   '<div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1 pl-0 lg:pl-4">')

# Section 1 (Why Us)
rb('<h2 class="text-[36px] lg:text-[52px]', '<h2 class="text-[32px] md:text-[44px] lg:text-[52px]')

# Footer Centering for Mobile
rb('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8 mb-20">',
   '<div class="grid grid-cols-1 text-center md:text-left md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8 mb-20">')
rb('<div class="flex flex-col pr-6">',
   '<div class="flex flex-col items-center md:items-start pr-0 lg:pr-6">')
rb('<div class="flex items-center gap-3 mb-6">',
   '<div class="flex items-center justify-center md:justify-start gap-3 mb-6">')
rb('<div class="flex items-center gap-3">',
   '<div class="flex items-center justify-center md:justify-start gap-3">')
rb('<li class="flex items-start gap-4">',
   '<li class="flex items-start justify-center md:justify-start gap-4">')
rb('<i data-lucide="map-pin" class="w-5 h-5 text-[#D89A18] shrink-0 mt-0.5"></i>\n                            <span class="text-gray-400 font-[450] text-[14px] leading-relaxed">',
   '<i data-lucide="map-pin" class="w-5 h-5 text-[#D89A18] shrink-0 mt-0.5"></i>\n                            <span class="text-gray-400 font-[450] text-[14px] leading-relaxed text-left">')

# Metrics Centering Mobile
rb('<div class="content-container flex flex-wrap items-center justify-between gap-8 px-4 lg:px-16">',
   '<div class="content-container flex flex-col md:flex-row flex-wrap items-center justify-center md:justify-between gap-10 px-4 lg:px-16">')
rb('<div class="flex items-center gap-5">',
   '<div class="flex flex-col md:flex-row items-center text-center md:text-left gap-4 md:gap-5">')
   
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Mobile Menu and deep responsive layers injected successfully.")
