async function calcDistance() {
    const p1 = document.getElementById("p1").value;
    const p2 = document.getElementById("p2").value;
    const unit = document.getElementById("unit1").value;

    const res = await fetch("/distance", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({p1, p2, unit})
    });
    const data = await res.json();
    document.getElementById("distanceResult").innerText =
        "Distance: " + data.distance + " " + unit;
}

async function formatHP() {
    const name = document.getElementById("hpName").value || "HP_UNNAMED";
    const point = document.getElementById("hpPoint").value;
    const unit = document.getElementById("unit2").value;

    const res = await fetch("/format", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, point, unit})
    });
    const data = await res.json();
    document.getElementById("formattedHP").innerText = data.formatted;
}

function copyToClipboard() {
    const text = document.getElementById("formattedHP").innerText;
    navigator.clipboard.writeText(text)
        .then(() => alert("Copied to clipboard"))
        .catch(() => alert("Failed to copy"));
}
