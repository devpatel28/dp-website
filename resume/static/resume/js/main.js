/**
 * Dev Nareshkumar Patel - Portfolio & Resume JavaScript
 * Handles dark/light theme, interactive copy, active nav links, and UI states.
 */

document.addEventListener('DOMContentLoaded', () => {
    // --------------------------------------------------------
    // 1. Dark / Light Theme Manager
    // --------------------------------------------------------
    const themeToggleBtn = document.getElementById('theme-toggle');
    const rootHtml = document.documentElement;

    // Check saved theme or system preference
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
    // 2. Mobile Menu Toggle
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

        // Close mobile menu when a nav link is clicked
        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    navLinks.style.display = 'none';
                }
            });
        });
    }

    // --------------------------------------------------------
    // 3. Active Nav Link on Scroll (Intersection Observer)
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
    // 4. Interactive Copy Email to Clipboard
    // --------------------------------------------------------
    const copyEmailLink = document.getElementById('copy-email-link');
    const copyHint = document.getElementById('copy-hint');

    if (copyEmailLink && copyHint) {
        copyEmailLink.addEventListener('click', (e) => {
            e.preventDefault();
            const email = copyEmailLink.textContent.trim();
            navigator.clipboard.writeText(email).then(() => {
                const originalText = copyHint.textContent;
                copyHint.textContent = 'Copied to clipboard! ✓';
                copyHint.style.color = 'var(--success)';
                setTimeout(() => {
                    copyHint.textContent = originalText;
                    copyHint.style.color = '';
                }, 2500);
            }).catch(() => {
                window.location.href = `mailto:${email}`;
            });
        });
    }

    // --------------------------------------------------------
    // 5. Auto-dismiss Toast Notifications
    // --------------------------------------------------------
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            toast.style.transition = 'all 0.4s ease';
            setTimeout(() => toast.remove(), 400);
        }, 5000);
    });
});

