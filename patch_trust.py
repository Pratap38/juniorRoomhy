import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Trust Strip HTML
old_trust = """                <div
                    class="bg-[#0D1B14] rounded-[20px] py-[44px] px-[48px] text-white shadow-2xl flex items-center justify-between">
                    <!-- Point 1 -->
                    <div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1">
                        <div class="text-[#D89A18] mt-1">
                            <i data-lucide="shield-check" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                        </div>
                        <div>
                            <h4 class="font-[800] text-[17px] mb-2">Safe & Secure</h4>
                            <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[180px] font-[450]">Your cargo is
                                protected with safety-first approach.</p>
                        </div>
                    </div>
                    <!-- Separator -->
                    <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                    <!-- Point 2 -->
                    <div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1 pl-0 lg:pl-4">
                        <div class="text-[#D89A18] mt-1">
                            <i data-lucide="clock" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                        </div>
                        <div>
                            <h4 class="font-[800] text-[17px] mb-2">On-Time Delivery</h4>
                            <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[190px] font-[450]">We value time
                                and ensure punctual deliveries.</p>
                        </div>
                    </div>
                    <!-- Separator -->
                    <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                    <!-- Point 3 -->
                    <div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1 pl-0 lg:pl-4">
                        <div class="text-[#D89A18] mt-1">
                            <i data-lucide="globe" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                        </div>
                        <div>
                            <h4 class="font-[800] text-[17px] mb-2">Wide Coverage</h4>
                            <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[190px] font-[450]">Extensive
                                network across regional and global routes.</p>
                        </div>
                    </div>
                    <!-- Separator -->
                    <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                    <!-- Point 4 -->
                    <div class="flex items-start gap-4 w-full md:w-[45%] lg:w-auto flex-none lg:flex-1 pl-0 lg:pl-4">
                        <div class="text-[#D89A18] mt-1">
                            <i data-lucide="headphones" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                        </div>
                        <div>
                            <h4 class="font-[800] text-[17px] mb-2">24/7 Support</h4>
                            <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[190px] font-[450]">Our team is
                                always here to assist you.</p>
                        </div>
                    </div>
                </div>"""

new_trust = """                <div class="bg-[#0D1B14] rounded-[24px] py-8 lg:py-[44px] px-6 lg:px-[48px] text-white shadow-2xl relative">
                    <!-- Mobile Swiper container -->
                    <div class="swiper trust-swiper w-full overflow-hidden">
                        <div class="swiper-wrapper flex lg:items-center lg:justify-between h-full w-full">
                            
                            <!-- Point 1 -->
                            <div class="swiper-slide w-full h-auto !flex items-start gap-4 lg:w-auto flex-none lg:flex-1">
                                <div class="text-[#D89A18] mt-1">
                                    <i data-lucide="shield-check" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                                </div>
                                <div class="flex flex-col">
                                    <h4 class="font-[800] text-[17px] mb-2">Safe & Secure</h4>
                                    <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[200px] lg:max-w-[180px] font-[450]">Your cargo is protected with safety-first approach.</p>
                                </div>
                            </div>
                            
                            <!-- Separator -->
                            <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                            
                            <!-- Point 2 -->
                            <div class="swiper-slide w-full h-auto !flex items-start gap-4 lg:w-auto flex-none lg:flex-1 lg:pl-4">
                                <div class="text-[#D89A18] mt-1">
                                    <i data-lucide="clock" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                                </div>
                                <div class="flex flex-col">
                                    <h4 class="font-[800] text-[17px] mb-2">On-Time Delivery</h4>
                                    <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[200px] lg:max-w-[190px] font-[450]">We value time and ensure punctual deliveries.</p>
                                </div>
                            </div>
                            
                            <!-- Separator -->
                            <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                            
                            <!-- Point 3 -->
                            <div class="swiper-slide w-full h-auto !flex items-start gap-4 lg:w-auto flex-none lg:flex-1 lg:pl-4">
                                <div class="text-[#D89A18] mt-1">
                                    <i data-lucide="globe" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                                </div>
                                <div class="flex flex-col">
                                    <h4 class="font-[800] text-[17px] mb-2">Wide Coverage</h4>
                                    <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[200px] lg:max-w-[190px] font-[450]">Extensive network across regional and global routes.</p>
                                </div>
                            </div>
                            
                            <!-- Separator -->
                            <div class="w-px h-14 bg-gray-800/80 mx-2 hidden lg:block"></div>
                            
                            <!-- Point 4 -->
                            <div class="swiper-slide w-full h-auto !flex items-start gap-4 lg:w-auto flex-none lg:flex-1 lg:pl-4">
                                <div class="text-[#D89A18] mt-1">
                                    <i data-lucide="headphones" class="w-[34px] h-[34px] stroke-[1.5]"></i>
                                </div>
                                <div class="flex flex-col">
                                    <h4 class="font-[800] text-[17px] mb-2">24/7 Support</h4>
                                    <p class="text-gray-400 text-[14px] leading-[1.6] max-w-[200px] lg:max-w-[190px] font-[450]">Our team is always here to assist you.</p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>"""

text = text.replace(old_trust, new_trust)

# Add Swiper initialization script at the bottom for Trust Strip
script_addition = """
        // Trust Strip Swiper (Mobile Only)
        const trustSwiper = new Swiper('.trust-swiper', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            autoplay: {
                delay: 2500,
                disableOnInteraction: false,
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30
                },
                1024: {
                    enabled: false,           // Disables Swiper mechanics entirely on desktop
                    slidesPerView: 'auto',
                    spaceBetween: 0
                }
            }
        });
"""
text = text.replace("if(openMenuBtn) {", script_addition + "\n        if(openMenuBtn) {")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Trust strip converted!")
