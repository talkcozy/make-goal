const header = document.querySelector(".site-header");
const tabs = document.querySelector("[data-tabs]");

if (header && location.hash && location.hash !== "#top") {
  header.dataset.elevated = "true";
}

if (header && "IntersectionObserver" in window) {
  const headerSentinel = document.createElement("span");
  headerSentinel.setAttribute("aria-hidden", "true");
  headerSentinel.className = "header-sentinel";
  document.body.prepend(headerSentinel);

  const headerObserver = new IntersectionObserver(
    ([entry]) => {
      header.dataset.elevated = entry.isIntersecting ? "false" : "true";
    },
    { rootMargin: "24px 0px 0px 0px" },
  );

  headerObserver.observe(headerSentinel);
}

if (tabs) {
  const buttons = [...tabs.querySelectorAll(".tab-button")];
  const panels = [...tabs.querySelectorAll(".tab-panel")];

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const targetId = button.getAttribute("aria-controls");

      buttons.forEach((item) => {
        item.setAttribute("aria-selected", String(item === button));
      });

      panels.forEach((panel) => {
        const active = panel.id === targetId;
        panel.hidden = !active;
        panel.classList.toggle("active", active);
      });
    });
  });
}
