import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [emailData, setEmailData] = useState({
        sender: '',
        recipient: '',
        content: ''
    });
    const [result, setResult] = useState('');

    const handleChange = (e) => {
        setEmailData({ ...emailData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/process_email', emailData);
            setResult(`Suspicion Level: ${response.data.suspicion_level.toFixed(2)}%`);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h1>Suspicious Email Tracker</h1>
            <form onSubmit={handleSubmit}>
                <label>Sender: </label>
                <input type="email" name="sender" onChange={handleChange} required /><br />
                <label>Recipient: </label>
                <input type="email" name="recipient" onChange={handleChange} required /><br />
                <label>Email Content: </label>
                <textarea name="content" onChange={handleChange} required></textarea><br />
                <button type="submit">Analyze</button>
            </form>
            <h2>Result:</h2>
            <p>{result}</p>
        </div>
    );
}

export default App;
