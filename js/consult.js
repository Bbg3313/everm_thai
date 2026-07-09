(function () {
  "use strict";

  var STRINGS = {
    th: {
      meta_title: "แบบสอบถามก่อนปรึกษา | EVERM Surgery Clinic",
      meta_description:
        "กรอกแบบสอบถามสั้น ๆ เพื่อให้ทีม EVERM และ BlueBridge Global วางแผนการปรึกษาศัลยกรรมโครงหน้าและขากรรไกรที่เกาหลีได้อย่างเหมาะสม",
      badge: "Pre-Screening",
      hero_title: "บอกเราเกี่ยวกับคุณ\nก่อนนัดปรึกษา",
      hero_lead:
        "ตอบคำถาม 4 ข้อสั้น ๆ เพื่อให้ทีมแพทย์และผู้ดูแลชาวไทยของ BlueBridge Global เตรียมแผนการปรึกษาที่เหมาะกับคุณที่สุด",
      trust_1: "ศัลยแพทย์ช่องปากและแม็กซิลโลเฟเชียลผู้เชี่ยวชาญ ณ โซล",
      trust_2: "วางแผนผ่าตัด 3D ก่อนตัดสินใจ",
      trust_3: "BlueBridge Global ดูแลครบตั้งแต่ไทยถึงเกาหลี",
      hero_note: "กลับไปยังเว็บไซต์หลัก →",
      form_title: "แบบสอบถามก่อนปรึกษา",
      form_sub: "กรุณากรอกทุกช่องที่มีเครื่องหมาย *",
      contact_title: "ข้อมูลติดต่อ",
      label_name: "ชื่อ-นามสกุล",
      ph_name: "ชื่อของคุณ",
      label_phone: "เบอร์โทร",
      ph_phone: "08X-XXX-XXXX",
      label_line: "LINE ID",
      ph_line: "@lineid",
      q1_label: "สิ่งที่คุณกังวลมากที่สุดคืออะไร?",
      q1_hint: "เช่น ปากยื่น คางสั้น หน้าไม่สมมาตร หรือการหายใจ",
      q1_ph: "เล่าสิ่งที่อยากแก้ไขหรือกังวลมากที่สุด",
      q2_label: "ประวัติการผ่าตัด / การปรึกษา",
      q2_hint: "เคยปรึกษาหรือผ่าตัดที่ไหนมาบ้าง ผลเป็นอย่างไร",
      q2_ph: "ระบุประวัติการปรึกษา ผ่าตัด หรือการรักษาที่เกี่ยวข้อง",
      q3_label: "วันที่วางแผนจะผ่าตัด",
      q3_hint: "หากยังไม่แน่ใจ ระบุช่วงเวลาที่คาดไว้",
      q4_label: "มีปัญหาฟันไม่เรียง / เคยจัดฟันหรือไม่?",
      malo_yes: "มี / เคยจัดฟัน",
      malo_no: "ไม่มี",
      malo_unsure: "ไม่แน่ใจ",
      malo_details_ph: "รายละเอียดเพิ่มเติม (ถ้ามี)",
      form_note: "ข้อมูลของคุณเป็นความลับ — เจ้าหน้าที่จะติดต่อกลับภายใน 24 ชม.",
      submit: "ส่งแบบสอบถาม",
      sending: "กำลังส่ง…",
      error: "ส่งไม่สำเร็จ กรุณาลองอีกครั้งหรือโทร 02-540-8275",
      success_title: "ขอบคุณค่ะ/ครับ!",
      success_body: "เราได้รับแบบสอบถามแล้ว ทีมงานจะติดต่อกลับโดยเร็วที่สุด",
      success_btn: "ดูเว็บไซต์ EVERM",
      footer: "© EVERM Surgery Clinic × BlueBridge Global",
      phone_invalid: "กรุณากรอกเบอร์โทรไทยให้ถูกต้อง (08X-XXX-XXXX)",
      malo_required: "กรุณาเลือกคำตอบข้อที่ 4",
    },
    en: {
      meta_title: "Pre-Screening Form | EVERM Surgery Clinic",
      meta_description:
        "Answer a short pre-screening form so EVERM and BlueBridge Global can prepare your maxillofacial surgery consultation in Korea.",
      badge: "Pre-Screening",
      hero_title: "Tell us about you\nbefore your consult",
      hero_lead:
        "Answer 4 quick questions so our surgeons and Thai care team at BlueBridge Global can prepare the right consultation plan for you.",
      trust_1: "Board-certified oral & maxillofacial surgeons in Seoul",
      trust_2: "3D surgical planning before you decide",
      trust_3: "BlueBridge Global — full care from Thailand to Korea",
      hero_note: "Back to main website →",
      form_title: "Pre-Screening Questionnaire",
      form_sub: "Please complete all fields marked *",
      contact_title: "Contact details",
      label_name: "Full name",
      ph_name: "Your name",
      label_phone: "Phone",
      ph_phone: "08X-XXX-XXXX",
      label_line: "LINE ID",
      ph_line: "@lineid",
      q1_label: "What is your biggest concern?",
      q1_hint: "e.g. protruding jaw, short chin, asymmetry, or breathing",
      q1_ph: "Describe what you most want to improve or worry about",
      q2_label: "Surgery / consultation history",
      q2_hint: "Where you consulted or had surgery before, and outcomes",
      q2_ph: "List any related consultations, surgeries, or treatments",
      q3_label: "Planned surgery date",
      q3_hint: "If unsure, enter your expected timeframe",
      q4_label: "Malocclusion / orthodontic history?",
      malo_yes: "Yes / orthodontic history",
      malo_no: "No",
      malo_unsure: "Not sure",
      malo_details_ph: "Additional details (optional)",
      form_note: "Your information is confidential — we will contact you within 24 hours.",
      submit: "Submit questionnaire",
      sending: "Sending…",
      error: "Submission failed. Please try again or call 02-540-8275",
      success_title: "Thank you!",
      success_body: "We received your questionnaire. Our team will contact you shortly.",
      success_btn: "Visit EVERM website",
      footer: "© EVERM Surgery Clinic × BlueBridge Global",
      phone_invalid: "Please enter a valid Thai phone number (08X-XXX-XXXX)",
      malo_required: "Please answer question 4",
    },
  };

  var currentLang = "th";
  var utmParams = {};

  function t(key) {
    var pack = STRINGS[currentLang] || STRINGS.th;
    return pack[key] || STRINGS.th[key] || key;
  }

  function getStoredLang() {
    var saved = localStorage.getItem("everm_lang");
    if (saved === "ko") saved = "th";
    return saved === "en" ? "en" : "th";
  }

  function setLang(lang) {
    currentLang = lang === "en" ? "en" : "th";
    localStorage.setItem("everm_lang", currentLang);
    document.documentElement.lang = currentLang === "th" ? "th" : "en";
    document.body.classList.remove("lang-th", "lang-en");
    document.body.classList.add(currentLang === "en" ? "lang-en" : "lang-th");
    applyStrings();
    syncLangButtons();
  }

  function applyStrings() {
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      var value = t(key);
      if (value.indexOf("\n") !== -1) {
        el.innerHTML = value.replace(/\n/g, "<br>");
      } else {
        el.textContent = value;
      }
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach(function (el) {
      el.placeholder = t(el.getAttribute("data-i18n-placeholder"));
    });

    document.title = t("meta_title");
    var desc = document.querySelector('meta[name="description"]');
    if (desc) desc.setAttribute("content", t("meta_description"));
  }

  function syncLangButtons() {
    document.querySelectorAll(".consult-lang__btn").forEach(function (btn) {
      var isActive = btn.getAttribute("data-lang") === currentLang;
      btn.classList.toggle("is-active", isActive);
      btn.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  }

  function parseUtm() {
    var params = new URLSearchParams(window.location.search);
    ["utm_source", "utm_campaign", "utm_medium", "fbclid"].forEach(function (key) {
      var val = params.get(key);
      if (val) utmParams[key] = val;
    });
  }

  function formatThaiPhone(value) {
    var digits = String(value || "").replace(/\D/g, "");
    if (digits.length === 10 && digits.charAt(0) === "0") {
      return digits.slice(0, 3) + "-" + digits.slice(3, 6) + "-" + digits.slice(6);
    }
    return value.trim();
  }

  function isValidThaiPhone(value) {
    return /^0\d{2}-\d{3}-\d{4}$/.test(formatThaiPhone(value));
  }

  function trackConversion() {
    if (typeof window.fbq === "function") {
      window.fbq("track", "Lead");
    }
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "meta_consult_submit",
      form_name: "everm_pre_screening",
      lang: currentLang,
    });
  }

  function showFormView(showSuccess) {
    var formWrap = document.getElementById("consult-form-wrap");
    var successWrap = document.getElementById("consult-success");
    if (formWrap) formWrap.hidden = showSuccess;
    if (successWrap) successWrap.hidden = !showSuccess;
    if (showSuccess) {
      successWrap.setAttribute("tabindex", "-1");
      successWrap.focus();
    }
  }

  function initForm() {
    var form = document.getElementById("consult-form");
    var submitBtn = document.getElementById("consult-submit");
    var errorEl = document.getElementById("consult-error");
    if (!form) return;

    var phoneInput = form.querySelector("#consult-phone");
    if (phoneInput) {
      phoneInput.addEventListener("input", function () {
        phoneInput.setCustomValidity("");
      });
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (errorEl) errorEl.hidden = true;

      var maloChecked = form.querySelector('input[name="malocclusion"]:checked');
      if (!maloChecked) {
        var maloGroup = form.querySelector(".consult-radio-group");
        if (maloGroup) {
          maloGroup.setAttribute("aria-invalid", "true");
        }
        alert(t("malo_required"));
        return;
      }

      if (phoneInput && phoneInput.value.trim() && !isValidThaiPhone(phoneInput.value)) {
        phoneInput.setCustomValidity(t("phone_invalid"));
      } else if (phoneInput) {
        phoneInput.setCustomValidity("");
      }

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var payload = {
        name: form.querySelector("#consult-name").value.trim(),
        phone: formatThaiPhone(form.querySelector("#consult-phone").value),
        line_id: form.querySelector("#consult-line").value.trim(),
        concern: form.querySelector("#consult-concern").value.trim(),
        surgery_history: form.querySelector("#consult-history").value.trim(),
        surgery_date: form.querySelector("#consult-date").value.trim(),
        malocclusion: maloChecked.value,
        malocclusion_details: (form.querySelector("#consult-malo-details") || {}).value || "",
        website: (form.querySelector("[name='website']") || {}).value || "",
        lang: currentLang,
        utm_source: utmParams.utm_source || "",
        utm_campaign: utmParams.utm_campaign || "",
        utm_medium: utmParams.utm_medium || "",
        fbclid: utmParams.fbclid || "",
      };

      var btnLabel = submitBtn ? submitBtn.textContent : "";
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.setAttribute("aria-busy", "true");
        submitBtn.textContent = t("sending");
      }

      fetch("/api/meta-consult", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok && data && data.ok };
          });
        })
        .then(function (result) {
          if (result.ok) {
            trackConversion();
            showFormView(true);
            return;
          }
          if (errorEl) errorEl.hidden = false;
        })
        .catch(function () {
          if (errorEl) errorEl.hidden = false;
        })
        .finally(function () {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.removeAttribute("aria-busy");
            submitBtn.textContent = btnLabel || t("submit");
          }
        });
    });
  }

  function initLang() {
    document.querySelectorAll(".consult-lang__btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        setLang(btn.getAttribute("data-lang"));
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    parseUtm();
    currentLang = getStoredLang();
    document.body.classList.add(currentLang === "en" ? "lang-en" : "lang-th");
    document.documentElement.lang = currentLang === "th" ? "th" : "en";
    applyStrings();
    syncLangButtons();
    initLang();
    initForm();
  });
})();
