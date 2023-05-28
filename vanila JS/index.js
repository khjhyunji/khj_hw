document.querySelector("#btn").onclick = function () {
    let img = document.createElement("img");
    img.setAttribute("src", "nijinsky.jpg");
    img.setAttribute("style", "width:300px;margin-top:20px;");
    document.body.append(img);
};
