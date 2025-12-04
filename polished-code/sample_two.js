const API_URL = "https://example.com/api/products";
const PRICE_THRESHOLD = 50;

/**
 * Fetches products from the API and renders those below the price threshold.
 */
async function loadProd() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
        }

        const products = await response.json();
        
        // Filter products based on business logic
        const affordableProducts = products.filter(product => product.price < PRICE_THRESHOLD);

        renderProducts(affordableProducts);

    } catch (error) {
        console.error("Error loading products:", error);
    }
}

/**
 * Renders the list of products to the DOM.
 * Uses a DocumentFragment to minimize reflows and textContent for security.
 * 
 * @param {Array} products - List of product objects to display
 */
function renderProducts(products) {
    const listElement = document.getElementById("list");

    if (!listElement) {
        console.warn("Target element 'list' not found in DOM.");
        return;
    }

    // Clear previous results
    listElement.innerHTML = "";

    const fragment = document.createDocumentFragment();

    products.forEach(product => {
        const itemDiv = document.createElement("div");
        itemDiv.className = "p";
        // Use textContent instead of innerHTML to prevent XSS vulnerabilities
        itemDiv.textContent = `${product.name} - ${product.price}`;
        fragment.appendChild(itemDiv);
    });

    listElement.appendChild(fragment);
}

// Initialize
loadProd();