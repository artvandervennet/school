(function () {
    const menuBtn = document.querySelector("#menu");

    const showMoreBtn = document.querySelector("#showMore");
    const morePictures = document.querySelectorAll(
        ".gallery img:not(img:first-child)"
    );
    const showMoreTekst = document.querySelector("#more");
    const showLessTekst = document.querySelector("#less");

    let picHidden = true;

    menuBtn.addEventListener("click", function () {
        menuBtn.ariaExpanded = !(menuBtn.ariaExpanded === "true");
    });

    
    
    showMoreBtn.addEventListener("click", function () {
        morePictures.forEach((element) => {
            
            element.className = picHidden ? "visableImg" : "";
        });
        showLessTekst.className = picHidden ? "visableImg" : "";
        showMoreTekst.className = !picHidden ? "visableImg" : "";

        picHidden = !picHidden;
    });

    showMoreBtn.click();
})();
