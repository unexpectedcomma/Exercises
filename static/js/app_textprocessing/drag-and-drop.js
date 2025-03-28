document.addEventListener("DOMContentLoaded", function () {
    let dropZone = document.getElementById("dropZone");
    let fileInput = document.querySelector("#fileInput");  // Use querySelector in case of duplicates


    dropZone.addEventListener("dragover", (event) => {
        event.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", () => dropZone.classList.remove("dragover"));

    dropZone.addEventListener("drop", (event) => {
        event.preventDefault();
        dropZone.classList.remove("dragover");

        let files = event.dataTransfer.files;

        if (files.length > 0) {
            fileInput.files = files;  // Assign dropped files to the input
            console.log("Dropped files:", fileInput.files);
        }
    });

    fileInput.addEventListener("change", (event) => {
        console.log("Selected files:", event.target.files);
    });
});