// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled', 'shadow-sm');
                navbar.style.padding = '0.5rem 0';
            } else {
                navbar.classList.remove('navbar-scrolled', 'shadow-sm');
                navbar.style.padding = '1rem 0';
            }
        });
    }

    // Portfolio filtering
    const filterButtons = document.querySelectorAll('.filter-btn');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    if (filterButtons.length > 0 && portfolioItems.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));

                // Add active class to clicked button
                this.classList.add('active');

                // Get filter value
                const filterValue = this.getAttribute('data-filter');

                // Filter portfolio items
                portfolioItems.forEach(item => {
                    if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                        item.style.display = 'block';
                        setTimeout(() => {
                            item.style.opacity = '1';
                            item.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        item.style.opacity = '0';
                        item.style.transform = 'scale(0.8)';
                        setTimeout(() => {
                            item.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }

    // Testimonial carousels
    const testimonialCarouselMobile = document.querySelector('#testimonialCarouselMobile');
    if (testimonialCarouselMobile) {
        new bootstrap.Carousel(testimonialCarouselMobile, {
            interval: 5000,
            wrap: true
        });
    }

    // Show More Testimonials button
    const showMoreTestimonialsBtn = document.querySelector('#showMoreTestimonials');
    if (showMoreTestimonialsBtn) {
        showMoreTestimonialsBtn.addEventListener('click', function() {
            // Create a modal with all testimonials in a carousel
            const modal = document.createElement('div');
            modal.classList.add('modal', 'fade');
            modal.id = 'allTestimonialsModal';
            modal.setAttribute('tabindex', '-1');
            modal.setAttribute('aria-labelledby', 'allTestimonialsModalLabel');
            modal.setAttribute('aria-hidden', 'true');

            // Get all testimonials
            const testimonials = document.querySelectorAll('.testimonial');

            // Create modal content
            modal.innerHTML = `
                <div class="modal-dialog modal-lg modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="allTestimonialsModalLabel">All Testimonials</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div id="allTestimonialsCarousel" class="carousel slide" data-bs-ride="carousel">
                                <div class="carousel-inner">
                                    ${Array.from(testimonials).map((testimonial, index) => {
                                        const clone = testimonial.cloneNode(true);
                                        return `
                                            <div class="carousel-item ${index === 0 ? 'active' : ''}">
                                                <div class="p-3">
                                                    ${clone.outerHTML}
                                                </div>
                                            </div>
                                        `;
                                    }).join('')}
                                </div>
                                <button class="carousel-control-prev" type="button" data-bs-target="#allTestimonialsCarousel" data-bs-slide="prev">
                                    <span class="carousel-control-prev-icon bg-primary rounded-circle p-3" aria-hidden="true"></span>
                                    <span class="visually-hidden">Previous</span>
                                </button>
                                <button class="carousel-control-next" type="button" data-bs-target="#allTestimonialsCarousel" data-bs-slide="next">
                                    <span class="carousel-control-next-icon bg-primary rounded-circle p-3" aria-hidden="true"></span>
                                    <span class="visually-hidden">Next</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            // Add modal to body
            document.body.appendChild(modal);

            // Initialize and show modal
            const modalInstance = new bootstrap.Modal(modal);
            modalInstance.show();

            // Clean up when modal is hidden
            modal.addEventListener('hidden.bs.modal', function() {
                document.body.removeChild(modal);
            });
        });
    }

    // Counter animation
    const counters = document.querySelectorAll('.counter');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.getAttribute('data-target'));
                    const duration = 2000; // 2 seconds
                    const step = Math.ceil(target / (duration / 16)); // 60fps

                    let current = 0;
                    const updateCounter = () => {
                        current += step;
                        if (current > target) current = target;
                        counter.textContent = current;

                        if (current < target) {
                            requestAnimationFrame(updateCounter);
                        }
                    };

                    updateCounter();
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            counterObserver.observe(counter);
        });
    }

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    if (forms.length > 0) {
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                form.classList.add('was-validated');
            }, false);
        });
    }
});
