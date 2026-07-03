const markdownRaw = document.getElementById("markdown-source").textContent;
document.getElementById("content").innerHTML =
marked.parse(markdownRaw);
