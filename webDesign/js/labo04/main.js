"use strict";

(function () {
    // oef1
    const user = {
        firstname: "john",
        lastname: "Lennon",
        isDead: false,
    };

    user.age = 40;
    delete user.lastname;

    for (const key in user) {
        console.log(key + " " + user[key]);
    }

    //oef 2

    const ladder = {
        step: 0,
        maxStep: 3,
        up() {
            this.step++;
            if (this.step > this.maxStep) {
                this.step = 0;
                console.log("je bent eraf gevallen");
            }
            return this;
        },

        down() {
            this.step--;
            if (this.step < 0) {
                throw new Error(
                    "error, je zit in de kelder op verdiep: " + this.step
                );
            }
            return this;
        },

        showStep() {
            console.log(this.step);
        },
    };

    ladder.up();
    ladder.down();
    ladder.up();
    ladder.up();
    ladder.up();
    ladder.up();

    ladder.showStep();

    //oef3

    const Car = function (name = "a", brand = "bmw") {
        this.name = name;
        this.brand = brand;
        this.crashed = false;

        this.turnLeft = function () {
            if (!this.crashed) {
                if (this.brand === "bmw") {
                    console.log(name + " done");
                } else {
                    console.log(name + " is turning left");
                }
            } else {
                console.log("I cant turn when im dead");
            }
        };

        this.turnRight = function () {
            if (!this.crashed) {
                if (this.brand === "bmw") {
                    console.log(name + " done");
                } else {
                    console.log(name + " is turning right");
                }
            } else {
                console.log("I cant turn when im dead");
            }
        };

        this.crash = function () {
            console.error("car is crashed");
            this.crashed = true;
        };
    };

    const car1 = new Car("bob", "volvo");
    car1.turnLeft();
    car1.turnRight();
    car1.crash();
    car1.turnRight();

    const car2 = new Car();
    car2.turnLeft();
    car2.turnRight();
    car2.crash();
})();
