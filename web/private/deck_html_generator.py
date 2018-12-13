# header and footer
# {{content}}
container_html = '''

<link rel="stylesheet" href="/static/style.css">
<link rel="stylesheet" href="/static/theme.css">

<main id="main">
    <div id="main-inner">
        <section class="section-decklist">
            <div class="hs-decklist-container">
                {{content}}
            </div>
        </section>
    </div>
</main>

<script src="/static/deck.js"></script>
<script src="/static/iframe_fit.js"></script>
'''

# hero header
# {{id}}  {{deck_code}}  {{deck_name}}
hero_html = '''

                <div class="hs-decklist-hero">
                    <div class="hs-decklist-hero-frame">
                        <img src="/static/img/CustomDeck_phone-Recovered.png" class="hero-frame">
                        <img src="https://art.hearthstonejson.com/v1/256x/{{id}}.jpg" class="hero-image">
                    </div>
                    <div class="hs-decklist-title">
                        <input id="deck-title-input" data-deckcode="{{deck_code}}" type="text" class="mdc-textfield__input" value="{{deck_name}}" maxlength="30">
                    </div>
                </div>

'''

# deck container
# {{content}}
deck_container = '''

                <ul class="mdc-list mdc-list--two-line mdc-list--avatar-list hs-decklist">
                    {{content}}
                </ul>

'''

# single card
# {{id}}  {{card_cost}}  {{name}}  {{lang}}
single_card = '''

                    <li class="mdc-list-item deck-entry deck-entry-without-amount">
                        <div class="hs-tile-img"><img src="https://art.hearthstonejson.com/v1/tiles/{{id}}.png"></div>
                        <div class="hs-tile-shade" style=""></div>
                        <div class="hs-tile-borders"></div>
                        <div class="hs-tile-mana"></div>
                        <div class="hs-tile-info"><span class="hs-tile-info-left mdc-list-item__start-detail" role="presentation">{{card_cost}}</span> <span class="hs-tile-info-middle mdc-list-item__text"><span>{{name}}</span></span><span class="hs-tile-info-right mdc-list-item__end-detail" aria-label="Amount" title="Amount" role="presentation"></span></div>
                        <div class="preview-card" style="display:none"><img data-imgsrc="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/512x/{{id}}.png" src="https://art.hearthstonejson.com/v1/render/latest/{{lang}}/256x/{{id}}.png"></div>
                    </li>

'''

# double cards
# {{id}}  {{card_cost}}  {{name}}  {{lang}}
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
# {{id}}  {{card_cost}}  {{name}}  {{lang}}
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

def generate_html(deck_array, deck_code, lang="zhCN", deck_name = "×"):
    # {{id}}  {{deck_code}}  {{deck_name}}
    if deck_name == "×":
         deck_name == deck_array["hero"][1]

    output_hero_html = hero_html.replace( \
                       '{{id}}', deck_array["hero"][0]).replace( \
                       '{{deck_name}}', deck_name).replace( \
                       '{{deck_code}}', deck_code)

    output_card_html = ""
    for item in deck_array["cards"]:
       #rarity_tags = ["FREE", "COMMON", "RARE", "EPIC", "LEGENDARY"]
       if item[4] == "LEGENDARY":
           card_template = star_card
       elif item[1] == 2:
           card_template = doulde_card
       else:
           card_template = single_card

       #{{id}}  {{card_cost}}  {{name}}  {{lang}}
       #('EX1_365', 1, '神圣愤怒', 5, 'RARE')
       output_card_html = output_card_html + card_template.replace( \
                          '{{id}}', item[0]).replace( \
                          '{{card_cost}}', str(item[3])).replace( \
                          '{{name}}', item[2]).replace( \
                          '{{lang}}', lang)

    deck_container_html = deck_container.replace('{{content}}', output_card_html)
    content_html = container_html.replace('{{content}}', output_hero_html + deck_container_html)

    return content_html

#key = input('Press any key to quit')
#quit()
