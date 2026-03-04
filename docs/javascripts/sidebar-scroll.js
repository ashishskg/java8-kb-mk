(function () {
  var KEY = 'mkdocs.sidebar.scrollTop.v1';
  var TS_KEY = 'mkdocs.sidebar.scrollTop.ts.v1';
  var restoreTimers = [];
  var restoring = false;
  var observer = null;
  var lastSavedY = null;
  var installedScrollEl = null;
  var installedScrollHandler = null;

  function getSidebarRoot() {
    return (
      document.querySelector('.wy-nav-side') ||
      document.querySelector('nav.wy-nav-side') ||
      document.querySelector('.wy-side-scroll')
    );
  }

  function isScrollable(el) {
    if (!el) return false;
    return el.scrollHeight > el.clientHeight + 2;
  }

  function findScrollableContainer(root) {
    if (!root) return null;
    // Prefer known containers first.
    var preferred = root.querySelector('.wy-side-scroll') || root;
    if (isScrollable(preferred)) return preferred;

    // Fall back: find first scrollable descendant.
    var candidates = root.querySelectorAll('*');
    for (var i = 0; i < candidates.length; i++) {
      var el = candidates[i];
      if (isScrollable(el)) return el;
    }
    return null;
  }

  function getScrollContainer() {
    var root = getSidebarRoot();
    return findScrollableContainer(root);
  }

  function clearRestoreTimers() {
    for (var i = 0; i < restoreTimers.length; i++) {
      clearTimeout(restoreTimers[i]);
    }
    restoreTimers = [];
  }

  function readSaved() {
    var raw = sessionStorage.getItem(KEY);
    if (!raw) return null;
    var y = parseInt(raw, 10);
    if (Number.isNaN(y)) return null;
    return y;
  }

  function readSavedTs() {
    var raw = sessionStorage.getItem(TS_KEY);
    if (!raw) return null;
    var ts = parseInt(raw, 10);
    if (Number.isNaN(ts)) return null;
    return ts;
  }

  function restore() {
    try {
      var y = readSaved();
      if (y === null) return;

      stabilizeRestore(y);
    } catch (_) {
      // no-op
    }
  }

  function persist() {
    try {
      var sc = getScrollContainer();
      if (!sc) return;
      var y = sc.scrollTop || 0;
      lastSavedY = y;
      sessionStorage.setItem(KEY, String(y));
      sessionStorage.setItem(TS_KEY, String(Date.now()));
    } catch (_) {
      // no-op
    }
  }

  function installScrollPersist() {
    var sc = getScrollContainer();
    if (!sc) return;

    if (installedScrollEl && installedScrollEl !== sc && installedScrollHandler) {
      installedScrollEl.removeEventListener('scroll', installedScrollHandler);
      installedScrollEl = null;
      installedScrollHandler = null;
    }

    if (installedScrollEl === sc) return;

    // Debounce writes to sessionStorage.
    var t = null;
    installedScrollHandler = function () {
      if (restoring) return;
      if (t) clearTimeout(t);
      t = setTimeout(persist, 75);
    };
    sc.addEventListener('scroll', installedScrollHandler, { passive: true });
    installedScrollEl = sc;
  }

  function disconnectObserver() {
    if (observer) {
      observer.disconnect();
      observer = null;
    }
  }

  function stabilizeRestore(targetY) {
    restoring = true;
    clearRestoreTimers();
    disconnectObserver();

    // Apply quickly; then keep re-applying during a stabilization window.
    var start = Date.now();
    var windowMs = 2600;

    function applyOnce() {
      var sc = getScrollContainer();
      if (!sc) return;
      var maxY = Math.max(0, (sc.scrollHeight || 0) - (sc.clientHeight || 0));
      var y = Math.max(0, Math.min(targetY, maxY));
      sc.scrollTop = y;
    }

    function tick() {
      applyOnce();
      if (Date.now() - start < windowMs) {
        requestAnimationFrame(tick);
      } else {
        restoring = false;
      }
    }

    // If theme mutates the nav (expands/collapses, marks current), apply again.
    var root = getSidebarRoot();
    if (root && typeof MutationObserver !== 'undefined') {
      observer = new MutationObserver(function () {
        installScrollPersist();
        applyOnce();
      });
      observer.observe(root, { subtree: true, childList: true, attributes: true });
    }

    // Also schedule delayed retries for cases where the theme expands/collapses
    // the current section after initial paint (common with deep nav sections).
    var delays = [0, 60, 180, 350, 700, 1200, 1800, 2400];
    for (var i = 0; i < delays.length; i++) {
      restoreTimers.push(
        setTimeout(
          (function (y) {
            return function () {
              applyOnce();
            };
          })(targetY),
          delays[i]
        )
      );
    }

    requestAnimationFrame(tick);
  }

  // Persist during navigation clicks within the sidebar.
  document.addEventListener(
    'click',
    function (e) {
      var root = getSidebarRoot();
      if (!root) return;
      if (!root.contains(e.target)) return;

      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (!a) return;
      if (!a.getAttribute('href')) return;

      persist();

      // The theme may auto-scroll the active item after navigation.
      // Re-apply restore shortly after click to override that behavior.
      setTimeout(restore, 0);
      setTimeout(restore, 50);
      setTimeout(restore, 150);
    },
    true
  );

  // Persist on unload as a fallback (tab close, reload, etc.).
  window.addEventListener('beforeunload', persist);
  window.addEventListener('pagehide', persist);
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') persist();
  });

  // Restore on history navigation and hash navigation.
  window.addEventListener('popstate', function () {
    installScrollPersist();
    restore();
  });
  window.addEventListener('hashchange', function () {
    installScrollPersist();
    restore();
  });

  // Restore after DOM is ready.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      installScrollPersist();
      restore();
    });
  } else {
    installScrollPersist();
    restore();
  }

  // Some browsers/theme behaviors finalize layout after DOMContentLoaded.
  // Run a late restore on window load to catch nav expansion and font/layout shifts.
  window.addEventListener('load', function () {
    installScrollPersist();
    restore();
  });
})();
