import React, { useState } from "react";

const BACKEND_SERVER = "http://localhost:8000";

function UserInfo() {
  const [accountInfo, setAccountInfo] = useState(null);
  const [accountNumber, setAccountNumber] = useState("");
  const [password, setPassword] = useState("");

  const handleFormSubmit = (e) => {
    e.preventDefault();

    // Send POST request to backend
    fetch(BACKEND_SERVER + "/user/info", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        account_number: accountNumber,
        password: password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setAccountInfo(data.result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div>
      <h1>User Information</h1>
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

        <button type="submit">Submit</button>
      </form>

      {accountInfo && (
        <div>
          <h2>Account Information</h2>
          <p>Account Count: {accountInfo.account_count}</p>
          <p>User ID: {accountInfo.user_id}</p>
          <p>User Name: {accountInfo.user_name}</p>
          {/* Render other account information as needed */}
        </div>
      )}
    </div>
  );
}

export default UserInfo;
