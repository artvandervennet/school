"use strict";

(function () {
    const domino = document.querySelector("#domino");
    const knoppen = document.querySelectorAll("button");

    const vallen = function (event) {
        this.style.transform = "rotate(90deg)";
        this.style.transformOrigin = "100% 100%";

        let volgendei;

        for (let index = 0; index < knoppen.length; index++) {
            const element = knoppen[index];
            if (element === this) {
                volgendei = index + 1;
            }
        }

        if (volgendei < knoppen.length) {
            event.stopPropagation();
            const volgendeKnop = knoppen[volgendei];
            setTimeout(() => volgendeKnop.click(), 100); //delay voor duidelijkheid
        }
    };

    for (let i = 0; i < knoppen.length; i++) {
        const knop = knoppen[i];

        knop.addEventListener("click", vallen);
    }

    domino.addEventListener("click", function () {
        domino.style.backgroundColor = "darkred";
    });
})();
