const passcodeDiv = document.getElementById('Passcode-div');
const privateRoomCheckbox = document.getElementById('private-room-checkbox');
const passcodeInput = document.getElementById('passcode-input');

privateRoomCheckbox.addEventListener('change', (event) => {
    if (event.target.checked) {
        passcodeDiv.hidden = false;
        passcodeInput.setAttribute('required', '');
    } else {
        passcodeDiv.hidden = true;
    }
});