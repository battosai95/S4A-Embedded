/**
 * Created by battosai on 08/02/16.
 */

(function (ext) {
    // Cleanup function when the extension is unloaded
    ext._shutdown = function () {
    };

    // Status reporting code
    // Use this to report missing hardware, plugin or unsupported browser
    ext._getStatus = function () {
        return {status: 2, msg: 'Ready'};
    };

    ext.pinMode = function(pinNumber, pinValue){
        console.log("pinMode function");
        var data = JSON.stringify({
            "objName": "iuletuirset"
        });

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
        });

        xhr.open("POST", "http://localhost:8080/arduinize", true);
        xhr.setRequestHeader("content-type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log(xhr.responseText)
            }
        };
        xhr.send(data);
    };

    ext.whenGreenFlagClicked = function () {
        console.log("whenGreenFlag function");
        var data = JSON.stringify({
            "objName": "Stage"
        });

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
                console.log(this.responseText);
            }
        });

        xhr.open("POST", "http://localhost:8080/arduinize", true);
        xhr.setRequestHeader("content-type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log(xhr.responseText)
            }
        };
        xhr.send(data);
    };

    var _getDefaultBlocks = function(){
        return {
            "scripts": [
                [226, 138,
                    [
                        ["whenGreenFlag"],
                        ["doForever",
                            [

                            ]
                        ]
                    ]
                ]
            ]
        };
    };

    // Block and block menu descriptions
    var descriptor = {
        blocks: [
            [" ", "Set Pin:%n as %m.inputOutput", "pinMode", 2, "input"],
            [" ", "digitalWrite Pin:%n as %m.highLow", "digitalWrite", 13, "high"],
            [" ", "analogWrite(PWM) Pin:%n  Value:%n", "analogWrite", 6, 255],
            [" ", "servoWrite Pin:%n Deg:%n", "servoWrite", 6, 120],
            [" ", "Tone Pin:%n Note:%n", "tone", 6, 1315],
            [" ", "noTone Pin:%n", "notone", 6],
            ["b", "digitalRead Pin:%n", "digitalRead", 2],
            ["r", "analogRead Pin: A%n", "analogRead", 0]
        ],
        "menus": {
            "inputOutput": ["input", "output"],
            "highLow": ["high", "low"]
        }
    };

    // Register the extension
    ScratchExtensions.register('Scratch vs Arduino', descriptor, ext);
})({});

var test = {
    "scripts": [
        [226, 138,
            [
                ["whenGreenFlag"],
                ["doForever",
                    [
                        ["A4S (Arduino For Scratch).tone", 2, 1315]
                    ]
                ]
            ]
        ]
    ]
};