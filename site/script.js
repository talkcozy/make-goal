const header = document.querySelector(".site-header");
const tabs = document.querySelector("[data-tabs]");

const updateHeader = () => {
  if (!header) return;
  header.dataset.elevated = window.scrollY > 24 ? "true" : "false";
};

updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

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
