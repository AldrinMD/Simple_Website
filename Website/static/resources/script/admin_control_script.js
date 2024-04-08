function target_selection_onclick() {
    if (document.getElementById("cards_image").checked || document.getElementById("Test2").checked) {
        document.getElementById("not_carousel").style.display = "block";
    } else document.getElementById("not_carousel").style.display = "none";

    if (document.getElementById("cards_image").checked) {
        document.getElementById("cards_selection").style.display = "block";
    } else document.getElementById("cards_selection").style.display = "none";

}

document.getElementById("upload_file_btn").addEventListener("change", 
function() {
    let reader = new FileReader();
    reader.readAsDataURL(this.files[0]);
    reader.onload = () => {
        document.getElementById("test_image").setAttribute("src", reader.result);
    }

    document.getElementById("selected_image").textContent = this.files[0].name
})