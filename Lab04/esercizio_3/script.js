const apiUrl = 'https://fakestoreapi.com/products';

const tableBody = document.querySelector('#productsTable tbody');
const addProductForm = document.querySelector('#addProductForm');

function renderProduct(product) {
  const tr = document.createElement('tr');
  tr.innerHTML = `
    <td>${product.id}</td>
    <td>${product.title}</td>
    <td>${product.price}</td>
    <td>${product.description}</td>
  `;
  tableBody.appendChild(tr);
}

function loadProducts() {

  fetch(apiUrl)
  .then(response => {

    if (!response.ok) {
      throw new Error("Response error: " + response.status);
    }
    return response.json();

  })
  .then(data => {

    for (let i = 0; i < 5; i++) {
      renderProduct(data[i]);
    }

  })
  .catch(error => {
    console.error("Fetch GET error: ", error);
  });
  
}

addProductForm.addEventListener('submit', event => {
  /* The preventDefault() method of the Event interface tells the user agent 
   * that the event is being explicitly handled, so its default action, 
   * such as page scrolling, link navigation, or pasting text, 
   * should not be taken. */
  event.preventDefault();

  const formData = new FormData(addProductForm);

  const newProduct = {
    title: formData.get('title'),
    price: parseFloat(formData.get('price')),
    description: formData.get('description') || ''
  }

  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(newProduct)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Response error: " + response.status);
    }
    return response.json();

  })
  .then(data => {
    renderProduct(data);

  })
  .catch(error => {
    console.error("Fetch POST error: ", error);
    document.getElementById("errorMessage").innerHTML = "Error while inserting the new product";
  
  });

  // The reset() method resets the values of all elements in a form (same as clicking the Reset button).
  addProductForm.reset();

});

loadProducts();
