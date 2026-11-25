/* Accessibility options: high contrast, larger text, wider spacing, underlined links. Stored in localStorage (optional). */
(function () {
  var KEY = "emore-a11y";
  var root = document.documentElement;
  var map = { contrast: ["data-contrast", "high"], text: ["data-text", "large"], spacing: ["data-spacing", "wide"], links: ["data-links", "underline"] };
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; } }
  function save(p) { try { localStorage.setItem(KEY, JSON.stringify(p)); } catch (e) {} }
  function apply(p) { Object.keys(map).forEach(function (k) { if (p[k]) root.setAttribute(map[k][0], map[k][1]); else root.removeAttribute(map[k][0]); }); }
  var prefs = load();
  if (!("contrast" in prefs) && window.matchMedia && matchMedia("(prefers-contrast: more)").matches) prefs.contrast = true;
  apply(prefs);
  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("a11y-btn"), panel = document.getElementById("a11y-panel");
    if (!btn || !panel) return;
    var boxes = panel.querySelectorAll("input[type=checkbox][data-opt]");
    function sync() { boxes.forEach(function (b) { b.checked = !!prefs[b.dataset.opt]; }); }
    function open(v) { panel.hidden = !v; btn.setAttribute("aria-expanded", v ? "true" : "false"); if (v) boxes[0].focus(); }
    sync();
    btn.addEventListener("click", function () { open(panel.hidden); });
    boxes.forEach(function (b) { b.addEventListener("change", function () { prefs[b.dataset.opt] = b.checked; save(prefs); apply(prefs); }); });
    document.getElementById("a11y-reset").addEventListener("click", function () { prefs = { contrast: false }; save(prefs); apply(prefs); sync(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) { open(false); btn.focus(); } });
    document.addEventListener("click", function (e) { if (!panel.hidden && !panel.contains(e.target) && !btn.contains(e.target)) open(false); });
  });
})();
