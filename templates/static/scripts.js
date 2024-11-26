function sendAction(action) {
    fetch('/action', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'action': action })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('state').innerText = 'Estado Atual: ' + data.state;
        document.getElementById('message').innerText = data.message;
    });
}

function simulatePassenger() {
    fetch('/simulate', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('state').innerText = 'Estado Atual: ' + data.state;
        document.getElementById('message').innerText = 'Ação Simulada: ' + data.action + ' - ' + data.message;
    });
}
