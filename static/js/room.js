// Get the user's first name and websocket-url from the HTML
const first_name = JSON.parse(document.getElementById('first_name').textContent);
const websocketUrl = document.getElementById('websocket-url').dataset.url;

// Add event listeners for sending messages
document.querySelector('#submit').onclick = function (e) {
    sendMessage();
};

document.querySelector('#input').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Open a websocket connection to the chat room
const chatSocket = new WebSocket(
    (window.location.protocol === 'https:' ? 'wss://' : 'ws://') + websocketUrl
);

// Send a message to the chat room
function sendMessage() {
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;
    if (message.trim() !== '') {
        chatSocket.send(JSON.stringify({
            'message': message,
            'first_name': first_name
        }));
    }
    messageInputDom.value = '';
}


// Handle messages received from the server
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    // If the message is a system message, add it to the chat with a "Server" label
    if (data.type === 'connected_message' || data.type === 'disconnected_message') {
        const bgColorClass = data.type === 'connected_message' ? 'bg-green-100' : 'bg-rose-100';
        document.querySelector('#chat-text').innerHTML += `<p class="mb-1 py-2 px-4 rounded ${bgColorClass} text-black text-center"><b>Server</b>: ${data.message}<br></p>`;
    }

    // Otherwise, add it to the chat with the user's name
    else {
        if (data.first_name === first_name){
            document.querySelector('#chat-text').innerHTML += `<p class="mb-1 py-2 px-4 rounded bg-green-100 text-black text-right"><b>${data.message}</p>`
        }
        else{
            document.querySelector('#chat-text').innerHTML += `<p class="mb-1 py-2 px-4 rounded bg-rose-100 text-black"><b>${data.first_name}</b>: ${data.message}</p>`
        }
    }

    // Scroll to the bottom of the chat window
    scrollToBottom();
}

// Scroll to the bottom of the chat window
function scrollToBottom() {
    let objDiv = document.getElementById("chat-text");
    objDiv.scrollTop = objDiv.scrollHeight;
}

// Trigger the scroll function on page load
scrollToBottom();
