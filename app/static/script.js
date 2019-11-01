
function toggleModal(button) {
    let modal = button.parentElement.querySelector(".modal");
    if (modal.style.display === 'none') {
        modal.style.display = '';
    } else {
        modal.style.display = 'none';
    }
}

function closeModal(button) {
    let modal = button.parentElement;
    modal.style.display = 'none';
}
