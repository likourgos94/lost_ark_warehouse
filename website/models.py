from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    marvelous_honor_leapstone = db.Column(db.Integer, default=0)
    great_honor_leapstone = db.Column(db.Integer, default=0)
    solar_protection = db.Column(db.Integer, default=0)
    solar_blessing = db.Column(db.Integer, default=0)
    solar_grace = db.Column(db.Integer, default=0)
    honor_shard_pouch_l = db.Column(db.Integer, default=0)
    honor_shard_pouch_m = db.Column(db.Integer, default=0)
    honor_shard_pouch_s = db.Column(db.Integer, default=0)
    obliteration_stone = db.Column(db.Integer, default=0)
    protection_stone = db.Column(db.Integer, default=0)
    crystallized_destruction_stone = db.Column(db.Integer, default=0)
    crystallized_protection_stone = db.Column(db.Integer, default=0)
    wild_flower = db.Column(db.Integer, default=0)
    shy_wild_flower = db.Column(db.Integer, default=0)
    bright_wild_flower = db.Column(db.Integer, default=0)
    crude_mushroom = db.Column(db.Integer, default=0)
    fresh_mushroom = db.Column(db.Integer, default=0)
    exquisite_mushroom = db.Column(db.Integer, default=0)
    timber = db.Column(db.Integer, default=0)
    tender_timber = db.Column(db.Integer, default=0)
    sturdy_timber = db.Column(db.Integer, default=0)
    fish = db.Column(db.Integer, default=0)
    redflesh_fish = db.Column(db.Integer, default=0)
    oreha_solar_carp = db.Column(db.Integer, default=0)
    natural_pearl = db.Column(db.Integer, default=0)
    ancient_relic = db.Column(db.Integer, default=0)
    rare_relic = db.Column(db.Integer, default=0)
    oreha_relic = db.Column(db.Integer, default=0)
    thick_raw_meat = db.Column(db.Integer, default=0)
    treated_meat = db.Column(db.Integer, default=0)
    tough_leather = db.Column(db.Integer, default=0)
    oreha_thick_meat = db.Column(db.Integer, default=0)
    iron_ore = db.Column(db.Integer, default=0)
    heavy_iron_ore = db.Column(db.Integer, default=0)
    strong_iron_ore = db.Column(db.Integer, default=0)
