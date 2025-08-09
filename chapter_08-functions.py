## Rename the original document of chapter 8 as printing_models.py
## Then import the functions within it with the following methods
# import name_mdl

import printing_models

printing_models.display_message()


# from name_mdl import name_fnct

from printing_models import favorite_book

favorite_book('o menino maluquinho')


# from name_mdl import name_fnct as nf

from printing_models import make_shirt as ms

ms('tiny', "this is my friday's shirt")


# import name_mdl as nm

import printing_models as pm

pm.describe_city('auckland', 'new zealand')


# from name_mdl import *

from printing_models import *

is_this_real = get_plant_info('psychotria' ,'viridis', 
                              popular_name='chacrona', origin='amazon')
print(is_this_real)