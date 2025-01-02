document.addEventListener("DOMContentLoaded", () => {
    gsap.from("nav ul li", { opacity: 0, y: -20, duration: 1, stagger: 0.2 });
    gsap.from("#welcome h1", { opacity: 0, scale: 0.5, duration: 1, ease: "elastic" });
    gsap.from("#welcome p", { opacity: 0, y: 20, duration: 1, stagger: 0.3 });
});
