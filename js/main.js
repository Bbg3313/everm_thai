(function () {
  "use strict";

  const header = document.querySelector(".site-header");
  const navToggle = document.querySelector(".nav-toggle");
  const siteNav = document.querySelector(".site-nav");
  const navLinks = document.querySelectorAll(".site-nav a[href^='#']");
  const form = document.getElementById("appointment-form");
  const formSuccess = document.getElementById("form-success");

  const floatTop = document.getElementById("float-top");
  const floatLine = document.getElementById("float-line");
  const floatActions = document.getElementById("float-actions");

  function onScroll() {
    if (window.scrollY > 40) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }

    if (floatTop) {
      const showTop = window.scrollY > 320;
      floatTop.hidden = !showTop;
      floatTop.classList.toggle("is-visible", showTop);
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (floatActions && floatLine) {
    var lineUrl = floatActions.getAttribute("data-line-url");
    if (lineUrl) {
      floatLine.setAttribute("href", lineUrl);
    }
  }

  if (floatTop) {
    floatTop.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* Mobile nav */
  if (navToggle && siteNav) {
    navToggle.addEventListener("click", function () {
      const expanded = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!expanded));
      siteNav.classList.toggle("open");
      document.body.style.overflow = expanded ? "" : "hidden";
    });

    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        navToggle.setAttribute("aria-expanded", "false");
        siteNav.classList.remove("open");
        document.body.style.overflow = "";
      });
    });
  }

  /* Review slider */
  const reviews = document.querySelectorAll(".review-card");
  const dots = document.querySelectorAll(".review-dots button");
  let reviewIndex = 0;
  let reviewTimer;

  function showReview(index) {
    if (!reviews.length) return;
    reviewIndex = (index + reviews.length) % reviews.length;
    reviews.forEach(function (card, i) {
      card.classList.toggle("active", i === reviewIndex);
    });
    dots.forEach(function (dot, i) {
      dot.classList.toggle("active", i === reviewIndex);
      dot.setAttribute("aria-selected", i === reviewIndex ? "true" : "false");
    });
  }

  function startReviewTimer() {
    clearInterval(reviewTimer);
    reviewTimer = setInterval(function () {
      showReview(reviewIndex + 1);
    }, 6000);
  }

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () {
      showReview(i);
      startReviewTimer();
    });
  });

  if (reviews.length) {
    showReview(0);
    startReviewTimer();
  }

  /* Hero image slider */
  const heroSlides = document.querySelectorAll(".hero-slide");
  const heroDots = document.querySelectorAll(".hero-slider-dots button");
  const heroCaptions = document.querySelectorAll(".hero-photo-caption");
  const heroProgressBar = document.getElementById("hero-progress-bar");
  const heroIntervalMs = 6000;
  let heroIndex = 0;
  let heroTimer;

  function restartHeroProgress() {
    if (!heroProgressBar) return;
    heroProgressBar.classList.remove("is-running");
    void heroProgressBar.offsetWidth;
    heroProgressBar.classList.add("is-running");
  }

  function showHeroSlide(index) {
    if (!heroSlides.length) return;
    heroIndex = (index + heroSlides.length) % heroSlides.length;
    heroSlides.forEach(function (slide, i) {
      slide.classList.toggle("active", i === heroIndex);
    });
    heroDots.forEach(function (dot, i) {
      dot.classList.toggle("active", i === heroIndex);
      dot.setAttribute("aria-selected", i === heroIndex ? "true" : "false");
    });
    heroCaptions.forEach(function (caption, i) {
      caption.classList.toggle("active", i === heroIndex);
    });
    restartHeroProgress();
  }

  function startHeroTimer() {
    clearInterval(heroTimer);
    restartHeroProgress();
    heroTimer = setInterval(function () {
      showHeroSlide(heroIndex + 1);
    }, heroIntervalMs);
  }

  heroDots.forEach(function (dot, i) {
    dot.addEventListener("click", function () {
      showHeroSlide(i);
      startHeroTimer();
    });
  });

  if (heroSlides.length) {
    showHeroSlide(0);
    startHeroTimer();
  }

  /* Technology image slider */
  const techSlides = document.querySelectorAll(".tech-slide");
  const techDots = document.querySelectorAll(".tech-slider-dots button");
  let techIndex = 0;
  let techTimer;

  function showTechSlide(index) {
    if (!techSlides.length) return;
    techIndex = (index + techSlides.length) % techSlides.length;
    techSlides.forEach(function (slide, i) {
      slide.classList.toggle("active", i === techIndex);
    });
    techDots.forEach(function (dot, i) {
      dot.classList.toggle("active", i === techIndex);
      dot.setAttribute("aria-selected", i === techIndex ? "true" : "false");
    });
  }

  function startTechTimer() {
    clearInterval(techTimer);
    techTimer = setInterval(function () {
      showTechSlide(techIndex + 1);
    }, 5000);
  }

  techDots.forEach(function (dot, i) {
    dot.addEventListener("click", function () {
      showTechSlide(i);
      startTechTimer();
    });
  });

  if (techSlides.length) {
    showTechSlide(0);
    startTechTimer();
  }

  /* FAQ accordion — one open at a time */
  const faqAccordion = document.getElementById("faq-accordion");
  if (faqAccordion) {
    const faqItems = faqAccordion.querySelectorAll(".accordion-item");
    faqItems.forEach(function (item) {
      item.addEventListener("toggle", function () {
        if (!item.open) return;
        faqItems.forEach(function (other) {
          if (other !== item && other.open) {
            other.open = false;
          }
        });
      });
    });
  }

  /* Scroll reveal */
  const revealEls = document.querySelectorAll(
    ".section-head, .treatment-card, .featured-video, .process-steps li, .doctor-profile, .case-card, .facility-card, .tech-list li, .about-panel, .hero-visual, .tech-slider, .faq-panel, .accordion-item, .faq-trust-list li"
  );

  revealEls.forEach(function (el) {
    el.classList.add("reveal");
  });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("visible");
    });
  }

  /* Facility gallery filter */
  const facilityTabs = document.querySelectorAll(".facility-tab");
  const facilityCards = document.querySelectorAll(".facility-card");

  facilityTabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      const filter = tab.getAttribute("data-filter");

      facilityTabs.forEach(function (t) {
        t.classList.remove("active");
        t.setAttribute("aria-selected", "false");
      });
      tab.classList.add("active");
      tab.setAttribute("aria-selected", "true");

      facilityCards.forEach(function (card) {
        const category = card.getAttribute("data-category");
        const show = filter === "all" || category === filter;
        card.classList.toggle("is-hidden", !show);
      });
    });
  });

  /* Appointment form */
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      form.reset();
      if (formSuccess) {
        formSuccess.hidden = false;
        setTimeout(function () {
          formSuccess.hidden = true;
        }, 6000);
      }
    });
  }

  /* Smooth offset for fixed header */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      const id = anchor.getAttribute("href");
      if (!id || id === "#") return;
      if (id === "#top") {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
        return;
      }
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - header.offsetHeight;
      window.scrollTo({ top: top, behavior: "smooth" });
    });
  });
})();
