$(".card-lecture").click(function() {
    var id = $(this).data("id");
    var lecture = $(this).data("lecture");
    var start = $(this).data("start");
    var end = $(this).data("end");
    var professor = $(this).data("professor");
    var code = $(this).data("code");
    var location = $(this).data("location");
    var day_of_week = $(this).data("day");

    if (day_of_week.length == 1) {
        day = "(" + day_of_week + ")";
    } else {
        day = "(" + day_of_week[0] + "), (" + day_of_week[1] + ")";
    }

    $("#modal-lecture-info-title").html(lecture);
    $("#modal-lecture-info-time").html(
        "강의 시간 : " +
            String("0" + start).slice(-2) +
            ":00 - " +
            String("0" + end).slice(-2) +
            ":50 | " +
            day
    );
    $("#modal-lecture-info-code").html("교과목 코드 : " + code);
    $("#modal-lecture-info-location").html("강의실 : " + location);
    $("#modal-lecture-info-professor").html("담당 교수 : " + professor);
    $("#modal-lecture-info-register").attr(
        "onclick",
        "location.href='/register/" + id + "'"
    );
    $("#modal-lecture-info").modal("show");
});

$(".lecture-time > a").click(function() {
    var id = $(this).data("id");
    var lecture = $(this).data("lecture");
    var start = $(this).data("start");
    var end = $(this).data("end");
    var professor = $(this).data("professor");
    var code = $(this).data("code");
    var location = $(this).data("location");
    var day_of_week = $(this).data("day");
    var memos = $(this).find("span");

    $(".memo-list").remove();

    for (var i = 0; i < memos.length; i++) {
        memo_id = $(memos[i]).data("memo-id");
        title = $(memos[i]).data("memo-title");
        var $tag = $(
            '<li class="memo-list">' +
                '<div class="memo-content" data-toggle="tooltip" data-placement="top" title="" data-original-title="">' +
                '<i class="material-icons ic-lecture-noti">assignment</i>' +
                '<span class="lecture-noti-title modal-memo">' +
                title +
                "</span>" +
                "</div>" +
                '<div class="memo-btn">' +
                "<a href=/delete-memo/" +
                memo_id +
                ">" +
                '<i class="material-icons ic-lecture-noti">delete</i>' +
                "</a></div></li>"
        );

        $("#modal-memo-list").append($tag);
    }

    if (day_of_week.length == 1) {
        day = "(" + day_of_week + ")";
    } else {
        day = "(" + day_of_week[0] + "), (" + day_of_week[1] + ")";
    }

    $("#modal-lecture-task-title").html(lecture);
    $("#modal-lecture-task-time").html(
        "강의 시간 : " +
            String("0" + start).slice(-2) +
            ":00 - " +
            String("0" + end).slice(-2) +
            ":50 | " +
            day
    );
    $("#modal-lecture-task-code").html("교과목 코드 : " + code);
    $("#modal-lecture-task-location").html("강의실 : " + location);
    $("#modal-lecture-task-professor").html("담당 교수 : " + professor);
    $("#modal-lecture-task-delete").attr(
        "onclick",
        "location.href='/delete/" + id + "'"
    );
    // $(".modal-memo").html($(memos[0]).data("memo-title"));
    $("#memo-form").attr("action", "/create-memo/" + id);
    $("#memo-delete").attr("href", "location.href='/delete-delete/" + id + "'");
    $("#modal-lecture-task").modal("show");
});

$(function() {
    $('[data-toggle="tooltip"]').tooltip();
});

$(function() {
    $('[data-toggle="popover"]').popover({
        container: "body",
        html: true,
        placement: "right",
        sanitize: false,
        content: function() {
            return $("#PopoverContent").html();
        }
    });
});
