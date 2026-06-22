// Mobile Menu
const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

if (menuBtn && navLinks) {
    menuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });
}

// Counter Animation
const counters = document.querySelectorAll(".counter");

const runCounter = () => {
    counters.forEach(counter => {
        const target = +counter.dataset.target;
        let count = 0;

        const update = () => {
            count += Math.ceil(target / 50);

            if (count < target) {
                counter.innerText = count;
                setTimeout(update, 30);
            } else {
                counter.innerText = target;
            }
        };

        update();
    });
};

window.addEventListener("load", runCounter);

// Navbar Scroll Effect
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    if (window.scrollY > 50) {
        navbar.style.background = "#0f172a";
    } else {
        navbar.style.background = "rgba(15,23,42,0.8)";
    }
});

// Typed Effect
window.addEventListener("load", () => {
    if (
        typeof Typed !== "undefined" &&
        document.querySelector(".typing")
    ) {
        new Typed(".typing", {
            strings: [
                "Python Backend Developer",
                "Flask Developer",
                "REST API Developer",
                "Web Developer"
            ],
            typeSpeed: 80,
            backSpeed: 40,
            loop: true
        });
    }
});

// Particles Safe Load
window.addEventListener("load", () => {
    if (typeof particlesJS !== "undefined") {
        particlesJS("particles-js", {
            particles: {
                number: {
                    value: 40
                },
                color: {
                    value: "#6366f1"
                },
                size: {
                    value: 3
                },
                move: {
                    speed: 2
                }
            }
        });
    }
});