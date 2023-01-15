(() => {
    const openNavMenu = document.querySelector(".open-nav-menu"),
    navMenu = document.querySelector(".nav-menu"), 
    menuOverlay = document.querySelector(".menu-overlay"),
    mediaSize = 991;

    openNavMenu.addEventListener("click", toggleNav);
    menuOverlay.addEventListener("click", toggleNav);

    function toggleNav() {
        navMenu.classList.toggle("open");
        menuOverlay.classList.toggle("active");
        document.body.classList.toggle("hidden-scrolling");
    }

})();

