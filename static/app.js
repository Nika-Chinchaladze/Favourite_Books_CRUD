$("#userInput").keyup(function() {
    filterProducts();
})

function filterProducts() {
    var userInput = $("#userInput");
    var myFilter = userInput.val().toUpperCase();
    var eachProduct = $(".infoDiv");
    var eachHeading = $(".bookInfo");

    for (var i = 0; i < eachHeading.length; i++) {
        myh2 = eachHeading[i];
        textValue = myh2.textContent || myh2.innerHTML;
        if (textValue.toUpperCase().indexOf(myFilter) > -1) {
            eachProduct[i].style.display = "";
        }
        else {
            eachProduct[i].style.display = "none";
        }
    }
}