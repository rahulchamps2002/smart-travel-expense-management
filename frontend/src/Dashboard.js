import React, {useEffect, useState} from "react";
import {Pie, Line} from 'react-chartjs-2';

function Dashboard(){
    const [expenses, setExpenses] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/expenses')
            .then(response => response.json())
            .then(data => setExpenses(data));
    }, []);

    const categories = expenses.reduce((acc, expense) => {
        acc[expense.category] = (acc[expense.category] || 0) + expense.amount;
        return acc;
    }, {});

    const pieData = {
        labels: Object.keys(categories),
        datasets: [{
            data: Object.values(categories),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56']
        }]
    };

    return (
        <div>
            <h2>Expense Dashboard</h2>
            <Pie data={pieData} />
        </div>
    );
}

export default Dashboard;