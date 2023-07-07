import React from "react";
import TransactionForm from "./TransactionForm";

function Selling() {
  return <TransactionForm title="Selling" endpoint="/transaction/selling" />;
}

export default Selling;
