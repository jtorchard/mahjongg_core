import unicodedata


def extract_name_from_unicode(unicode_tile):
    split_name = unicodedata.name(unicode_tile).split()

    tile_type = split_name[-1]
    if tile_type in ("CIRCLES", "CHARACTERS", "BAMBOOS"):
        _, _, rank, _, suit = split_name
        suit = suit[:-1]
    elif tile_type in ("WIND", "DRAGON"):
        _, _, rank, suit = split_name
    elif tile_type in ("SPRING", "SUMMER", "AUTUMN", "WINTER"):
        rank = tile_type
        suit = "season"
    elif tile_type in ("PLUM", "ORCHID", "BAMBOO", "CHRYSANTHEMUM"):
        rank = tile_type
        suit = "flower"
    else:
        raise ValueError

    return f"{rank.lower()}_{suit.lower()}"
