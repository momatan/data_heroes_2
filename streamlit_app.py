import streamlit as st
import yaml
import random

# read yaml file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# add title
st.markdown('# おいでよ Data Heroes 体験版')

# japanese title
st.markdown('### 遭遇した状況を3つのアイテムで解決しよう！')
# english title
st.markdown('### Solve the event with 3 items!')

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

