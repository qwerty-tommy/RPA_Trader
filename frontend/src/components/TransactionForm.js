import React, { useState } from "react";

const BACKEND_SERVER = "http://localhost:8000";

function TransactionForm({ title, endpoint }) {
  const [accountNumber, setAccountNumber] = useState("");
  const [password, setPassword] = useState("");
  const [stockName, setStockName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [message, setMessage] = useState("");

  const handleFormSubmit = (e) => {
    e.preventDefault();

    // Send POST request to backend
    fetch(BACKEND_SERVER + endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        account_number: accountNumber,
        password: password,
        stock_name: stockName,
        quantity: parseInt(quantity),
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        const result = data.result;
        if (result === true) {
          setMessage("Success");
        } else {
          setMessage("Fail");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        setMessage("Fail");
      });
  };

  return (
    <div>
      <h1>{title}</h1>
      <form onSubmit={handleFormSubmit}>
        <label htmlFor="accountNumber">Account Number:</label>
        <input
          type="text"
          id="accountNumber"
          value={accountNumber}
          onChange={(e) => setAccountNumber(e.target.value)}
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <label htmlFor="stockName">Stock Name:</label>
        <input
          type="text"
          id="stockName"
          value={stockName}
          onChange={(e) => setStockName(e.target.value)}
        />

        <label htmlFor="quantity">Quantity:</label>
        <input
          type="number"
          id="quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />

        <button type="submit">{title}</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default TransactionForm;
