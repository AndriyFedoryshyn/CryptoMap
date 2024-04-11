import pandas as pd
import altair as alt
from data.crypto_map import merge
import pycountry
import altair_saver

def my_theme():
    return {
        'config': {
            'range': {'category': ['#8200ff', '#ca27ff', "#ffffff", "#808080"]}
        }
    }


alt.themes.register('my_theme', my_theme)
alt.themes.enable('my_theme')

alt.renderers.enable('altair_saver', fmts=['vega-lite', 'png'])


world_map = alt.Chart(merge).mark_geoshape(
).encode(
    color='Legality:N'
).properties(
    width=1000,
    height=600
).configure_legend(labelLimit=0, labelColor='white').configure_title(fontSize=14).configure(background='black')

world_map = world_map.configure_legend(labelLimit=0, labelColor='white')
world_map.save('../static/images/world_map.png')

