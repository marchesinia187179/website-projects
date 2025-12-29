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
  
}

addProductForm.addEventListener('submit', event => {

});

loadProducts();