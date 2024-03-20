(function () {
    const menuBtn = document.querySelector("#menu");
    const showMoreBtn = document.querySelector("#showMore");


    const menu = document.querySelector("header nav");
    const morePictures = document.querySelectorAll(
        ".gallery img:not(img:first-child)"
    );


    let menuHidden = false;

    menuBtn.addEventListener("click", function () {
        console.log("a");

        menuHidden = !menuHidden;
        menu.hidden = menuHidden;
    });

    showMoreBtn.addEventListener("click", function () {
        console.log("a");

        menuHidden = !menuHidden;
        menu.computedStyleMap.di
    });


    
    
    menuBtn.click();
    showMoreBtn.click();

})();
