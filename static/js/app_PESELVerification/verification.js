
window.onload = function() {
    console.log("Page (including images & styles) is fully loaded!");
    var peselField = document.getElementById("peselField");
    var sexField = document.getElementById("sexField");
    var dateOfBirth = document.getElementById("dateOfBirth")

    peselField.addEventListener('input', function() {
        console.log('validating')
        validate(peselField, sexField, dateOfBirth);
    });


};

function validate(peselField, sexField, dateOfBirthField){
    let validation = checkPesel(peselField.value)
    if (validation.value) {

        setSex(validation.sex, sexField);
        setDateOfBrith(peselField.value, dateOfBirthField)

        peselField.classList.remove("is-invalid");
        peselField.classList.add("is-valid");
    } else {
        removeOldErrors(peselField);
        setSex("", sexField);
        validation.error.forEach(function(error) {
            addNewError(error, peselField);
            peselField.classList.remove("is-valid");
            peselField.classList.add("is-invalid");

        });
    }
}

function checkPesel(pesel) {

    let result = {
        value: true,
        error: [],
        sex: "x"

    }
    if (typeof pesel !== "string" || pesel.length !== 11) {
        result.error.push("PESEL must be 11 digits long");
        result.value = false;
    }

    let Nan = false;
    for (let i = 0; i < pesel.length; i++) {
        if (isNaN(Number(pesel[i]))) {
            Nan = true;
        }
    }
    if (Nan){
        result.error.push("PESEL must only consist of digits");
        result.value = false;
    }


    let weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3];
    let digits = pesel.split("").map(Number);

    let sum = 0;
    for (let i = 0; i < weights.length; i++) {
        sum += weights[i] * digits[i];
    }

    let controlDigit = (10 - (sum % 10)) % 10;

    if (controlDigit !== digits[10]) {
        result.error.push("PESEL is incorrect");
        result.value = false;
    }
    result.sex = checkSex(digits[9]);
    return result;
}

function checkSex(digit) {
    return digit % 2 === 0 ? 'F' : 'M';
}

function setSex(sex, sexField) {
    sexField.value = sex;
}

function removeOldErrors(inputField) {
    let sibling = inputField.nextElementSibling;

    while (sibling) {
        let nextSibling = sibling.nextElementSibling;

        if (sibling.tagName.toLowerCase() === 'div') {
            sibling.remove();
        }


        sibling = nextSibling;
    }
}
function addNewError(message, inputField){
    let newDiv = document.createElement('div');
    newDiv.classList.add('invalid-feedback');
    newDiv.textContent = message;
    inputField.insertAdjacentElement('afterend', newDiv);
}

function setDateOfBrith(pesel, inputField){
    let year = Number(pesel.slice(0, 2));
    let month = Number(pesel.slice(2, 4));
    let day = Number(pesel.slice(4, 6));

    if (month >= 1 && month <= 12) {
        year += 1900;
    } else if (month >= 13 && month <= 32) {
        year += 2000;
        month -= 20;
    } else if (month >= 40 && month <= 42) {
        year += 2100;
        month -= 40;
    } else if (month >= 60 && month <= 72) {
        year += 2200;
        month -= 60;
    } else if (month >= 80 && month <= 92) {
        year += 1800;
        month -= 80;
    }
    let formattedMonth = "";
    let formattedDay = "";
    if (month<=9){
       formattedMonth = month.toString().padStart(2, "0");
    } else {
        formattedMonth = month.toString();
    }
    if (day<=9){
       formattedDay = day.toString().padStart(2, "0");
    } else {
        formattedDay = day.toString();
    }

    inputField.value = `${year}-${formattedMonth}-${formattedDay}`;

}