$(document).ready(function() {
    var queryTimer = 0;
    var delay = 600;
    $('#definition_suggestion').keyup(function(){
        var query;
        query = $(this).val();

        if (queryTimer) {
            clearTimeout(queryTimer);
        }

        queryTimer = setTimeout(function() {
            $.get('/help/suggest_definition/', {definition_suggestion: query}, function(data){
                $('#defs').html(data);
            });
        }, delay);
    });
    

    $('#question_suggestion').keyup(function(){
        var query;
        query = $(this).val();

        if (queryTimer) {
            clearTimeout(queryTimer);
        }
        queryTimer = setTimeout(function() {
            $.get('/help/suggest_question/', {question_suggestion: query}, function(data){
                $('#ques').html(data);
            });
        }, delay);
    });

    $('#question_suggestion2').keyup(function(){
        var query;
        query = $(this).val();

        if (queryTimer) {
            clearTimeout(queryTimer);
        }
        queryTimer = setTimeout(function() {
            $.get('/help/suggest_question/', {question_suggestion: query}, function(data){
                $('#ques2').html(data);
            });
        }, delay);
    });
    
    
    $("#searchForm").submit(function() {
        search($("#searchText").get(0));
        return false;
    });

});

