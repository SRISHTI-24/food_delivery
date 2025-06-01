const BASE_URL = "http://localhost:8001"; // Replace with your actual User Service URL

async function getResturants() {
  const hour = document.getElementById("hourInput").value;
  const list = document.getElementById("resturantList");
  list.innerHTML = "";

  try {
    const res = await fetch(`${BASE_URL}/api/user/resturants/available?hour=${hour}`);
    if (!res.ok) throw new Error("No resturants available");

    const resturants = await res.json();
    resturants.forEach(r => {
      const li = document.createElement("li");
      li.textContent = `${r.name} (Rating: ${r.rating})`;
      list.appendChild(li);
    });
  } catch (err) {
    list.innerHTML = `<li>Error: ${err.message}</li>`;
  }
}

async function placeOrder() {
  const jsonInput = document.getElementById("orderJson").value;
  const resBox = document.getElementById("orderResponse");
  try {
    const response = await fetch(`${BASE_URL}/api/user/orders`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonInput,
    });
    const result = await response.json();
    resBox.textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    resBox.textContent = `Error placing order: ${err.message}`;
  }
}

async function submitRating() {
  const jsonInput = document.getElementById("ratingJson").value;
  const resBox = document.getElementById("ratingResponse");
  try {
    const response = await fetch(`${BASE_URL}/api/user/ratings`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonInput,
    });
    const result = await response.json();
    resBox.textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    resBox.textContent = `Error submitting rating: ${err.message}`;
  }
}
