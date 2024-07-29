const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const listProducts = [
  { itemId: 1, itemName: "Suitcase 250", price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: "Suitcase 450", price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: "Suitcase 650", price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: "Suitcase 1050", price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => listProducts.find(item => item.itemId === id);

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
};

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: "Product not found" });
    return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId) || item.initialAvailableQuantity;

  res.json({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
    currentQuantity: parseInt(currentQuantity, 10)
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: "Product not found" });
    return;
  }

  let currentQuantity = await getCurrentReservedStockById(itemId) || item.initialAvailableQuantity;
  currentQuantity = parseInt(currentQuantity, 10);

  if (currentQuantity <= 0) {
    res.json({ status: "Not enough stock available", itemId });
    return;
  }

  reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: "Reservation confirmed", itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

