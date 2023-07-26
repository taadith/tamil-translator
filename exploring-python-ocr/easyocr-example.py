#%%
import PIL
from PIL import ImageDraw

#%%
im = PIL.Image.open("tamil-text.jpeg")
im

# %%
import easyocr
reader = easyocr.Reader(['ta','en'])

#%%
result = reader.readtext("tamil-text.jpeg")