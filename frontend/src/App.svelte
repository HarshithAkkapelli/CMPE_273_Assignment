<script>
    import { onMount } from 'svelte';

    let chatPrompt = "";
    let response = "";

    async function sendMessage() {
        // Logic to send 'chatPrompt' to the server and receive 'response'
        try {
            const result = await fetch('http://localhost:3001/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: chatPrompt
                })
            });
            
            if (!result.ok) {
                throw new Error('Failed to fetch from API');
            }
            
            const data = await result.json();
            response = data.response;  // Assuming your response contains the reply in 'message' property
        } catch (error) {
            response = "Error: " + error.message;
        }
    }

    function cancelMessage() {
        chatPrompt = "";
        response = "";
    }
</script>

<div class="wrapper">
    <h1>Deloitte Auditor Enterprise Chat UI</h1>
    <div class="section">
        <h2>Chat Prompt</h2>
        <textarea bind:value={chatPrompt} placeholder="Enter your query..." rows=6></textarea>
    </div>
    <div class="button-container">
        <button class="send-button" on:click={sendMessage}>
            <span class="btn-text">Send</span>
            <img src="download.png" alt="OpenAI Logo" class="logo"/>
        </button>
        <button class="cancel-button" on:click={cancelMessage}>Cancel</button>
    </div>
    <div class="section">
        <h2>Response</h2>
        <textarea bind:value={response} rows=6 readonly></textarea>
    </div>
</div>

<style>
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(to right, #E55D87, #5FC3E4); /* Pink to blue gradient */
    }

    .wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 80%;
        margin: 0 auto;
        border-radius: 15px;
        background-color: #F5F5F5; /* Light grey background */
        padding: 2rem;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }

    h1 {
        color: #263238; /* Deep blue-grey */
        margin-bottom: 1rem;
        background-color: #FFD54F; /* Yellow background */
        padding: 0.5rem;
        border-radius: 5px;
    }

    h2 {
        margin: 0;
        padding: 10px;
        color: #FFFFFF;
        text-align: center;
        background-color: #009688; /* Teal background color */
    }

    .section {
        width: 100%;
        background-color: #E8EAF6; /* Very light blue background */
        border-radius: 5px;
        margin-bottom: 1rem;
        overflow: hidden; 
    }

    textarea {
        border-top: none; 
        margin-top: 0; 
        width: 100%;
        padding: 10px;
        border: none; /* Remove the border */
        border-radius: 0; /* Remove border radius */
        resize: vertical;
    }

    .button-container {
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .send-button, .cancel-button {
        padding: 10px 20px;
        border-radius: 5px;
        color: #fff; 
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    .send-button {
        background-color: #673AB7; /* Deep purple */
    }

    .send-button:hover {
        background-color: #512DA8; 
        transform: scale(1.05);
    }

    .cancel-button {
        background-color: #FF5722; /* Deep orange */
    }

    .cancel-button:hover {
        background-color: #E64A19;
        transform: scale(1.05);
    }

    .logo {
        height: 23px; 
    }
</style>

