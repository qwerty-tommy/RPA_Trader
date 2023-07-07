import React from "react";
import TransactionForm from "./TransactionForm";

function Buying() {
  return <TransactionForm title="Buying" endpoint="/transaction/buying" />;
}

export default Buying;
