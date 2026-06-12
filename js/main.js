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
  const navBackdrop = document.getElementById("nav-backdrop");

  function setMobileNavOpen(open) {
    if (!navToggle || !siteNav) return;
    navToggle.setAttribute("aria-expanded", String(open));
    siteNav.classList.toggle("open", open);
    document.body.classList.toggle("nav-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (navBackdrop) {
      navBackdrop.hidden = !open;
      navBackdrop.classList.toggle("is-visible", open);
      navBackdrop.setAttribute("aria-hidden", String(!open));
    }
  }

  if (navToggle && siteNav) {
    navToggle.addEventListener("click", function () {
      const expanded = navToggle.getAttribute("aria-expanded") === "true";
      setMobileNavOpen(!expanded);
    });

    if (navBackdrop) {
      navBackdrop.addEventListener("click", function () {
        setMobileNavOpen(false);
      });
    }

    navLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        setMobileNavOpen(false);
      });
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 768) {
        setMobileNavOpen(false);
      }
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
    }, 2000);
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
  const heroIntervalMs = 4000;
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
    }, 2000);
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
    ".section-head, .partner-care__card, .partner-care__steps li, .treatment-card, .featured-video, .process-roadmap__step, .doctor-profile, .results-showcase, .facility-carousel, .facility-tour, .tech-list li, .about-panel, .hero-visual, .hero-stat, .tech-slider, .faq-panel, .accordion-item, .faq-trust-list li"
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

  /* Facility carousel — 2 images per slide, auto-advance */
  const facilitySource = document.getElementById("facility-source");
  const facilityTrack = document.getElementById("facility-track");
  const facilityDots = document.getElementById("facility-dots");
  const facilityPrev = document.getElementById("facility-prev");
  const facilityNext = document.getElementById("facility-next");
  const facilityCarousel = document.getElementById("facility-carousel");
  const facilityTabs = document.querySelectorAll(".facility-tab");

  if (facilitySource && facilityTrack) {
    let facilityFilter = "all";
    let facilitySlideIndex = 0;
    let facilityTimer;
    const facilityIntervalMs = 5500;

    function getSourceCards() {
      return Array.from(facilitySource.querySelectorAll(".facility-card"));
    }

    function returnCardsToSource() {
      facilityTrack.querySelectorAll(".facility-card").forEach(function (card) {
        facilitySource.appendChild(card);
      });
    }

    function getFilteredCards() {
      return getSourceCards().filter(function (card) {
        const category = card.getAttribute("data-category");
        return facilityFilter === "all" || category === facilityFilter;
      });
    }

    function buildSlidePairs(cards) {
      const pairs = [];
      for (let i = 0; i < cards.length; i += 2) {
        pairs.push(cards.slice(i, i + 2));
      }
      return pairs;
    }

    function goFacilitySlide(index) {
      const slides = facilityTrack.querySelectorAll(".facility-slide");
      if (!slides.length) return;
      facilitySlideIndex = (index + slides.length) % slides.length;
      facilityTrack.style.transform = "translateX(-" + facilitySlideIndex * 100 + "%)";
      if (facilityDots) {
        facilityDots.querySelectorAll(".facility-carousel__dot").forEach(function (dot, i) {
          const active = i === facilitySlideIndex;
          dot.classList.toggle("active", active);
          dot.setAttribute("aria-selected", active ? "true" : "false");
        });
      }
    }

    function startFacilityTimer() {
      clearInterval(facilityTimer);
      facilityTimer = setInterval(function () {
        goFacilitySlide(facilitySlideIndex + 1);
      }, facilityIntervalMs);
    }

    function renderFacilityCarousel() {
      returnCardsToSource();
      const cards = getFilteredCards();
      const pairs = buildSlidePairs(cards);

      facilityTrack.innerHTML = "";
      if (facilityDots) facilityDots.innerHTML = "";

      if (!pairs.length) {
        facilityTrack.innerHTML =
          '<p class="facility-carousel__empty" data-i18n="fac_empty">ไม่มีภาพในหมวดนี้</p>';
        if (window.EvermI18n) {
          const el = facilityTrack.querySelector("[data-i18n]");
          if (el) {
            const key = el.getAttribute("data-i18n");
            const text = window.EvermI18n.t(key);
            if (text) el.textContent = text;
          }
        }
        return;
      }

      pairs.forEach(function (pair, slideIndex) {
        const slide = document.createElement("div");
        slide.className = "facility-slide" + (pair.length === 1 ? " facility-slide--single" : "");
        slide.setAttribute("role", "group");
        slide.setAttribute("aria-roledescription", "slide");

        pair.forEach(function (card) {
          slide.appendChild(card);
        });
        facilityTrack.appendChild(slide);

        if (facilityDots) {
          const dot = document.createElement("button");
          dot.type = "button";
          dot.className = "facility-carousel__dot" + (slideIndex === 0 ? " active" : "");
          dot.setAttribute("role", "tab");
          dot.setAttribute("aria-selected", slideIndex === 0 ? "true" : "false");
          dot.setAttribute("aria-label", String(slideIndex + 1));
          dot.addEventListener("click", function () {
            goFacilitySlide(slideIndex);
            startFacilityTimer();
          });
          facilityDots.appendChild(dot);
        }
      });

      facilitySlideIndex = Math.min(facilitySlideIndex, pairs.length - 1);
      goFacilitySlide(facilitySlideIndex);
    }

    facilityTabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        facilityFilter = tab.getAttribute("data-filter") || "all";
        facilitySlideIndex = 0;

        facilityTabs.forEach(function (t) {
          t.classList.remove("active");
          t.setAttribute("aria-selected", "false");
        });
        tab.classList.add("active");
        tab.setAttribute("aria-selected", "true");

        renderFacilityCarousel();
        startFacilityTimer();
      });
    });

    if (facilityPrev) {
      facilityPrev.addEventListener("click", function () {
        goFacilitySlide(facilitySlideIndex - 1);
        startFacilityTimer();
      });
    }

    if (facilityNext) {
      facilityNext.addEventListener("click", function () {
        goFacilitySlide(facilitySlideIndex + 1);
        startFacilityTimer();
      });
    }

    if (facilityCarousel) {
      facilityCarousel.addEventListener("mouseenter", function () {
        clearInterval(facilityTimer);
      });
      facilityCarousel.addEventListener("mouseleave", function () {
        startFacilityTimer();
      });
      facilityCarousel.addEventListener("focusin", function () {
        clearInterval(facilityTimer);
      });
      facilityCarousel.addEventListener("focusout", function () {
        startFacilityTimer();
      });
    }

    renderFacilityCarousel();
    startFacilityTimer();
  }

  /* Results carousel — Before & After clinical cases */
  const resultsTrack = document.getElementById("results-track");
  const resultsCarousel = document.getElementById("results-carousel");
  const resultsPrev = document.getElementById("results-prev");
  const resultsNext = document.getElementById("results-next");
  const resultsCurrent = document.getElementById("results-current");
  const resultsTotal = document.getElementById("results-total");
  const resultsProgress = document.getElementById("results-progress");
  const resultsCount = 32;

  if (resultsTrack) {
    let resultsIndex = 0;
    let resultsTimer;
    const resultsIntervalMs = 4500;

    for (let i = 1; i <= resultsCount; i += 1) {
      const slide = document.createElement("figure");
      slide.className = "results-slide";
      slide.setAttribute("role", "group");
      slide.setAttribute("aria-roledescription", "slide");
      slide.setAttribute("aria-label", String(i));

      const img = document.createElement("img");
      const num = String(i).padStart(2, "0");
      img.src = "images/cases/ba-" + num + ".jpg";
      img.alt = "Before and after case " + i;
      img.width = 780;
      img.height = 505;
      img.loading = i <= 2 ? "eager" : "lazy";
      img.decoding = "async";
      img.setAttribute("data-i18n-alt", "cases_img_alt");
      slide.appendChild(img);
      resultsTrack.appendChild(slide);
    }

    if (resultsTotal) {
      resultsTotal.textContent = String(resultsCount).padStart(2, "0");
    }

    function padSlide(n) {
      return String(n).padStart(2, "0");
    }

    function goResultsSlide(index) {
      resultsIndex = (index + resultsCount) % resultsCount;
      resultsTrack.style.transform = "translateX(-" + resultsIndex * 100 + "%)";
      if (resultsCurrent) resultsCurrent.textContent = padSlide(resultsIndex + 1);
      if (resultsProgress) {
        resultsProgress.style.width = ((resultsIndex + 1) / resultsCount) * 100 + "%";
      }
    }

    function startResultsTimer() {
      clearInterval(resultsTimer);
      resultsTimer = setInterval(function () {
        goResultsSlide(resultsIndex + 1);
      }, resultsIntervalMs);
    }

    if (resultsPrev) {
      resultsPrev.addEventListener("click", function () {
        goResultsSlide(resultsIndex - 1);
        startResultsTimer();
      });
    }

    if (resultsNext) {
      resultsNext.addEventListener("click", function () {
        goResultsSlide(resultsIndex + 1);
        startResultsTimer();
      });
    }

    if (resultsCarousel) {
      resultsCarousel.addEventListener("mouseenter", function () {
        clearInterval(resultsTimer);
      });
      resultsCarousel.addEventListener("mouseleave", function () {
        startResultsTimer();
      });
      resultsCarousel.addEventListener("focusin", function () {
        clearInterval(resultsTimer);
      });
      resultsCarousel.addEventListener("focusout", function () {
        startResultsTimer();
      });
    }

    goResultsSlide(0);
    startResultsTimer();
  }

  /* Video thumbnail at fixed timestamp; playback always starts at 0 */
  document.querySelectorAll("video[data-poster-time]").forEach(function (video) {
    var posterTime = parseFloat(video.getAttribute("data-poster-time"));
    if (!isFinite(posterTime) || posterTime < 0) return;

    var posterFrameSet = false;
    var playbackStarted = false;

    function markPosterReady() {
      video.classList.add("is-poster-ready");
    }

    function applyPosterFrame() {
      if (posterFrameSet || playbackStarted || video.readyState < 1) return;
      var duration = video.duration;
      if (!isFinite(duration) || duration <= 0) return;

      var seekTo = Math.min(posterTime, Math.max(0, duration - 0.25));
      posterFrameSet = true;
      video.pause();

      function onSeeked() {
        if (Math.abs(video.currentTime - seekTo) < 1) {
          markPosterReady();
          video.removeEventListener("seeked", onSeeked);
        }
      }

      video.addEventListener("seeked", onSeeked);
      video.currentTime = seekTo;
    }

    video.addEventListener("play", function () {
      if (playbackStarted) return;
      playbackStarted = true;
      posterFrameSet = true;

      if (video.currentTime < 0.05) return;

      video.pause();
      video.currentTime = 0;
      video.play();
    });

    video.addEventListener("loadedmetadata", applyPosterFrame);
    if (video.readyState >= 1) applyPosterFrame();

    setTimeout(function () {
      if (!video.classList.contains("is-poster-ready")) {
        markPosterReady();
      }
    }, 8000);
  });

  function playAutoplayVideo(video) {
    if (!video) return;
    video.muted = true;
    var rate = parseFloat(video.getAttribute("data-playback-rate"));
    video.playbackRate = isFinite(rate) && rate > 0 ? rate : 1;
    var attempt = video.play();
    if (attempt && typeof attempt.catch === "function") {
      attempt.catch(function () {});
    }
  }

  document.querySelectorAll("video.video-autoplay").forEach(function (video) {
    playAutoplayVideo(video);

    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              playAutoplayVideo(video);
            } else {
              video.pause();
            }
          });
        },
        { threshold: 0.35 }
      );
      observer.observe(video);
    }
  });

  /* Thai phone — 08X-XXX-XXXX (mobile) or 02-XXX-XXXX (Bangkok landline) */
  function normalizeThaiPhoneDigits(value) {
    var digits = String(value || "").replace(/\D/g, "");
    if (digits.indexOf("66") === 0 && digits.length >= 11) {
      digits = "0" + digits.slice(2);
    }
    return digits.slice(0, 10);
  }

  function formatThaiPhone(value) {
    var digits = normalizeThaiPhoneDigits(value);
    if (!digits.length) return "";
    if (digits.indexOf("02") === 0) {
      if (digits.length <= 2) return digits;
      if (digits.length <= 5) return digits.slice(0, 2) + "-" + digits.slice(2);
      return digits.slice(0, 2) + "-" + digits.slice(2, 5) + "-" + digits.slice(5, 9);
    }
    if (digits.length <= 3) return digits;
    if (digits.length <= 6) return digits.slice(0, 3) + "-" + digits.slice(3);
    return digits.slice(0, 3) + "-" + digits.slice(3, 6) + "-" + digits.slice(6);
  }

  function isValidThaiPhone(value) {
    var digits = normalizeThaiPhoneDigits(value);
    if (digits.length === 10 && /^0[6-9]/.test(digits)) return true;
    if (digits.length === 9 && /^02/.test(digits)) return true;
    return false;
  }

  function initThaiPhoneField(input) {
    if (!input) return;

    input.addEventListener("input", function () {
      var formatted = formatThaiPhone(input.value);
      if (formatted !== input.value) input.value = formatted;
      input.setCustomValidity("");
    });

    input.addEventListener("blur", function () {
      if (!input.value.trim()) {
        input.setCustomValidity("");
        return;
      }
      if (!isValidThaiPhone(input.value)) {
        var msg =
          window.EvermI18n && typeof window.EvermI18n.t === "function"
            ? window.EvermI18n.t("form_phone_invalid")
            : "Invalid Thai phone number";
        input.setCustomValidity(msg || "Invalid Thai phone number");
      } else {
        input.setCustomValidity("");
      }
    });
  }

  initThaiPhoneField(document.getElementById("phone"));

  /* Appointment form — POST to /api/inquiry (email via Resend) */
  const formError = document.getElementById("form-error");
  const formSubmitBtn = document.getElementById("form-submit-btn");

  function getSelectedServiceLabel() {
    const select = form && form.querySelector("#service, [name='service']");
    if (!select || select.selectedIndex < 0) return "";
    const option = select.options[select.selectedIndex];
    return (option && option.textContent.trim()) || option.value || "";
  }

  function setFormMessage(type) {
    if (formSuccess) formSuccess.hidden = type !== "success";
    if (formError) formError.hidden = type !== "error";
  }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      setFormMessage(null);

      const phoneInput = form.querySelector("#phone");
      if (phoneInput && phoneInput.value.trim() && !isValidThaiPhone(phoneInput.value)) {
        var phoneMsg =
          window.EvermI18n && typeof window.EvermI18n.t === "function"
            ? window.EvermI18n.t("form_phone_invalid")
            : "Invalid Thai phone number";
        phoneInput.setCustomValidity(phoneMsg || "Invalid Thai phone number");
      } else if (phoneInput) {
        phoneInput.setCustomValidity("");
      }

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      const payload = {
        name: (form.querySelector("#name") || {}).value || "",
        phone: formatThaiPhone((form.querySelector("#phone") || {}).value || ""),
        line_id: (form.querySelector("#line_id") || {}).value || "",
        service: getSelectedServiceLabel(),
        date: (form.querySelector("#date") || {}).value || "",
        time: (form.querySelector("#time") || {}).value || "",
        message: (form.querySelector("#message") || {}).value || "",
        website: (form.querySelector("[name='website']") || {}).value || "",
        lang: document.documentElement.lang || "",
      };

      var submitBtnLabel = "";
      if (formSubmitBtn) {
        submitBtnLabel = formSubmitBtn.textContent;
        formSubmitBtn.disabled = true;
        formSubmitBtn.setAttribute("aria-busy", "true");
        if (window.EvermI18n && typeof window.EvermI18n.t === "function") {
          var sendingLabel = window.EvermI18n.t("form_sending");
          if (sendingLabel) formSubmitBtn.textContent = sendingLabel;
        }
      }

      fetch("/api/inquiry", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok && data && data.ok, data: data, status: res.status };
          });
        })
        .then(function (result) {
          if (result.ok) {
            form.reset();
            document.querySelectorAll(".form-datetime-input").forEach(function (input) {
              syncNativeDatetimeEmptyState(input);
            });
            setFormMessage("success");
            setTimeout(function () {
              if (formSuccess) formSuccess.hidden = true;
            }, 8000);
            return;
          }
          setFormMessage("error");
        })
        .catch(function () {
          setFormMessage("error");
        })
        .finally(function () {
          if (formSubmitBtn) {
            formSubmitBtn.disabled = false;
            formSubmitBtn.removeAttribute("aria-busy");
            if (submitBtnLabel) formSubmitBtn.textContent = submitBtnLabel;
          }
        });
    });
  }

  /* Treatments carousel — horizontal swipe on mobile only */
  const treatmentsViewport = document.getElementById("treatments-viewport");
  const treatmentsTrack = document.getElementById("treatments-track");
  const treatmentsDots = document.getElementById("treatments-dots");
  const treatmentsNav = document.getElementById("treatments-nav");
  const treatmentsMql = window.matchMedia("(max-width: 768px)");

  if (treatmentsViewport && treatmentsTrack && treatmentsDots) {
    let treatmentsScrollTimer;

    function getTreatmentCards() {
      return Array.from(treatmentsTrack.querySelectorAll(".treatment-card"));
    }

    function getActiveTreatmentIndex() {
      const cards = getTreatmentCards();
      if (!cards.length) return 0;
      const center = treatmentsViewport.scrollLeft + treatmentsViewport.clientWidth / 2;
      let active = 0;
      cards.forEach(function (card, i) {
        const cardCenter = card.offsetLeft + card.offsetWidth / 2;
        if (cardCenter <= center + 1) active = i;
      });
      return active;
    }

    function updateTreatmentDots() {
      const active = getActiveTreatmentIndex();
      treatmentsDots.querySelectorAll(".treatments-carousel__dot").forEach(function (dot, i) {
        const isActive = i === active;
        dot.classList.toggle("active", isActive);
        dot.setAttribute("aria-selected", isActive ? "true" : "false");
      });
    }

    function scrollToTreatment(index) {
      const card = getTreatmentCards()[index];
      if (!card) return;
      const offset = card.offsetLeft - (treatmentsViewport.clientWidth - card.offsetWidth) / 2;
      treatmentsViewport.scrollTo({ left: Math.max(0, offset), behavior: "smooth" });
    }

    function buildTreatmentDots() {
      const cards = getTreatmentCards();
      treatmentsDots.innerHTML = "";
      cards.forEach(function (_, i) {
        const dot = document.createElement("button");
        dot.type = "button";
        dot.className = "treatments-carousel__dot" + (i === 0 ? " active" : "");
        dot.setAttribute("role", "tab");
        dot.setAttribute("aria-label", String(i + 1));
        dot.setAttribute("aria-selected", i === 0 ? "true" : "false");
        dot.addEventListener("click", function () {
          scrollToTreatment(i);
        });
        treatmentsDots.appendChild(dot);
      });
    }

    function syncTreatmentsCarousel() {
      if (treatmentsMql.matches) {
        if (treatmentsNav) treatmentsNav.hidden = false;
        if (!treatmentsDots.children.length) buildTreatmentDots();
        updateTreatmentDots();
      } else {
        if (treatmentsNav) treatmentsNav.hidden = true;
        treatmentsViewport.scrollLeft = 0;
        treatmentsDots.innerHTML = "";
      }
    }

    treatmentsViewport.addEventListener(
      "scroll",
      function () {
        if (!treatmentsMql.matches) return;
        clearTimeout(treatmentsScrollTimer);
        treatmentsScrollTimer = setTimeout(updateTreatmentDots, 60);
      },
      { passive: true }
    );

    if (typeof treatmentsMql.addEventListener === "function") {
      treatmentsMql.addEventListener("change", syncTreatmentsCarousel);
    } else {
      treatmentsMql.addListener(syncTreatmentsCarousel);
    }

    window.addEventListener("resize", syncTreatmentsCarousel);
    syncTreatmentsCarousel();
  }

  function syncNativeDatetimeEmptyState(input) {
    if (!input) return;
    input.classList.toggle("is-empty", !input.value);
  }

  function initNativeDatetimeFields() {
    document.querySelectorAll(".form-datetime-input").forEach(function (input) {
      syncNativeDatetimeEmptyState(input);
      input.addEventListener("input", function () {
        syncNativeDatetimeEmptyState(input);
      });
      input.addEventListener("change", function () {
        syncNativeDatetimeEmptyState(input);
      });
    });
  }

  initNativeDatetimeFields();

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
