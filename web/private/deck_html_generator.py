# header and footer
# {{content}}
container_html = '''

<link rel="stylesheet" href="/static/style.css">
<main>
    <div id="main-inner">
        <section class="section-decklist">
            <div class="hs-decklist-container">
                {{content}}
            </div>
        </section>
    </div>
</main>

'''

# hero header
# {{id}}  {{deck_code}}  {{deck_name}}
hero_html = '''

                <div class="hs-decklist-hero"><img src="https://art.hearthstonejson.com/v1/256x/{{id}}.jpg">
                    <div class="hs-decklist-title">
                        <input id="deck-title-input" data-deckcode="{{deck_code}}" type="text" class="mdc-textfield__input" value="{{deck_name}}" maxlength="30">
                    </div>
                </div>

'''

# deck container
# {{content}}
deck_container_html = '''

                <ul class="mdc-list mdc-list--two-line mdc-list--avatar-list hs-decklist">
                    {{content}}
                </ul>

'''

# single card
# {{id}}  {{card_cost}}  {{name}}  {{lang}}
single_card = '''

                    <li class="mdc-list-item deck-entry deck-entry-without-amount">
                        <div class="hs-tile-img"><img src="https://art.hearthstonejson.com/v1/tiles/{{id}}"></div>
                        <div class="hs-tile-shade" style=""></div>
                        <div class="hs-tile-borders"></div>
                        <div class="hs-tile-mana"></div>
                        <div class="hs-tile-info"><span class="hs-tile-info-left mdc-list-item__start-detail" role="presentation">{{card_cost}}</span> <span class="hs-tile-info-middle mdc-list-item__text"><span>{{name}}</span></span><span class="hs-tile-info-right mdc-list-item__end-detail" aria-label="Amount" title="Amount" role="presentation"></span></div>
                        <div class="preview-card" style="display:none"><img data-imgsrc="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/512x/{{id}}.png" src="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/256x/{{id}}.png"></div>
                    </li>

'''

# double cards
{{id}}  {{card_cost}}  {{name}}  {{lang}}
doulde_card = '''

                    <li class="mdc-list-item deck-entry deck-entry-with-amount">
                        <div class="hs-tile-img"><img src="https://art.hearthstonejson.com/v1/tiles/{{id}}.png"></div>
                        <div class="hs-tile-shade" style=""></div>
                        <div class="hs-tile-borders"></div>
                        <div class="hs-tile-mana"></div>
                        <div class="hs-tile-info"><span class="hs-tile-info-left mdc-list-item__start-detail" role="presentation">{{card_cost}}</span> <span class="hs-tile-info-middle mdc-list-item__text"><span>{{name}}</span></span><span class="hs-tile-info-right mdc-list-item__end-detail" aria-label="Amount" title="Amount" role="presentation">2</span></div>
                        <div class="preview-card" style="display:none">
                        <img src="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/256x/{{id}}.png"></div>
                    </li>

'''

# LEGENDARY card (star)
{{id}}  {{card_cost}}  {{name}}  {{lang}}
star_card = '''

                    <li class="mdc-list-item deck-entry deck-entry-with-amount">
                        <div class="hs-tile-img"><img src="https://art.hearthstonejson.com/v1/tiles/{{id}}.png"></div>
                        <div class="hs-tile-shade" style=""></div>
                        <div class="hs-tile-borders"></div>
                        <div class="hs-tile-mana"></div>
                        <div class="hs-tile-info"><span class="hs-tile-info-left mdc-list-item__start-detail" role="presentation">{{card_cost}}</span> <span class="hs-tile-info-middle mdc-list-item__text"><span>{{name}}</span></span><span class="hs-tile-info-right mdc-list-item__end-detail" aria-label="Amount" title="Amount" role="presentation"><img src="/static/img/star.png"></span></div>
                        <div class="preview-card">
                        <img src="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/256x/{{id}}.png"></div>
                    </li>

'''

key = input('Press any key to quit')
quit()
