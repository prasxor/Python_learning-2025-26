let txt = "ABcd@1$z"

// console.log(length(txt));
// console.log(txt.length);

let upperCounter = 0
let lowerCounter = 0
let digitCounter = 0
let specialCounter = 0

for (let i = 0; i < txt.length; i++) {
    const currentI = txt[i];

    if (currentI >= 'A' && currentI <= 'Z') {
        upperCounter++;
    }
    else if (currentI >= 'a' && currentI <= 'z') {
        lowerCounter++;
    }
    else if (currentI >= '0' && currentI <= '9') {
        digitCounter++;
    }
    else {
        specialCounter++;
    }
}

console.log("count of UpperCase:", upperCounter)
console.log("count of Lowercase:", lowerCounter)
console.log("count of Digits:", digitCounter)
console.log("count of Special Characters:", specialCounter)