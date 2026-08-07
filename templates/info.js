let query = location.search;
const searchParams = new URLSearchParams(query);
const postcode = searchParams.get("postcode");

console.log(postcode);
if (postcode !== null) {
    document.getElementById("postcode").textContent = postcode;
} else {
    document.getElementById("postcode").textContent = "no postcode, return to index.html to see more info";
    window.location.href = "index.html";
};