/**
 * Dev Patel - Portfolio & Resume JavaScript
 * Handles dark/light theme, custom circular cursor pointer, interactive copy, active nav links, and UI states.
 */

document.addEventListener('DOMContentLoaded', () => {
    // --------------------------------------------------------
    // 1. Fancy Circular Pointer (Mouse Cursor)
    // --------------------------------------------------------
    const cursorDot = document.getElementById('cursor-dot');
    const cursorFollower = document.getElementById('cursor-follower');

    if (cursorDot && cursorFollower && window.matchMedia('(pointer: fine)').matches) {
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let followerX = mouseX;
        let followerY = mouseY;
        let isCursorActive = false;

        // Track real mouse position
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;

            if (!isCursorActive) {
                cursorDot.classList.remove('is-hidden');
                cursorFollower.classList.remove('is-hidden');
                cursorDot.style.opacity = '1';
                cursorFollower.style.opacity = '1';
                followerX = mouseX;
                followerY = mouseY;
                isCursorActive = true;
            }

            cursorDot.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
        });

        // Smooth physics animation loop for the outer circle
        function animateCursor() {
            // Linear interpolation (LERP) for fluid follow
            followerX += (mouseX - followerX) * 0.16;
            followerY += (mouseY - followerY) * 0.16;

            cursorFollower.style.transform = `translate(${followerX}px, ${followerY}px) translate(-50%, -50%)`;
            requestAnimationFrame(animateCursor);
        }
        requestAnimationFrame(animateCursor);

        // Hover effect on interactive elements
        const interactiveElements = document.querySelectorAll(
            'a, button, .btn, .project-card, .skill-tag, .theme-toggle, .mobile-toggle, .stat-box, .cert-badge, .contact-item'
        );

        interactiveElements.forEach((el) => {
            el.addEventListener('mouseenter', () => {
                cursorFollower.classList.add('is-hovering');
            });
            el.addEventListener('mouseleave', () => {
                cursorFollower.classList.remove('is-hovering');
            });
        });

        // Typing effect inside input/textarea
        const textInputs = document.querySelectorAll('input, textarea');
        textInputs.forEach((input) => {
            input.addEventListener('mouseenter', () => {
                cursorFollower.classList.add('is-typing');
                cursorDot.style.opacity = '0';
            });
            input.addEventListener('mouseleave', () => {
                cursorFollower.classList.remove('is-typing');
                cursorDot.style.opacity = '1';
            });
        });

        // Mouse down/up click feedback
        window.addEventListener('mousedown', () => {
            cursorFollower.classList.add('is-clicking');
        });
        window.addEventListener('mouseup', () => {
            cursorFollower.classList.remove('is-clicking');
        });

        // Hide when mouse leaves window
        document.addEventListener('mouseleave', () => {
            cursorDot.classList.add('is-hidden');
            cursorFollower.classList.add('is-hidden');
        });
        document.addEventListener('mouseenter', () => {
            cursorDot.classList.remove('is-hidden');
            cursorFollower.classList.remove('is-hidden');
        });
    }

    // --------------------------------------------------------
    // 2. Dark / Light Theme Manager
    // --------------------------------------------------------
    const themeToggleBtn = document.getElementById('theme-toggle');
    const rootHtml = document.documentElement;

    const savedTheme = localStorage.getItem('dp_theme');
    if (savedTheme) {
        rootHtml.setAttribute('data-theme', savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        rootHtml.setAttribute('data-theme', 'light');
    } else {
        rootHtml.setAttribute('data-theme', 'dark');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = rootHtml.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            rootHtml.setAttribute('data-theme', newTheme);
            localStorage.setItem('dp_theme', newTheme);
        });
    }

    // --------------------------------------------------------
    // 3. Mobile Menu Toggle
    // --------------------------------------------------------
    const mobileToggle = document.getElementById('mobile-toggle');
    const navLinks = document.getElementById('nav-links');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            const isFlex = navLinks.style.display === 'flex';
            navLinks.style.display = isFlex ? 'none' : 'flex';
            if (!isFlex) {
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '4.5rem';
                navLinks.style.left = '0';
                navLinks.style.right = '0';
                navLinks.style.backgroundColor = 'var(--bg-primary)';
                navLinks.style.padding = '1.5rem';
                navLinks.style.borderBottom = '1px solid var(--border-color)';
            }
        });

        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    navLinks.style.display = 'none';
                }
            });
        });
    }

    // --------------------------------------------------------
    // 4. Active Nav Link on Scroll
    // --------------------------------------------------------
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        let currentSectionId = '';
        const scrollPosition = window.pageYOffset + 120;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navItems.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });

    // --------------------------------------------------------
    // 5. Interactive Copy Email Button
    // --------------------------------------------------------
    const copyEmailBtn = document.getElementById('btn-copy-email');
    const copyText = document.getElementById('copy-text');

    if (copyEmailBtn) {
        copyEmailBtn.addEventListener('click', () => {
            const email = "dnhp281999@gmail.com";
            navigator.clipboard.writeText(email).then(() => {
                if (copyText) {
                    const original = copyText.textContent;
                    copyText.textContent = 'Copied! ✓';
                    copyEmailBtn.style.borderColor = 'var(--success)';
                    copyEmailBtn.style.color = 'var(--success)';
                    setTimeout(() => {
                        copyText.textContent = original;
                        copyEmailBtn.style.borderColor = '';
                        copyEmailBtn.style.color = '';
                    }, 2500);
                }
            }).catch(() => {
                window.location.href = `mailto:${email}`;
            });
        });
    }

    // --------------------------------------------------------
    // 6. Contact Form Real-Time Email Delivery Forwarding
    // --------------------------------------------------------
    const contactForm = document.querySelector('.resume-contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            const nameInput = contactForm.querySelector('[name="name"]');
            const emailInput = contactForm.querySelector('[name="email"]');
            const subjectInput = contactForm.querySelector('[name="subject"]');
            const messageInput = contactForm.querySelector('[name="message"]');

            if (nameInput && emailInput && messageInput) {
                // Send an async forward copy to FormSubmit so Dev receives email instantly in Gmail
                try {
                    fetch('https://formsubmit.co/ajax/dnhp281999@gmail.com', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            name: nameInput.value,
                            email: emailInput.value,
                            _subject: `Portfolio Message from ${nameInput.value}: ${subjectInput ? subjectInput.value : 'Inquiry'}`,
                            message: messageInput.value
                        })
                    }).catch(() => {
                        // Silent failover to standard Django form submission
                    });
                } catch (err) {
                    // Fallback to standard Django POST
                }
            }
        });
    }

    // --------------------------------------------------------
    // 7. Auto-dismiss Toast Notifications
    // --------------------------------------------------------
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            toast.style.transition = 'all 0.4s ease';
            setTimeout(() => toast.remove(), 400);
        }, 6000);
    });
});
