(function () {
  "use strict";

  var STORAGE_KEY = "everm_lang";
  var DEFAULT_LANG = "th";
  var SUPPORTED = ["ko", "en", "th"];

  var I18N_ATTRS = [
    "data-i18n",
    "data-i18n-html",
    "data-i18n-placeholder",
    "data-i18n-aria",
    "data-i18n-alt",
    "data-i18n-title",
  ];

  function detectLang() {
    var saved = localStorage.getItem(STORAGE_KEY);
    if (saved && SUPPORTED.indexOf(saved) !== -1) return saved;
    var nav = (navigator.language || navigator.userLanguage || "").toLowerCase();
    if (nav.indexOf("ko") === 0) return "ko";
    if (nav.indexOf("th") === 0) return "th";
    if (nav.indexOf("en") === 0) return "en";
    return DEFAULT_LANG;
  }

  function t(lang, key) {
    var pack = window.EVERM_I18N && window.EVERM_I18N[lang];
    if (!pack) return null;
    return pack[key];
  }

  function getKey(el) {
    for (var i = 0; i < I18N_ATTRS.length; i++) {
      var key = el.getAttribute(I18N_ATTRS[i]);
      if (key) return key;
    }
    return null;
  }

  function applyToElement(el, lang, key) {
    var value = t(lang, key);
    if (value == null) return;

    if (el.hasAttribute("data-i18n-html")) {
      el.innerHTML = value;
      return;
    }

    if (el.hasAttribute("data-i18n-placeholder")) {
      el.placeholder = value;
      return;
    }

    if (el.hasAttribute("data-i18n-aria")) {
      el.setAttribute("aria-label", value);
      return;
    }

    if (el.hasAttribute("data-i18n-alt")) {
      el.setAttribute("alt", value);
      return;
    }

    if (el.hasAttribute("data-i18n-title")) {
      el.setAttribute("title", value);
      return;
    }

    el.textContent = value;
  }

  function queryI18nElements() {
    var seen = new Set();
    var list = [];
    I18N_ATTRS.forEach(function (attr) {
      document.querySelectorAll("[" + attr + "]").forEach(function (el) {
        if (!seen.has(el)) {
          seen.add(el);
          list.push(el);
        }
      });
    });
    return list;
  }

  function setLanguage(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = DEFAULT_LANG;

    document.documentElement.lang = lang === "ko" ? "ko" : lang === "th" ? "th" : "en";
    document.body.classList.remove("lang-ko", "lang-en", "lang-th");
    document.body.classList.add("lang-" + lang);

    var title = t(lang, "meta_title");
    var desc = t(lang, "meta_description");
    if (title) document.title = title;
    if (desc) {
      var meta = document.querySelector('meta[name="description"]');
      if (meta) meta.setAttribute("content", desc);
    }

    queryI18nElements().forEach(function (el) {
      var key = getKey(el);
      if (key) applyToElement(el, lang, key);
    });

    document.querySelectorAll(".lang-btn").forEach(function (btn) {
      var active = btn.getAttribute("data-lang") === lang;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });

    localStorage.setItem(STORAGE_KEY, lang);
    document.dispatchEvent(new CustomEvent("everm:languagechange", { detail: { lang: lang } }));
  }

  window.EvermI18n = {
    setLanguage: setLanguage,
    getLanguage: function () {
      return localStorage.getItem(STORAGE_KEY) || detectLang();
    },
    t: function (key) {
      return t(window.EvermI18n.getLanguage(), key);
    },
  };

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".lang-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        setLanguage(btn.getAttribute("data-lang"));
      });
    });
    setLanguage(detectLang());
  });
})();
