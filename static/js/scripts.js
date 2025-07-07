document.addEventListener("DOMContentLoaded", () => {
    // ========== Accordion Toggle ==========
    const toggles = document.querySelectorAll(".accordion-toggle");

    toggles.forEach(toggle => {
        toggle.addEventListener("click", () => {
            const content = toggle.closest(".accordion-item").querySelector(".accordion-content");

            // Close all others
            document.querySelectorAll(".accordion-content").forEach(c => c.classList.remove("open"));
            document.querySelectorAll(".accordion-toggle").forEach(t => t.classList.remove("active"));

            // Open selected
            toggle.classList.add("active");
            content.classList.add("open");
        });
    });

    // Auto-expand accordion from hash
    const hash = window.location.hash;
    if (hash) {
        const target = document.querySelector(hash);
        if (target && target.classList.contains("accordion-item")) {
            const button = target.querySelector(".accordion-toggle");
            const content = target.querySelector(".accordion-content");

            document.querySelectorAll(".accordion-content").forEach(c => c.classList.remove("open"));
            document.querySelectorAll(".accordion-toggle").forEach(t => t.classList.remove("active"));

            content.classList.add("open");
            button.classList.add("active");

            target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    }

    // ========== Carousel Auto-Slider ==========
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentIndex = 0;
    let interval;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    function startAutoSlide() {
        interval = setInterval(nextSlide, 4000); // every 4 sec
    }

    function stopAutoSlide() {
        clearInterval(interval);
    }

    if (slides.length > 1) {
        showSlide(currentIndex);
        startAutoSlide();

        if (nextBtn && prevBtn) {
            nextBtn.addEventListener('click', () => {
                stopAutoSlide();
                nextSlide();
                startAutoSlide();
            });

            prevBtn.addEventListener('click', () => {
                stopAutoSlide();
                prevSlide();
                startAutoSlide();
            });
        }
    }
});
