
$(".course .details").click(function(event) {
    let modals = $('.modal');
    modals.css('display', 'none');
    $(event.target.parentElement).find(modals).css('display', 'block');
});

$(".modal-close").click(function (event) {
    $(event.target.parentElement).css('display', 'none');
});
