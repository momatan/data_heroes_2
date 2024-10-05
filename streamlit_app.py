import streamlit as st
import yaml
import random

# read yaml file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


# add circle image small size
st.image('imgs/circle.jpg', width=100)

# add title
st.markdown('# おいでよ Data Heroes 体験版')

# japanese title
st.markdown('### 遭遇した状況を3つのアイテムで解決しよう！')
st.write('''
遭遇した状況を3つのアイテムで解決するゲームです。
以下のボタンを押すと、ランダムに状況とアイテムが表示されます。
あなたの解決策をみんなに説明しましょう。過半数が納得したら成功です。
アイテムはすべて使わなくても構いませんが、使ったアイテムの数が多いほど高得点です。
''')
# english title
st.markdown('### Solve the event with 3 items!')
st.write('''
This is a game to solve the event with 3 items.
Press the button below to show a random event and 3 items.
Explain your solution to everyone. If more than half of the people agree, you succeed.
You don't have to use all the items, but the more items you use, the higher your score.
''')

# # ad text
# st.markdown('### 製品版のボードゲームは技術書典17にて頒布予定です。')
# st.markdown('### The board game will be available at the event "Techbook Fest 17".')

# add button to show items and event
if st.button('Show me a random event and 3 items'):
    # pickup 1 event at random
    events = config['events']
    chosen_event = random.choice(events)
    col1, col2, col3 = st.columns(3)
    # show image of event with column width
    with col2:
        st.image(f"imgs/event_{chosen_event['id']}.jpg", caption="Event", use_column_width=True)

    # pickup 3 items at random
    items = config['items']
    chosen_items = random.sample(items, 3)
    # show image of items with column width
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(f"imgs/item_{chosen_items[0]['id']}.jpg", caption=chosen_items[0]['name'], use_column_width=True)
    with col2:
        st.image(f"imgs/item_{chosen_items[1]['id']}.jpg", caption=chosen_items[1]['name'], use_column_width=True)
    with col3:
        st.image(f"imgs/item_{chosen_items[2]['id']}.jpg", caption=chosen_items[2]['name'], use_column_width=True)

