$(function() {
    
    window.games = {
        startYear: 2013,
        nowYear: 2014,
        currentYear: 2014
    };

    games.prevYear = function () {
        if (games.currentYear > games.startYear) {
            games.currentYear--;
            $("#year").html(games.currentYear);
            games.loadGames();
        }
    };

    games.nextYear = function () {
        if (games.currentYear < games.nowYear) {
            games.currentYear++;
            $("#year").html(games.currentYear);
            games.loadGames();
        }
    };

    games.loadGames = function () {
        $("#big-game").hide(100);
         
         $("#small-games").animate({
            "margin-left": "-200%"
         }, 1000, "swing", function () {
            $("#small-games").load("/games/"+games.currentYear+"/", function () {
                games.bindClick();
                $("#small-games")
                .css("margin-left", "200%")
                .animate({
                    "margin-left": "0px"
                }, 1000, "swing");
             });
        });
         
         
    };

    var clickGame = function() {
        var $game = $(this),
            id = $game.attr("game");
        console.log("Clicked "+id);
        $("#big-game")
            .load("/runs/game/"+id+"/")
            .show(100);
    };

    games.bindClick = function () {
        console.log("Binding clicks..");
        $(".game")
            .unbind("click")
            .bind("click", clickGame);
    };
    
    games.bindClick();
});