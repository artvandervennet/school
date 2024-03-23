(function () {
    const menuBtn = document.querySelector("#menu");
    const showMoreBtn = document.querySelector("#showMore");

    const menu = document.querySelector("header nav");
    const morePictures = document.querySelectorAll(
        ".gallery img:not(img:first-child)"
    );
    const showMoreTekst = document.querySelector("#more");
    const showLessTekst = document.querySelector("#less");

    let menuHidden = true;
    let picHidden = true;

    menuBtn.addEventListener("click", function () {
        console.log("a");

        menu.className = menuHidden ? "visableMenu" : "";
        menuHidden = !menuHidden;
    });


    
    showMoreBtn.addEventListener("click", function () {
        morePictures.forEach((element) => {
            console.log(element);
            element.className = picHidden ? "visableImg" : "";
        });
        showLessTekst.className = picHidden ? "visableImg" : "";
        showMoreTekst.className = !picHidden ? "visableImg" : "";

        picHidden = !picHidden;
    });

    menuBtn.click();
    showMoreBtn.click();
})();
