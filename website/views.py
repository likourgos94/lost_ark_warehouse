from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.models import User
from . import db
import json
import sqlalchemy




views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@login_required
def home():
    username = User.query.filter_by(id=current_user.id).first().first_name
    marvelous_honor_leapstone = User.query.filter_by(
        id=current_user.id).first().marvelous_honor_leapstone
    great_honor_leapstone = User.query.filter_by(
        id=current_user.id).first().great_honor_leapstone
    solar_protection = User.query.filter_by(
        id=current_user.id).first().solar_protection
    solar_blessing = User.query.filter_by(
        id=current_user.id).first().solar_blessing
    solar_grace = User.query.filter_by(id=current_user.id).first().solar_grace
    honor_shard_pouch_l = User.query.filter_by(
        id=current_user.id).first().honor_shard_pouch_l
    honor_shard_pouch_m = User.query.filter_by(
        id=current_user.id).first().honor_shard_pouch_m
    honor_shard_pouch_s = User.query.filter_by(
        id=current_user.id).first().honor_shard_pouch_s
    obliteration_stone = User.query.filter_by(
        id=current_user.id).first().obliteration_stone
    protection_stone = User.query.filter_by(
        id=current_user.id).first().protection_stone
    crystallized_destruction_stone = User.query.filter_by(
        id=current_user.id).first().crystallized_destruction_stone
    crystallized_protection_stone = User.query.filter_by(
        id=current_user.id).first().crystallized_protection_stone
    wild_flower = User.query.filter_by(id=current_user.id).first().wild_flower
    shy_wild_flower = User.query.filter_by(
        id=current_user.id).first().shy_wild_flower
    bright_wild_flower = User.query.filter_by(
        id=current_user.id).first().bright_wild_flower
    crude_mushroom = User.query.filter_by(
        id=current_user.id).first().crude_mushroom
    fresh_mushroom = User.query.filter_by(
        id=current_user.id).first().fresh_mushroom
    exquisite_mushroom = User.query.filter_by(
        id=current_user.id).first().exquisite_mushroom
    timber = User.query.filter_by(id=current_user.id).first().timber
    tender_timber = User.query.filter_by(
        id=current_user.id).first().tender_timber
    sturdy_timber = User.query.filter_by(
        id=current_user.id).first().sturdy_timber
    iron_ore = User.query.filter_by(id=current_user.id).first().iron_ore
    heavy_iron_ore = User.query.filter_by(
        id=current_user.id).first().heavy_iron_ore
    strong_iron_ore = User.query.filter_by(
        id=current_user.id).first().strong_iron_ore
    fish = User.query.filter_by(id=current_user.id).first().fish
    redflesh_fish = User.query.filter_by(
        id=current_user.id).first().redflesh_fish
    oreha_solar_carp = User.query.filter_by(
        id=current_user.id).first().oreha_solar_carp
    natural_pearl = User.query.filter_by(
        id=current_user.id).first().natural_pearl
    ancient_relic = User.query.filter_by(
        id=current_user.id).first().ancient_relic
    rare_relic = User.query.filter_by(id=current_user.id).first().rare_relic
    oreha_relic = User.query.filter_by(id=current_user.id).first().oreha_relic
    thick_raw_meat = User.query.filter_by(
        id=current_user.id).first().thick_raw_meat
    treated_meat = User.query.filter_by(
        id=current_user.id).first().treated_meat
    tough_leather = User.query.filter_by(
        id=current_user.id).first().tough_leather
    oreha_thick_meat = User.query.filter_by(
        id=current_user.id).first().oreha_thick_meat

    return render_template("home.html", user=current_user, username=username.capitalize(), marvelous_honor_leapstone=marvelous_honor_leapstone, great_honor_leapstone=great_honor_leapstone,
                           solar_protection=solar_protection, solar_blessing=solar_blessing, solar_grace=solar_grace, honor_shard_pouch_l=honor_shard_pouch_l, honor_shard_pouch_m=honor_shard_pouch_m,
                           honor_shard_pouch_s=honor_shard_pouch_s, obliteration_stone=obliteration_stone, protection_stone=protection_stone, crystallized_destruction_stone=crystallized_destruction_stone,
                           crystallized_protection_stone=crystallized_protection_stone, shy_wild_flower=shy_wild_flower, bright_wild_flower=bright_wild_flower, crude_mushroom=crude_mushroom, fresh_mushroom=fresh_mushroom,
                           exquisite_mushroom=exquisite_mushroom, timber=timber, tender_timber=tender_timber, sturdy_timber=sturdy_timber, iron_ore=iron_ore, heavy_iron_ore=heavy_iron_ore, strong_iron_ore=strong_iron_ore,
                           fish=fish, redflesh_fish=redflesh_fish, oreha_solar_carp=oreha_solar_carp, natural_pearl=natural_pearl, ancient_relic=ancient_relic, rare_relic=rare_relic, oreha_relic=oreha_relic, thick_raw_meat=thick_raw_meat,
                           treated_meat=treated_meat, tough_leather=tough_leather, oreha_thick_meat=oreha_thick_meat, wild_flower=wild_flower)


@views.route('/', methods=['POST'])
@login_required
def update_values():
    user = current_user
    data=request.form
    for column, amount in data.items():
        if amount != "":
            setattr(user, column, amount)
    db.session.commit()
        

    return home()
