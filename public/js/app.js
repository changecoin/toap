$(function() {
    $(".tip-form [type='text']").on("keypress", function(e) {
        if (e.keyCode === "13") {
            $(".tip-form").submit();
        }
    });

    $(".tip-form").on("submit", function(e) {
        e.preventDefault();

        $.post("/tip-url", $(".tip-form").serialize(), function(data) {
            $("body").addClass("done");
            $(".qr")
                .attr("src", "https://api.qrserver.com/v1/create-qr-code/?data=" + data.magic_url + "&size=320x320");
            $(".link .text span").text(data.magic_url);
        });
    });

    $(".print button").on("click", function(e) {
        e.preventDefault();
        window.print();
    });
});
