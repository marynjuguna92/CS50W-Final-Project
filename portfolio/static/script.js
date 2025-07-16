document.addEventListener("DOMContentLoaded", function () {
  // ---- Scroll animation ----
  if (typeof ScrollReveal !== "undefined") {
    ScrollReveal().reveal(".hero-section", {
      delay: 200,
      duration: 1000,
      origin: "bottom",
      distance: "50px",
      easing: "ease-in-out"
    });

    ScrollReveal().reveal(".section-title", {
      delay: 100,
      duration: 800,
      origin: "bottom",
      distance: "40px",
      easing: "ease-in-out"
    });

    ScrollReveal().reveal(".about-card", {
      interval: 150,
      duration: 800,
      origin: "bottom",
      distance: "30px"
    });

    ScrollReveal().reveal(".education-list li", {
      interval: 150,
      origin: "bottom",
      distance: "30px",
      duration: 700
    });

    ScrollReveal().reveal(".logo-grid img", {
      interval: 100,
      origin: "bottom",
      distance: "20px",
      duration: 800
    });

    ScrollReveal().reveal(".footer-container", {
      duration: 1000,
      origin: "bottom",
      distance: "50px"
    });
  }

  // Back to top arrow
  const backToTop = document.getElementById("backToTop");

  window.addEventListener("scroll", function () {
    const scrollY = window.scrollY;
    const aboutTop = document.querySelector(".about-section")?.offsetTop || 0;
    const educationTop = document.querySelector(".education-section")?.offsetTop || 0;

    if (scrollY > aboutTop - 100 || scrollY > educationTop - 100 || scrollY > 500) {
      backToTop.style.display = "block";
    } else {
      backToTop.style.display = "none";
    }
  });

  backToTop.addEventListener("click", function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  //  Mobile menu toggle 
  const menuToggle = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  menuToggle.addEventListener("click", () => {
    mobileMenu.classList.toggle("active");
    menuToggle.classList.toggle("active"); 
  });

  // Auto-close mobile menu
  document.querySelectorAll(".mobile-links a").forEach(link => {
    link.addEventListener("click", () => {
      mobileMenu.classList.remove("active");
      menuToggle.classList.remove("active");
    });
  });
});
