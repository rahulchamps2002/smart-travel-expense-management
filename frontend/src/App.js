import React, {useState} from "react";

function App() {
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('amount', amount);
    formData.append('category', category);
    formData.append('date', date);
    formData.append('receipt', receipt);

    fetch('localhost:5000/expenses',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: formData
    }).then(responnse => response.json())
        .then(data => console.log(data))
  }

  const handleFileChange = (e) => {
    setReceipt(e.target.files[0]);
  }

  return(
      <div>
        <h1>Expense Input</h1>
        <form onSubmit={handleSubmit}>
          <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" required />
          <input type="text" value={category} onChange={(e) => setCategory(e.target.value)} placeholder="Category" required />
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
          <input type="file" onChange={handleFileChange} required />
          <button type="submit">Add Expense</button>
        </form>
      </div>
  );
}

export default App;
