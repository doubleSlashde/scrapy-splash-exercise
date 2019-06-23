function main(splash)
    
    --- TODO: find corresponding css selectors!
    local LINK_MORE_REVIEWS = ''
    local LINK_EXPAND_REVIEW = ''

    --- go to place page
    splash:go(splash.args.url)
    assert(splash:wait(1.0))
    splash:set_viewport_full()

    --- go to review page
    local more_reviews_element = splash:select(LINK_MORE_REVIEWS)
    assert(more_reviews_element:mouse_click { y = 0 })
    assert(splash:wait(1.5))

    --- expand collapsed reviews
    local expand_buttons = splash:select_all(LINK_EXPAND_REVIEW)
    for i in pairs(expand_buttons) do
        assert(expand_buttons[i]:mouse_click())
        assert(splash:wait(0.05))
    end

    return splash:html()
end
