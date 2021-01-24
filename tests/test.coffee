class Syntax
    constructor: (@name, @beautiful) ->

    print: ->
        console.log "I am #{@name} and I am " +
            if @beautiful then "beautiful" else "ugly"

fall_syntax = new Syntax("Fall Syntax", true)
fall_syntax.print()
